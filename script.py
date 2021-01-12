import requests
print(requests.__version__)

url = "http://www.google.com"
res = requests.get(url)
print(res.status_code)
