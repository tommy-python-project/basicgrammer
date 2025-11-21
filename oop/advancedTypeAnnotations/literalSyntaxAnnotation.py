"""
字面量类型注解进阶
"""
from http import HTTPMethod
from typing import Literal

HttpMethod = Literal["GET", "POST", "PUT", "DELETE"]
Status = Literal[200, 404, 500]

def make_request(
    method: HTTPMethod,
    url: str,
    expected_status: Status = 200,
) -> bool:
    print(f"Making {method} request to {url}, expecting {expected_status}")
    return True

# 使用示例
make_request("GET", "/api/data")  # 合法
make_request("POST", "/api/data", 200)  # 合法
# make_request("PATCH", "/api/data")  # 类型错误！