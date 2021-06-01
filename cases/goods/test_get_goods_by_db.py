import pytest
from api.goods import add_goods, get_goods
from common.connect_mysql import DbConnect, dbinfo



def get_db():
    db = DbConnect(dbinfo, database="apps")

    sql = 'SELECT id, goodscode, goodsstatus from apiapp_goods WHERE goodscode = "sp_test_1111";'
    a = db.select(sql)
    print(a)   # list of dict
    return a[0]


def test_get_goods(session, base_url, delete_by_goodscode):
    delete_by_goodscode(goodscode="sp_test_1111")
    # 1.先添加
    add = add_goods(session, base_url, goodscode="sp_test_1111")
    # 2.查询
    sid = add.json()["data"]["id"]
    r = get_goods(session, base_url, sid)

    # 校验数据库
    assert get_db()["id"] == sid
    assert get_db()["goodscode"] == "sp_test_1111"
    assert get_db()["goodsstatus"] == 1


test_data = [
    ["sp_test_1111", {"goodscode": "sp_test_1111", "goodsstatus": 1}]
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_get_goods_1(session, base_url, delete_by_goodscode, test_input, expected):
    delete_by_goodscode(goodscode=test_input)
    # 1.先添加
    add = add_goods(session,base_url, goodscode=test_input)
    # 2.查询
    sid = add.json()["data"]["id"]
    r = get_goods(session,base_url, sid)

    # 校验数据库
    assert get_db()["id"] == sid
    assert get_db()["goodscode"] == expected["goodscode"]
    assert get_db()["goodsstatus"] == expected["goodsstatus"]