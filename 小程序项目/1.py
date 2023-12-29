import json

# 示例JSON数据
json_data = '''
{
    "code": 200,
    "data": {
        "source_lang": "en",
        "target_lang": "zh-CN",
        "translate_result": "你好"
    },
    "processTime": "230.26ms",
    "url": "https://findmyip.net/",
    "time": "2023-12-29 17:05:23"
}
'''

# 将JSON解析为字典
my_dict = json.loads(json_data)

# 打印原始字典
print("原始字典:", my_dict)

# 动态更新序号
new_key = "new_key"
new_value = {"sub_key": "sub_value"}

# 添加新的键值对
my_dict[new_key] = new_value

# 打印更新后的字典
print("更新后的字典:", my_dict)
