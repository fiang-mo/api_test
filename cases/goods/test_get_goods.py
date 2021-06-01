import pytest
from api.goods import add_goods, get_goods




def test_get_goods(session, base_url,  delete_by_goodscode):
    delete_by_goodscode(goodscode="sp_test_yoyo")
    # 1.先添加
    add = add_goods(session, base_url, goodscode="sp_test_yoyo")
    # 2.查询
    sid = add.json()["data"]["id"]
    r = get_goods(session, base_url, sid)
    assert r.json()["code"] == 0
    assert r.json()["msg"] == "success!"
    assert r.json()["data"]["id"] == sid


