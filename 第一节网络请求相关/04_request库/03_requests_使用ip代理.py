import requests

proxy = {
    'http':'120.83.107.86:9999'
}

response = requests.get('http://www.httpbin.org/',proxies=proxy)
print(response.text)





