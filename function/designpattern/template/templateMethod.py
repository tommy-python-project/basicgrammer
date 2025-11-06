"""
模版方法
用函数实现模版方法
"""

def data_processing_template(data, extract_func, transform_func, load_func):
    """
    数据处理模版
    """

    # 提取阶段
    print("开始提取数据...")
    raw_data = extract_func(data)

    # 转换阶段
    print("开始转换数据...")
    processed_data = transform_func(raw_data)

    # 加载阶段
    print("开始加载数据...")
    result = load_func(processed_data)

    print("数据处理完成")
    return result

# 具体实现函数
def extract_from_csv(file_path):
    print(f"从CSV文件提取: {file_path}")
    return ["data1", "data2", "data3"]

def transform_to_upper(data):
    return [item.upper() for item in data]

def load_to_database(data):
    print(f"加载到数据库: {data}")
    return len(data)

def extract_from_api(api_url):
    print(f"从API提取: {api_url}")
    return ["api_data1", "api_data2"]

def transform_add_prefix(data):
    return [f"PREFIX_{item}" for item in data]


# 使用模板
result1 = data_processing_template(
    "data.csv",
    extract_from_csv,
    transform_to_upper,
    load_to_database
)

result2 = data_processing_template(
    "https://api.example.com/data",
    extract_from_api,
    transform_add_prefix,
    load_to_database
)