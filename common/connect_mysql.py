import pymysql
from config.config import dbinfo
from nb_log import LogManager
from config.config import ROOT_PATH
import os
logpath = os.path.join(ROOT_PATH, "log")


logger = LogManager("ha").get_logger_and_add_handlers(
    log_filename="momo.log",log_path=logpath
)

'''
pip install PyMySQL==0.9.3
'''

# # 配置数据库相关信息
# dbinfo = {
#     "host": "49.235.92.12",
#     "user": "root",
#     "password": "123456",
#     "port": 3309}


class DbConnect(object):
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        logger.info("读取db配置：%s" % str(self.db_cof))
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        logger.debug("创建游标")

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        logger.info("执行查询SQL：%s" % sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        logger.info("执行查询SQL结果：%s" % str(results))
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        logger.info("执行SQL：%s" % sql)
        try:
           self.cursor.execute(sql)  # 执行SQL语句
           self.db.commit()  # 提交修改
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

if __name__ == '__main__':
    db = DbConnect(dbinfo, database="apps")

    sql = 'SELECT id, goodscode from apiapp_goods WHERE goodscode = "sp_100008";'
    a = db.select(sql)
    print(a)   # list of dict

    sql2 = 'DELETE FROM apiapp_goods WHERE goodscode = "sp_10086";'
    db.execute(sql2)
    db.close()