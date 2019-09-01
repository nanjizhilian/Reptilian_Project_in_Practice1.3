import re
from selenium import webdriver
from lxml import etree
import time


class LagouSipder(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.Safe = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source    #  page_source是selenium中获取当前页面所有源代码
            self.request_detail_list(source)    #  下面的方法中调用时需要传入一个值，所以闯入了source这个值，source这个值是获取页面源代码的结果，所以在下面的方法中解析这个source
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[@class='pager_next']")
            next_btn.click()
            # if next_btn.get_attribute("class") == "pager_next pager_next_disabled":
            #     pass
            # else:
            #     next_btn.click()
            # time.sleep(2)

    def request_detail_list(self,source):
        html = etree.HTML(source)
        lisnks = html.xpath("//a[@class='position_link']/@href")
        for link in lisnks:
            self.page_url_demo(link)


    def page_url_demo(self,url):
        self.driver.get(url)    # 当第一个网页爬取之后，在次请求到第二个网页中
        self.driver.execute_script('window.open("%s")'%url)
        self.driver.switch_to_window(self.driver.window_handles[1 ])
        source = self.driver.page_source    # 在其他页面继续获取源代码
        self.page_city_page(source)

        self.driver.close() # 关闭当前详情页
        self.driver.switch_to_window(self.driver.window_handles[0]) # 继续切换到职位列表页

    def page_city_page(self,source):
        html = etree.HTML(source)
        title = html.xpath("//div[@class='job-name']/h2[@class='name']/text()")[0]  # 获取 职称信息
        salary = html.xpath("//dd[@class='job_request']//span/text()")[0].strip()  # 获取薪资
        city = html.xpath("//dd[@class='job_request']//span/text()")[1] # 获取地区
        city = re.sub(r"[\/]",'',city).strip()
        experienc = html.xpath("//dd[@class='job_request']//span/text()")[2] # 获取经验
        experienc = re.sub("\/",'',experienc).strip()
        Education = html.xpath("//dd[@class='job_request']//span/text()")[3]    # 获取学历
        Education = re.sub("\/",'',Education).strip()
        Jobinformation = "".join(html.xpath("//div[@class='job_bt']//text()")).strip()
        Corporate_name = html.xpath("//h3[@class='fl']/em[@class='fl-cn']/text()")[0].strip()  # 公司昵称
        positions = {
            'title':title,
            'salary':salary,
            'city':city,
            'experienc':experienc,
            'Education':Education,
            'Jobinformation':Jobinformation,
            'Corporate_name':Corporate_name

        }

        self.Safe.append(positions)
        print(positions)

        print("="*40)


if __name__ == '__main__':
    Sipder = LagouSipder()
    Sipder.run()

