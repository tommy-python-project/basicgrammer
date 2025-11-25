"""
Sentence 类第 2 版：经典迭代器
"""
import re
from typing import List

RE_WORD = re.compile(r'\w+')

class SentenceV2:
    """经典迭代器版本 - 实现完整的迭代器协议"""

    def __init__(self, text:str):
        self.text = text
        self.words = RE_WORD.findall(text)
        self._index = 0  # 当前迭代位置

    def __iter__(self):
        """返回迭代器对象"""
        return SentenceIterator(self.words)

class SentenceIterator:
    """专门的迭代器类"""

    def __init__(self, words: List[str]):
        self.words = words
        self._index = 0

    def __next__(self):
        """返回下一个单词"""
        try:
            word = self.words[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return word

    def __iter__(self):
        """迭代器本身也是可迭代的"""
        return self

# 使用示例
def demo_sentence_v2():
    text = "The quick brown fox jumps over the lazy dog"
    sentence = SentenceV2(text)

    print("=== 手动迭代 ===")
    iterator = iter(sentence)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass

    print("=== for循环迭代 ===")
    for word in sentence:
        print(word)

    print("=== 多次迭代测试 ===")
    # 可以多次迭代，因为每次 __iter__ 都返回新的迭代器
    for word in sentence:
        print(f"第一次: {word}")

    for word in sentence:
        print(f"第二次: {word}")

demo_sentence_v2()