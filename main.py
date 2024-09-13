import sys

import jieba
import re
import numpy as np


# content = "今天是星期天，天气晴，今天晚上我要去看电影。"
# content_add = "今天是周天，天气晴朗，我晚上要去看电影。"


# 读文件
def readFile(oriFile, difFile):
    with open(oriFile, "r", encoding="utf-8") as f:
        content = f.read()
    with open(difFile, "r", encoding="utf-8") as f:
        content_dif = f.read()
        # 去掉无效字符
    content = re.sub(r'[^\w\s]|\s+', '', content)
    content_dif = re.sub(r'[^\w\s]|\s+', '', content_dif)
    return content, content_dif

# 写文件
def outputFile(dist,output_file):
    with open(output_file,"w",encoding="utf-8")as f:
        f.write(f"{dist:.2f}")

# 分词
def process(content, content_dif):
    cut_words = jieba.cut(content, cut_all=False)
    cut_words_dif = jieba.cut(content_dif, cut_all=False)
    seg_list = "/".join(cut_words).split("/")
    seg_list_dif = "/".join(cut_words_dif).split("/")
    return seg_list, seg_list_dif


# 计算余弦相似度
def cosine_similarity(seg_list, seg_list_dif):
    keywords = list(set(seg_list + seg_list_dif))
    # 向量化
    word_vector1 = np.zeros(len(keywords))
    word_vector2 = np.zeros(len(keywords))

    for i in range(len(keywords)):
        # 遍历keywords中每个词在句子中的出现次数
        for j in range(len(seg_list)):
            if keywords[i] == seg_list[j]:
                word_vector1[i] += 1
        for k in range(len(seg_list_dif)):
            if keywords[i] == seg_list_dif[k]:
                word_vector2[i] += 1
    # 求值
    dist = float(np.dot(word_vector1, word_vector2) / (np.linalg.norm(word_vector1) * np.linalg.norm(word_vector2)))
    return dist


if __name__ == "__main__":
    oriFile = sys.argv[1]
    difFile = sys.argv[2]
    outFile = sys.argv[3]
    content, content_dif = readFile(oriFile, difFile)
    # print(content)
    # print(content_dif)
    seg_list, seg_list_dif = process(content, content_dif)
    dist = cosine_similarity(seg_list, seg_list_dif)
    outputFile(dist,outFile)

# print(seg_list)
# print(seg_list_dif)

# print(word_vector1)
# print(word_vector2)


