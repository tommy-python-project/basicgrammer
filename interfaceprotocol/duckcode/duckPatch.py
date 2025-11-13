"""
猴子补丁 - 在运行时动态地修改（或添加）模块、类或实例的属性（通常是方法）。
"""

class Cat:

    def moew(self):
        print("喵...")

def monkey_patch_quack(self):
    print(f"{type(self).__name__} 正在呱呱叫！")


cat = Cat()
# cat.quack()  # AttributeError: 'Cat' object has no attribute 'quack'

# 执行猴子补丁
Cat.quack = monkey_patch_quack

cat.quack()  # 输出: Cat 正在呱呱叫！


class FrenchDeck:

    def __init__(self):
        self.ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        self.suits = 'spades diamonds clubs hearts'.split()
        self._cards = [(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# 猴子补丁：在运行时添加方法
def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card

# 现在支持洗牌操作
import random
deck = FrenchDeck()
random.shuffle(deck)  # 需要 __setitem__ 方法