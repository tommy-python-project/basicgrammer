"""
不区分大小写的映射
"""

class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        if isinstance(key, str):
            key = key.lower()
        super().__setitem__(key,value)

    def __getitem__(self, key):
        if isinstance(key, str):
            key = key.lower()
        return super().__getitem__(key)

    def get(self, key, default=None):
        if isinstance(key, str):
            key = key.lower()
        return super().get(key, default)

# 使用
cid = CaseInsensitiveDict()
cid['Name'] = 'Alice'
print(cid['name'])
print(cid['NAME'])
print(cid.get('NaMe'))