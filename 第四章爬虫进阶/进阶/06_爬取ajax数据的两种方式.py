from selenium import webdriver
import time
from lxml import etree

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
html = etree.HTML(driver.page_source)    # 拿到所有网页源代码
print(html)
time.sleep(2)
driver.close()


