import requests
print(requests.__version__)

url = "http://www.google.com"
r = requests.get(url)
print(r.status_code)


url = "https://raw.githubusercontent.com/Jeremy0818/CMPUT404-Lab1/main/script.py"
r = requests.get(url)
print(r.text)