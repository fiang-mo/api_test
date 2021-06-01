import requests


def add_goods(session,base_url, goodscode="sp_111", goodsname="商品_test", **kwargs):
    """添加商品"""
    # 添加商品 goodscode
    url = base_url+"/api/v2/goods"
    body = {
        "goodsname": goodsname,
        "goodscode": goodscode
    }
    body.update(**kwargs)  # 更新关键字参数
    r = session.post(url, json=body)
    print("添加商品返回:%s" % r.text)
    return r

def get_goods(session,base_url, goodsid):
    """查询商品"""
    url = base_url+"/api/v2/goods/%s"%goodsid
    r = session.get(url)
    print("查询结果：%s" % r.text)
    return r

def delete_goods(session, goodsid):
    """删除商品"""
    pass

def update_goods(session, goodsid):
    """修改商品"""
    pass

def get_all_goods(session, goodsid):
    """全部商品"""
    pass


if __name__ == '__main__':
   s = requests.session()
   from api.login import login_get_token
   base_url = "http://49.235.92.12:7005"
   login_get_token(s,base_url)
   add = add_goods(s,base_url, goodscode="sp_10068934")
   sid = add.json()["data"]["id"]
   get_goods(s,base_url, sid)


