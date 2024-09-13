import sys

import jieba
import re
import numpy as np


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
    cut_words = jieba.cut(content_p, cut_all=False)
    cut_words_dif = jieba.cut(content_p_dif, cut_all=False)
    seg_list_p = "/".join(cut_words).split("/")
    seg_list_dif_p = "/".join(cut_words_dif).split("/")
    return seg_list_p, seg_list_dif_p


# 计算余弦相似度
def cosine_similarity(seg_list_cos, seg_list_dif_cos):
    keywords = list(set(seg_list_cos + seg_list_dif_cos))
    # 向量化
    word_vector1 = np.zeros(len(keywords))
    word_vector2 = np.zeros(len(keywords))

    for i in range(len(keywords)):
        # 遍历keywords中每个词在句子中的出现次数
        for j in range(len(seg_list_cos)):
            if keywords[i] == seg_list_cos[j]:
                word_vector1[i] += 1
        for k in range(len(seg_list_dif_cos)):
            if keywords[i] == seg_list_dif_cos[k]:
                word_vector2[i] += 1
    # 求值
    dist_cos = float(np.dot(word_vector1, word_vector2) / (np.linalg.norm(word_vector1) * np.linalg.norm(word_vector2)))
    return dist_cos


if __name__ == "__main__":
    oriFile = sys.argv[1]
    difFile = sys.argv[2]
    outFile = sys.argv[3]
    content, content_dif = readFile(oriFile, difFile)
    # print(content)
    # print(content_dif)
    seg_list, seg_list_dif = process(content, content_dif)
    dist = cosine_similarity(seg_list, seg_list_dif)
    outputFile(dist, outFile)

# print(seg_list)
# print(seg_list_dif)

# print(word_vector1)
# print(word_vector2)
