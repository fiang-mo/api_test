import os

# 当前文件路径
CUR_PATH = os.path.realpath(__file__)
# print(CUR_PATH)

# 项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CUR_PATH))
# print(ROOT_PATH)

# 配置读取数据库
dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}
