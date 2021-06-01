import requests
import pytest
from api.login import login_get_token
from common.connect_mysql import DbConnect, dbinfo


@pytest.fixture(scope="session")
def session(base_url):
    """session直接登陆"""
    s = requests.session()
    login_get_token(s,base_url)
    yield s
    print("yield后面是后置操作")
    s.close()


@pytest.fixture(scope="function")
def unlogin():
    """不需要登陆"""
    s = requests.session()
    yield s
    s.close()


# @pytest.fixture(scope="session")
# def login(session):
#     print("先登录, 自动更新token")
#     login_get_token(session)


@pytest.fixture(scope="session")
def db():
    db = DbConnect(dbinfo, database="apps")
    yield db
    print("关闭数据库连接")
    db.close()