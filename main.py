import sys
# import cProfile
import jieba
import re
import numpy as np
from collections import Counter
from functools import lru_cache


# 缓存重复分词
@lru_cache(maxsize=1000)
def cached_cut(text):
    return list(jieba.cut(text, cut_all=False))


# content = "今天是星期天，天气晴，今天晚上我要去看电影。"
# content_add = "今天是周天，天气晴朗，我晚上要去看电影。"


# 读文件
def readFile(ori_file, dif_file):
    with open(ori_file, "r", encoding="utf-8") as f:
        content_r = f.read()
    with open(dif_file, "r", encoding="utf-8") as f:
        content_r_dif = f.read()
        # 去掉无效字符
    content_r = re.sub(r'[^\w\s]|\s+', '', content_r)
    content_r_dif = re.sub(r'[^\w\s]|\s+', '', content_r_dif)
    return content_r, content_r_dif


# 写文件
def outputFile(dist_o, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{dist_o: .2f}")


# 分词
def process(content_p, content_p_dif):
    seg_list_p = cached_cut(content_p)
    seg_list_dif_p = cached_cut(content_p_dif)

    # print(seg_list_p)
    # print(seg_list_dif_p)

    return seg_list_p, seg_list_dif_p


# 计算余弦相似度
def cosine_similarity(seg_list_cos, seg_list_dif_cos):
    keywords = list(set(seg_list_cos + seg_list_dif_cos))

    # 计算词频
    counter1 = Counter(seg_list_cos)
    counter2 = Counter(seg_list_dif_cos)

    # 向量化
    word_vector1 = np.array([counter1.get(word, 0) for word in keywords])
    word_vector2 = np.array([counter2.get(word, 0) for word in keywords])

    # 计算余弦相似度
    dot_product = np.dot(word_vector1, word_vector2)
    norm1 = np.linalg.norm(word_vector1)
    norm2 = np.linalg.norm(word_vector2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    dist_cos = float(dot_product / (norm1 * norm2))
    # print(dist_cos)
    return dist_cos


if __name__ == "__main__":
    oriFile = sys.argv[1]
    difFile = sys.argv[2]
    outFile = sys.argv[3]

    # oriFile = "orig.txt"
    # difFile = "orig_0.8_dis_1.txt"
    # outFile = "out.txt"

    content, content_dif = readFile(oriFile, difFile)

    seg_list, seg_list_dif = process(content, content_dif)
    dist = cosine_similarity(seg_list, seg_list_dif)
    outputFile(dist, outFile)

    # cProfile.run('readFile(oriFile, difFile)')
    # cProfile.run('process(content, content_dif)')
    # cProfile.run('cosine_similarity(seg_list, seg_list_dif)')
    # cProfile.run('outputFile(dist, outFile)')
