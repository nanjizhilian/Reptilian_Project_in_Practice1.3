from selenium import webdriver


# 设置代理的目录就是为了不让浏览器知道自己的ip

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server-http://125.110.74.111:9000")      # 设置代理

driver = webdriver.Chrome(chrome_options=options)   # 给浏览器携带一个代理
driver.get("http://www.httpbin.org/")

















