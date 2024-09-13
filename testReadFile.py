import unittest
import os
from main import readFile


class TestReadFile(unittest.TestCase):

    def setUp(self):
        # 创建临时文件用于测试
        self.orig_file = 'test_ori.txt'
        self.dif_file = 'test_dif.txt'

        with open(self.orig_file, 'w', encoding='utf-8') as f:
            f.write("awuz你现在是真的火了，平时一定要注意自己的言行举止，不要让人以为你是一个多坏的人，你不知道有多少眼睛盯着你，看着你出错，我知道你是个很真性情的人，也希望你能保持这份直率，但你更要严格要求自己，谨言慎行，起到艾斯比的表率作用，这样才能走的更远。你记住、鱼越大，刺越大；刺越大，肉越少；肉越少，刺越小；刺越小，鱼越小，所以鱼越大，鱼越小。\n")

        with open(self.dif_file, 'w', encoding='utf-8') as f:
            f.write("awuz你现在语是真的火了，平时一定要注意自己囖的言行举止，不要让人以为你是一个玉玉多坏的人，你不知道即可有多少眼睛盯着你，看着你出错，我知道你是记得个很真性情的人，也希望你能保持这特尔份直率，但你更要严惹格要求自己，谨言的慎行，起到艾斯比的表率哦婆婆作用，这样才能走的打更远。你记住、鱼越大，刺越大；刺越大，肉越少；肉越少，刺越小；刺越我小，鱼越小，所以鱼越大，鱼越小。")


    def tearDown(self):
        # 删除测试文件
        os.remove(self.orig_file)
        os.remove(self.dif_file)

    def test_read_file(self):
        content_r, content_r_dif = readFile(self.orig_file, self.dif_file)
        self.assertEqual(content_r, 'awuz你现在是真的火了平时一定要注意自己的言行举止不要让人以为你是一个多坏的人你不知道有多少眼睛盯着你看着你出错我知道你是个很真性情的人也希望你能保持这份直率但你更要严格要求自己谨言慎行起到艾斯比的表率作用这样才能走的更远你记住鱼越大刺越大刺越大肉越少肉越少刺越小刺越小鱼越小所以鱼越大鱼越小')
        self.assertEqual(content_r_dif, "awuz你现在语是真的火了平时一定要注意自己囖的言行举止不要让人以为你是一个玉玉多坏的人你不知道即可有多少眼睛盯着你看着你出错我知道你是记得个很真性情的人也希望你能保持这特尔份直率但你更要严惹格要求自己谨言的慎行起到艾斯比的表率哦婆婆作用这样才能走的打更远你记住鱼越大刺越大刺越大肉越少肉越少刺越小刺越我小鱼越小所以鱼越大鱼越小")

    def test_empty_files(self):
        with open(self.orig_file, 'w', encoding='utf-8') as f:
            f.write("")
        with open(self.dif_file, 'w', encoding='utf-8') as f:
            f.write("")

        content_r, content_r_dif = readFile(self.orig_file, self.dif_file)
        self.assertEqual(content_r, '')
        self.assertEqual(content_r_dif, '')

    def test_special_characters(self):
        with open(self.orig_file, 'w', encoding='utf-8') as f:
            f.write("!@#$%^&*()+_[]{}|;:',.<>/?`~")
        with open(self.dif_file, 'w', encoding='utf-8') as f:
            f.write("`~!@#$%^&*()+_-=<>?/:;,.|[]{}")

        content_r, content_r_dif = readFile(self.orig_file, self.dif_file)

        self.assertEqual(content_r, '')
        self.assertEqual(content_r_dif, '')


if __name__ == '__main__':
    unittest.main()
