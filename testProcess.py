import unittest
import jieba

from main import process


class TestTextProcessing(unittest.TestCase):

    def setUp(self):
        self.text1 = "awuz你现在是真的火了平时一定要注意自己的言行举止不要让人以为你是一个多坏的人你不知道有多少眼睛盯着你看着你出错我知道你是个很真性情的人也希望你能保持这份直率但你更要严格要求自己谨言慎行起到艾斯比的表率作用这样才能走的更远你记住鱼越大刺越大刺越大肉越少肉越少刺越小刺越小鱼越小所以鱼越大鱼越小"
        self.text2 = "awuz你现在语是真的火了平时一定要注意自己囖的言行举止不要让人以为你是一个玉玉多坏的人你不知道即可有多少眼睛盯着你看着你出错我知道你是记得个很真性情的人也希望你能保持这特尔份直率但你更要严惹格要求自己谨言的慎行起到艾斯比的表率哦婆婆作用这样才能走的打更远你记住鱼越大刺越大刺越大肉越少肉越少刺越小刺越我小鱼越小所以鱼越大鱼越小"
        self.expected_output1 = list(jieba.cut(self.text1, cut_all=False))
        self.expected_output2 = list(jieba.cut(self.text2, cut_all=False))
        print(self.expected_output1)
        print(self.expected_output2)


    def test_process(self,):
        # 调用 process 函数
        seg_list_p, seg_list_dif_p = process(self.text1, self.text2)
        # 断言结果是否符合预期
        self.assertEqual(seg_list_p, self.expected_output1)
        self.assertEqual(seg_list_dif_p, self.expected_output2)


if __name__ == '__main__':
    unittest.main()
