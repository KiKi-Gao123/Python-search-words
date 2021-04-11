import requests
r = requests.get("http://www.sogou.com/")
print(r.status_code)
print(r.text)
type(r)
r.headers
