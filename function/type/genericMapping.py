"""
泛化映射
"""
from collections import defaultdict
from typing import Mapping


# 1. 定义一个“泛化”的函数
# 它接受任何“键为str,值为 int”的只读映射
def print_total_score(scores: Mapping[str,int]) -> None:
    total  = sum(scores.values())
    print(f"Total score: {total}")

# 2. 准备不同类型的“映射”
regular_dict: dict[str, int] = {'Alice':100,'Bob':90}
default_dict: defaultdict[str, int] = defaultdict(int,{"Charlie":80})

# 3. 他们都可以被“泛化”的函数接受
print_total_score(regular_dict)
print_total_score(default_dict)

