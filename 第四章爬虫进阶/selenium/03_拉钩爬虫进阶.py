import requests
from lxml import etree
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Cookie':'user_trace_token=20190808201401-47790fd5-4176-4e31-983d-251183516409; _ga=GA1.2.1153627082.1565266442; LGUID=20190808201402-02435921-b9d6-11e9-8874-525400f775ce; LG_LOGIN_USER_ID=261c1b75a68423007b36c7320a009aa8df583864e5cf7a89ccd96491e9875085; LG_HAS_LOGIN=1; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.591083831.1567227234; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c7126de481ae-04572a9e127c73-37637c02-1296000-16c7126de491e4%22%2C%22%24device_id%22%3A%2216c7126de481ae-04572a9e127c73-37637c02-1296000-16c7126de491e4%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%7D%7D; _putrc=C043D1A70A9A0DA6123F89F2B170EADC; JSESSIONID=ABAAABAAAGFABEF99FDC084B4DD4212A14A64DF727D5DE3; login=true; unick=%E5%88%98%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=484; gate_login_token=9bab46ab302e5fb100823f970892f091c4d3c025d498b866fd5b5e123e61383f; privacyPolicyPopup=false; WEBTJ-ID=20190831125715-16ce608db5f19c-0678fd78efab6a-38607701-1296000-16ce608db61409; LGSID=20190831164603-c3eb5772-cbcb-11e9-a507-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566197716,1566641864,1567227230,1567241164; SEARCH_ID=3d96eb724a5a42d4b193c6a1d3cf3011; _gat=1; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=03ce6aef5897a4d4dcb12032cc59c1b9; X_HTTP_TOKEN=ce058fc888af4680989442765105c5a77bbd9504f7; LGRID=20190831174949-ac3885c0-cbd4-11e9-a507-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567244989',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.lagou.com',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Accept': 'application / json, text / javascript, * / *; q = 0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh - CN, zh;q = 0.9',
    'Connection': 'keep - alive',
    'Content-Length': '25',
    'Content-Type': 'application / x - www - form - urlencoded;charset = UTF - 8'

}


def page_url_request():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

    data = {
       'first': 'true',
       'pn': 1,
       'kd': 'python'
           }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        result = response.json()
        print(result)
        positions = result['content']['positionResult']['result']   # 从三个层级拿到职位信息   返回的是一个列表
        for postion in positions:
            postionID = postion['positionId']   # 获取职位的id
            position_url = 'https://www.lagou.com/jobs/6348521.html?show= %s' % postionID
            page_position(position_url)
            break
        break


def page_position(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text) # 解析数据
    position_name = html.xpath('//span[@class="name"]/text()')[0]
    print(position_name)


def main():
    page_url_request()


if __name__ == '__main__':
    main()





