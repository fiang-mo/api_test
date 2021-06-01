import pytest
from api.goods import add_goods
from common.read_yaml import yaml_to_python
from config.config import ROOT_PATH
import os

# 读 yaml 文件的数据，测试数据和代码分离
add_goods_data = yaml_to_python(os.path.join(ROOT_PATH, "data", "add_goods.yml"))


'''
add_goods_data = [
    [{"goodscode": "sp_10086_test"}, {"code": 0, "msg": "success!"}],
    [{"goodscode": ""}, {"code": 2000, "msg": "缺少必填项goodscode","data":{}}],
    [{"goodscode": "113"}, {"code": 3003, "msg": "参数不合法", "data":{"goodscode":["请确保这个字段至少包含 8 个字符。"]}}],
    [{"goodscode": "sp_15_11112222_test_122"}, {"code":3003,"msg":"参数不合法","data":{"goodscode":["请确保这个字段不能超过 15 个字符。"]}}],
    [{"goodscode": "sp_10086_test", "goodsname": ""}, {"code":3003,"msg":"参数不合法","data":{"goodsname":["该字段不能为空。"]}}],
    [{"goodscode": "sp_10086_test", "goodsname": "《python自动化》"}, {"code": 0, "msg": "success!"}],
    [{"goodscode": "sp_10086_test", "goodsname": "《python自动化》aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}, {"code":3003,"msg":"参数不合法","data":{"goodsname":["请确保这个字段不能超过 30 个字符。"]}}],
    [{"goodscode": "sp_10086_test", "stock": "aa"}, {"code":3003,"msg":"参数不合法","data":{"stock":["请填写合法的整数值。"]}}],
    [{"goodscode": "sp_10086_test", "stock": -1}, {"code":3003,"msg":"参数不合法","data":{"stock":["请填写合法的整数值。"]}}],
    [{"goodscode": "sp_10086_test", "stock": 1000},{"code": 0, "msg": "success!"}],
    [{"goodscode": "sp_10086_test", "goodsstatus": 0},{"code": 0, "msg": "success!"}],
    [{"goodscode": "sp_10086_test", "goodsstatus": 1},{"code": 0, "msg": "success!"}],
    [{"goodscode": "sp_10086_test", "goodsstatus": 2},{"code":3003,"msg":"参数不合法","data":{"goodsstatus":["“2” 不是合法选项。"]}}],
]
'''

@pytest.mark.parametrize("test_input, expected", add_goods_data)
def test_add_goods_1(session, base_url,  delete_by_goodscode, test_input, expected):
    '''针对goodscode写用例'''
    # 添加商品 goodscode
    delete_by_goodscode(goodscode="sp_10086_test")
    r = add_goods(session,base_url, **test_input)
    assert r.json()["code"] == expected.get("code")
    assert r.json()["msg"] == expected.get("msg")
    # 如果期望结果有data，就断言data
    if expected.get("data"):
        assert r.json()["data"] == expected.get("data")


@pytest.mark.parametrize("test_input, expected", add_goods_data[:1])
def test_add_goods_2(session, base_url, delete_by_goodscode, test_input, expected):
    '''不能重复增加'''
    # 添加商品 goodscode
    delete_by_goodscode(goodscode="sp_10086_test")
    r = add_goods(session,base_url, **test_input)
    assert r.json()["code"] == expected.get("code")
    assert r.json()["msg"] == expected.get("msg")

    # 再添加一次
    r2 = add_goods(session,base_url, **test_input)
    assert r2.json()["code"] == 4000
    assert r2.json()["msg"] == "goodscode不能重复添加"