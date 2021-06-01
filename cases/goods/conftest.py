import pytest


# 工厂化的fixture
@pytest.fixture()
def delete_by_goodscode(db):

    def delete_goods(goodscode):
        '''删除'''
        sql2 = 'DELETE FROM apiapp_goods WHERE goodscode = "%s";' % goodscode
        print(sql2)
        db.execute(sql2)
    return delete_goods
