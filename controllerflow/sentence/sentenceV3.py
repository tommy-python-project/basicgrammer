"""
Sentence 类第 3 版：生成器函数
"""
import re

RE_WORD = re.compile(r'\w+')
class SentenceV3:
    """生成器函数版本 - 使用 yield 简化实现"""

    def __init__(self,text: str):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        """生成器函数自动创建迭代器"""
        for word in self.words:
            yield word
        # 函数结束自动抛出 StopIteration

def demo_sentence_v3():
    sentence = SentenceV3("Python generators are awesome!")

    print("=== 生成器版本 ===")
    for word in sentence:
        print(word)

    # 检查迭代器类型
    iterator = iter(sentence)
    print(f"迭代器类型: {type(iterator)}")  # <class 'generator'>

    # 支持多次迭代
    words1 = list(sentence)
    words2 = list(sentence)
    print(f"第一次迭代: {words1}")
    print(f"第二次迭代: {words2}")
    print(f"两次迭代结果相同: {words1 == words2}")
    print("===============")

# demo_sentence_v3()


# 生成器工作原理
def generator_mechanics_demo():
    def simple_generator():
        print("开始执行生成器")
        yield "第一个值"
        print("继续执行")
        yield "第二个值"
        print("生成器结束")

    gen = simple_generator()  # 创建生成器对象，但尚未执行
    print("生成器创建完成")

    print("第一次调用 next():")
    result1 = next(gen)  # 执行到第一个 yield
    print(f"得到: {result1}")

    print("第二次调用 next():")
    result2 = next(gen)  # 从上次暂停处继续，执行到第二个 yield
    print(f"得到: {result2}")

    print("第三次调用 next():")
    try:
        result3 = next(gen)  # 执行到函数结束，抛出 StopIteration
    except StopIteration:
        print("生成器已耗尽")


# generator_mechanics_demo()