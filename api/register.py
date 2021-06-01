import requests


def register_user(s,base_url,
                  username="test_register1",
                  password="123456",
                  email=""):
    """注册用户"""
    url = base_url+"/api/v1/register"
    body = {"username": username,
            "password": password,
            "email": email}
    r = s.post(url, json=body)
    print("注册接口返回：%s" % r.text)
    return r

if __name__ == '__main__':
    import requests
    s = requests.session()
    base_url="http://49.235.92.12:7005"
    register_user(s,base_url)
