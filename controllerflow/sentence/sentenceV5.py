"""
Sentence 类第 5 版：惰性生成器表达式
"""
import re

from controllerflow.sentence.sentenceV2 import SentenceV2
from controllerflow.sentence.sentenceV3 import SentenceV3
from controllerflow.sentence.sentenceV4 import SentenceV4

RE_WORD = re.compile(r'\w+')
class SentenceV5:
    """生成器表达式版本 - 更简洁的实现"""

    def __init__(self,text: str):
        self.text = text

    def __iter__(self):
        """使用生成器表达式"""
        return (match.group() for match in RE_WORD.finditer(self.text))

def compare_implementations():
    """对比不同版本的实现"""

    text = "Python programming is fun and powerful"
    implementations = {
        "V2-经典迭代器": SentenceV2(text),
        "V3-生成器函数": SentenceV3(text),
        "V4-惰性生成器": SentenceV4(text),
        "V5-生成器表达式": SentenceV5(text)
    }

    for name, sentence in implementations.items():
        words = list(sentence)
        print(f"{name}: {words}")
        print(f"  单词数量: {len(words)}")

compare_implementations()