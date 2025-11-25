"""
惰性版本的Sentence类
"""
import re
import reprlib

RE_WORD = re.compile(r'\w+')
# Sentence类第4版：惰性生成器
class Sentence:

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


# Sentence类第5版： 惰性生成器表达式
class Sentence:
    def __init__(self, text):
        self.text = text
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'
    