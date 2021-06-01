import pytest
from api.register import register_user
from common.read_yaml import yaml_to_python
from config.config import ROOT_PATH
import os

# 读 yaml 文件的数据，测试数据和代码分离
register_data = yaml_to_python(os.path.join(ROOT_PATH, "data", "register_data.yml"))


'''
register_data = [
    [{"username": "test_register", "password": "123456", "email": ""}, {"code": 0, "msg": "register success!", "data": {}}],
    [{"username": "", "password": "123456", "email": ""}, {"code": 3003, "msg": "参数不合法", "data": {"username": ["该字段不能为空。"]}}],
    [{"username": "te", "password": "123456", "email": ""}, {"code": 3003, "msg": "参数不合法", "data": {"username": ["请确保这个字段至少包含 3 个字符。"]}}],
    [{"username": "test_123_4567891112222222222222333333333", "password": "123456", "email": ""}, {"code": 3003, "msg": "参数不合法","data":{"username":["请确保这个字段不能超过 30 个字符。"]}}],
    [{"username": "test_register", "password": "", "email": ""}, {"code": 3003, "msg": "参数不合法","data":{"password":["该字段不能为空。"]}}],
    [{"username": "test_register", "password": "12345", "email": ""}, {"code": 3003, "msg": "参数不合法","data":{"password":["请确保这个字段至少包含 6 个字符。"]}}],
    [{"username": "test_register", "password": "1234567890123564tests12233456", "email": ""}, {"code": 3003, "msg": "参数不合法","data":{"password":["请确保这个字段不能超过 16 个字符。"]}}],
    [{"username": "test_register", "password": "123456", "email": "122"}, {"code": 3003, "msg": "参数不合法","data":{"email":["请输入合法的邮件地址。"]}}],
    [{"username": "test_register", "password": "123456", "email": "abcddd.com"}, {"code": 3003, "msg": "参数不合法","data":{"email":["请输入合法的邮件地址。"]}}],
    [{"username": "test_register", "password": "123456", "email": "test123@qq.com"}, {"code": 0, "msg": "register success!", "data": {}}]
]
'''


@pytest.mark.parametrize("test_input, expected", register_data)
def test_register_case(unlogin, base_url,delete_user, test_input, expected):
    """注册用例"""
    r = register_user(unlogin,base_url,
                      username=test_input.get("username"),
                      password=test_input.get("password"),
                      email=test_input.get("email"))

    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]


@pytest.mark.parametrize("test_input, expected", register_data[:1])
def test_register_case_2(unlogin, base_url, delete_user, test_input, expected):
    """重复注册用例,用到上面第一条数据"""
    r = register_user(unlogin, base_url,
                      username=test_input.get("username"),
                      password=test_input.get("password"),
                      email=test_input.get("email"))

    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]

    # 重复注册
    r = register_user(unlogin,base_url,
                      username=test_input.get("username"),
                      password=test_input.get("password"),
                      email=test_input.get("email"))
    # 断言
    assert r.json()["code"] == 2000
    assert "用户已被注册" in r.json()['msg']