import requests


def login_get_token(s, base_url, username="test", password="123456"):
    '''登录获取token'''
    url = base_url+"/api/v1/login"
    print(url)

    body = {
         "username": username,
         "password": password
    }
    r = s.post(url, json=body)
    print("接口返回：%s" % r.text)

    # 更新session会话的头部
    h = {
        "Authorization": "Token "+r.json()["token"]
    }
    s.headers.update(h)

    # 返回response对象
    return r

if __name__ == '__main__':
    s = requests.Session()
    base_url = "http://49.235.92.12:7005"
    r = login_get_token(s, base_url, "test1")
    code = r.json()["code"]
    token = r.json()["token"]
    print(token)
