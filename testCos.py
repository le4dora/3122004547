import unittest
from collections import Counter
import numpy as np
from main import cosine_similarity  # 替换为实际模块路径


class TestCosineSimilarity(unittest.TestCase):

    def test_cosine_similarity(self):
        # 比较
        seg_list_cos1 = ['现在', '言行举止', '一个多', '出错', '知道']
        seg_list_cos2 = ['现在', '一个多', '出错', '知道', '即可']
        # 预期的余弦相似度值
        expected_similarity = 0.8  # 这是一个示例值，根据实际计算结果进行调整
        # 调用余弦相似度函数
        result = cosine_similarity(seg_list_cos1, seg_list_cos2)
        # 断言结果是否符合预期
        self.assertAlmostEqual(result, expected_similarity, places=2)

        # 完全相同的情况
        seg_list_cos3 = seg_list_cos1 = ['现在', '言行举止', '一个多', '出错', '知道']
        expected_similarity = 1.0
        result = cosine_similarity(seg_list_cos1, seg_list_cos3)
        self.assertAlmostEqual(result, expected_similarity, places=2)

        # 完全不同的情况
        seg_list_cos4 = ['类目', '笑嘻嘻']
        expected_similarity = 0.0
        result = cosine_similarity(seg_list_cos1, seg_list_cos4)
        self.assertAlmostEqual(result, expected_similarity, places=2)

        # 空的情况
        seg_list_cos5 = []
        expected_similarity = 0.0
        result = cosine_similarity(seg_list_cos1, seg_list_cos4)
        self.assertAlmostEqual(result, expected_similarity, places=2)



if __name__ == '__main__':
    unittest.main()
