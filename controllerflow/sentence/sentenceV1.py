"""
sentence 类第1版： 基础实现（假设）
"""
import re
from typing import List

RE_WORD = re.compile(r'\w+')

class SentenceV1:
    """基础版本 -- 预先计算所有单词 """
    def __init__(self,text: str):
        self.text = text
        self.words : List[str] = RE_WORD.findall(text) # 立即计算所有单词

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    