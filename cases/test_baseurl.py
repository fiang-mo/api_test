import requests

def test_baseurl(base_url):
    print(base_url)
    assert requests.get(base_url).status_code == 200