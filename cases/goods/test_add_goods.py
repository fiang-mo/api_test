import pytest
'''这里只是调试下，看代码能不能正常运行'''


def test_add_goods_1(session, base_url, delete_by_goodscode):
    """针对goodscode写用例"""
    # 添加商品 goodscode
    delete_by_goodscode(goodscode="sp_test_yoyo")

    url = base_url+"/api/v2/goods"
    body = {
        "goodsname": "yoyo",
        "goodscode": "sp_test_yoyo",
        "merchantid": "10001",
        "merchantname": "悠悠学堂"
    }
    r = session.post(url, json=body)
    print(r.text)
    assert r.json()["code"] == 0
    assert r.json()["msg"] == "success!"

