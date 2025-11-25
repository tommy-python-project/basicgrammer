"""
惰性生成器版本 - 按需生成单词，节省内存
"""
import re

from controllerflow.sentence.sentenceV3 import SentenceV3

RE_WORD = re.compile(r'\w+')
class SentenceV4:
    """惰性生成器版本 - 按需生成单词，节省内存"""

    def __init__(self,text:str):
        self.text = text  #只存储原始文本

    def __iter__(self):
        """惰性生成单词"""
        for match in RE_WORD.finditer(self.text): # finditer 返回迭代器
            yield match.group()

def demo_sentence_v4():
    # 模拟大文本
    large_text= "word " * 1000000

    print("=== 内存使用对比 ===")
    import sys

    # V3 版本（预先计算）
    sentence_v3 = SentenceV3(large_text)
    print(f"SentenceV3 内存: {sys.getsizeof(sentence_v3.words)} bytes")

    # V4 版本（惰性计算）
    sentence_v4 = SentenceV4(large_text)
    print(f"SentenceV4 内存: {sys.getsizeof(sentence_v4.text)} bytes")

    # 使用示例
    print("=== 惰性迭代 ===")
    sentence = SentenceV4("The lazy dog sleeps all day")
    for i, word in enumerate(sentence):
        if i < 3:  # 只取前3个单词
            print(word)
        else:
            break

demo_sentence_v4()
