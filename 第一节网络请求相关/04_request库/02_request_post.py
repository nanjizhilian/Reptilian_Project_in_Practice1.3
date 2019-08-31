import requests

url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',
}

response = requests.post(url,headers=headers,data=data)
print(response.json())






