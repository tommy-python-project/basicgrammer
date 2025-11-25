"""
重要原则：勿让可迭代对象变成其自己的迭代器
"""
import re

# 错误示范
RE_WORD = re.compile(r'\w+')
class BadSentence:
    """错误设计 --  可迭代对象也是迭代器 """

    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(text)
        self.index = 0 # 错误：在可迭代对象中维护迭代状态

    def __iter__(self):
        return self # 错误：返回自身

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

def demo_bad_sentence():
    bad_sentence = BadSentence("Hello World")

    print("=== 第一次迭代 ===")
    for word in bad_sentence:
        print(word)  # 输出: Hello, world

    print("=== 第二次迭代 ===")
    for word in bad_sentence:
        print(word)  # 没有输出！迭代状态已经耗尽

    # 更明显的问题
    bad_sentence2 = BadSentence("Test sentence")
    iterator1 = iter(bad_sentence2)
    iterator2 = iter(bad_sentence2)

    print(next(iterator1))  # Test
    print(next(iterator2))  # sentence - 共享相同的状态！

demo_bad_sentence()