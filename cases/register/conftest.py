import pytest
'''注册接口前置删除注册用户'''


@pytest.fixture()
def delete_user(db):
    '''删除'''
    user = 'test_register'
    sql2 = "DELETE from auth_user WHERE username='%s';" % user
    print("执行sql:%s" % sql2)
    db.execute(sql2)
