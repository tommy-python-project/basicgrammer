"""
itertools.islice - 切片控制
"""
import itertools


def itertools_islice_demo():
    print("=== itertools.islice 切片控制 ===")

    # 创建有限数列
    infinite_seq = itertools.count(0, 5)  # 0, 5, 10, 15, ...
    limited_seq = itertools.islice(infinite_seq, 0,50,10) # 取前50个，每10个取一个

    print("有限数列:")
    print(list(limited_seq))


    # 实际应用： 分页处理
    def paginate_data(total_items,page_size):
        all_data = itertools.count(1) # 模拟无限数据流
        page_num = 0

        while True:
            page = list(itertools.islice(all_data, page_size))
            if not page:
                break
            page_num += 1
            print(f"第{page_num}页: {page}")
            if page_num >= 3:  # 只显示3页
                break

    print("分页演示:")
    paginate_data(100, 5)

itertools_islice_demo()