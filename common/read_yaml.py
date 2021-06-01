import yaml
import os
from nb_log import LogManager
from config.config import ROOT_PATH
import os
logpath = os.path.join(ROOT_PATH, "log")


logger = LogManager("ha").get_logger_and_add_handlers(
    log_filename="momo.log",log_path=logpath
)

def yaml_to_python(yaml_path):
    '''yaml转python类型'''
    logger.info("读取yaml文件，转python类型")
    logger.info("读取yaml文件地址：%s" % yaml_path)
    try:
        f = open(yaml_path, "r", encoding="utf-8")
        fp = f.read()
        # print(fp)
        d = yaml.safe_load(fp)
        # print(d)
        f.close()
    except Exception as msg:
        logger.error("读取文件异常：%s" % msg)
        raise IOError("读yaml文件报错")
    return d
if __name__ == '__main__':
    # print(__file__)
    # curpath = os.path.realpath(__file__)
    # print(curpath)
    #
    # root_dir = os.path.dirname(os.path.dirname(curpath))
    # print(root_dir)

    from config.config import ROOT_PATH
    yaml_path = os.path.join(ROOT_PATH, "data", "test_datax.yml")
    print(yaml_path)

    d = yaml_to_python(yaml_path)
    print(d)
