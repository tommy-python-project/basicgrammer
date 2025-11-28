"""
规约实际应用案例
1- 数据分析应用
2- 文本处理应用
"""
import functools


# 1- 数据分析应用
def data_analysis_applications():
    """数据分析应用"""
    print("\n=== 数据分析应用 ===")

    # 销售数据分析
    sales_data = [
        {'product': 'A', 'revenue': 1000, 'cost': 600},
        {'product': 'B', 'revenue': 1500, 'cost': 800},
        {'product': 'C', 'revenue': 800, 'cost': 500},
        {'product': 'A', 'revenue': 1200, 'cost': 700},
    ]

    def analyze_sales(acc,sale):
        product = sale['product']
        if product not in acc:
            acc[product] = {'revenue': 0, 'cost': 0, 'count': 0}

        acc[product]['revenue'] += sale['revenue']
        acc[product]['cost'] += sale['cost']
        acc[product]['count'] += 1
        acc[product]['profit'] = acc[product]['revenue'] - acc[product]['cost']
        return acc

    analysis = functools.reduce(analyze_sales, sales_data, {})

    print("销售分析:")
    for product, stats in analysis.items():
        print(f"  产品{product}:")
        print(f"    收入: {stats['revenue']}")
        print(f"    成本: {stats['cost']}")
        print(f"    利润: {stats['profit']}")
        print(f"    交易数: {stats['count']}")

data_analysis_applications()


# 2. 文本处理应用
def text_processing_applications():
    """文本处理应用"""
    print("\n=== 文本处理应用 ===")

    text = "hello world this is a test hello world python"
    words = text.split()

    # 词频统计
    word_freq = functools.reduce(
        lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
        words,
        {}
    )

    print(f"文本: '{text}'")
    print(f"词频: {word_freq}")

    # 找到最长的单词
    longest_word = functools.reduce(
        lambda a, b: a if len(a) > len(b) else b,
        words
    )

    print(f"最长单词: '{longest_word}' (长度: {len(longest_word)})")

text_processing_applications()

