"""
sentence 实际应用场景1 ： 数据流处理
"""
import re

RE_WORD = re.compile(r'\w+')
class ProcessingSentence:
    """带数据处理的句子迭代器"""

    def __init__(self, text: str,processor=None):
        self.text = text
        self.processor = processor or (lambda x: x)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            word = match.group()
            yield self.processor(word)

def demo_processing():
    text = "Hello WORLD! This is a TEST."

    # 转换为小写
    lower_sentence = ProcessingSentence(text, lambda w: w.lower())
    print("小写处理:", list(lower_sentence))

    # 过滤短单词
    long_words = ProcessingSentence(text, lambda w: w if len(w) > 3 else None)
    print("长单词:", [w for w in long_words if w])

demo_processing()