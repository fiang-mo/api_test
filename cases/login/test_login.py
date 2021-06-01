import pytest
from api.login import login_get_token
from common.read_yaml import yaml_to_python
from config.config import ROOT_PATH
import os


# 读 yaml 文件的数据，测试数据和代码分离
login_data = yaml_to_python(os.path.join(ROOT_PATH, "data", "login_data.yml"))

'''
login_data = [
    [{"username": "test", "password": "123456"}, {"code": 0, "msg": "login success!"}],
    [{"username": "", "password": "123456"}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "test", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}]
]
'''


@pytest.mark.parametrize("test_input, expected", login_data)
def test_login_case(unlogin, base_url, test_input, expected):
    """登录用例"""
    r = login_get_token(unlogin, base_url,
                        username=test_input["username"],
                        password=test_input["password"])

    assert r.json().get("code") == expected.get("code")
    assert r.json().get("msg") == expected.get("msg")


