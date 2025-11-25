"""
生成器
"""
import re
import reprlib


# 传统的类实现迭代器--笨重
class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
            self.index += 1
            return word
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


# 生成器函数 -- 优雅
RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

# 使用示例
s = Sentence('"The time has come," the Walrus said,')
for word in s:
    print(word)
