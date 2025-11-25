"""
sentence 实际应用场景1 ： 处理打文件
"""
import re

RE_WORD = re.compile(r'\w+')
class FileSentence:
    """处理大文本文件的句子迭代器"""

    def __init__(self, filename:str):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                for match in RE_WORD.finditer(line):
                    yield match.group()

# 使用示例
def process_large_file():
    # 假设 big_file.txt 是一个很大的文本文件
    file_sentence = FileSentence('big_file.txt')
    word_count = 0
    for word in file_sentence:
        word_count += 1
        if word_count % 10000 == 0:
            print(f"已处理 {word_count} 个单词")

    print(f"总共处理了 {word_count} 个单词")

