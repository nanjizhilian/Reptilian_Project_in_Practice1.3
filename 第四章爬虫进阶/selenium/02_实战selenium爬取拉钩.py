import requests
from lxml import etree


def request_list_url():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
        'Cookie':'user_trace_token=20190808201401-47790fd5-4176-4e31-983d-251183516409; _ga=GA1.2.1153627082.15652664'
                 '42; LGUID=20190808201402-02435921-b9d6-11e9-8874-525400f775ce; LG_LOGIN_USER_ID=261c1b75a6842300'
                 '7b36c7320a009aa8df583864e5cf7a89ccd96491e9875085; LG_HAS_LOGIN=1; index_location_city=%E4%B8%8A%'
                 'E6%B5%B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566106024,1566197716,1566641864,1567227230; LGSID='
                 '20190831125349-52a394cd-cbab-11e9-a507-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.'
                 'baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c0'
                 '0fZNKw_0pEIb0FNkUsKpOy-I00000Zc2r7C00000T-4jYm.THd_myIEIfK85yF9pywd0ZnqrHTYPHFhujmsnj03ujc1n0Kd5H6k'
                 'nR7KrjckfWbkfWNKnYnkf1wKn1DdwbDkfWNDP1Dk0ADqI1YhUyPGujY1nWTYPjTzrH03FMKzUvwGujYkP6K-5y9YIZK1rBtEILILQ'
                 'hk9uvqdQhPEUiq_my4bpy4MQgK9uvRETAnETvN9ThPCQh9YUysOIgwVgLPEIgFWuHdVgvPhgvPsI7qBmy-bINqsmvFY0APzm1Ykr'
                 'jDkn0%26tpl%3Dtpl_11534_19968_16032%26l%3D1513622130%26attach%3Dlocation%253D%2526linkName%253D%252'
                 '5E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%2525'
                 '87%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%'
                 '253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%2525'
                 ''
                 '80%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5'
                 '%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2'
                 '525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3274472908_canvas%252522%29%25252FDIV%25255B1'
                 '%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1'
                 '%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D177%26ie%3'
                 'DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3Dlagou%26oq%3Dlagou%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.'
                 'lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; _gid=GA1.2.591083831'
                 '.1567227234; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c7126de481ae-04572a9e127c73-37637c'
                 '02-1296000-16c7126de491e4%22%2C%22%24device_id%22%3A%2216c7126de481ae-04572a9e127c73-37637c02-129600'
                 '0-16c7126de491e4%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%7D%7D; _'
                 'putrc=C043D1A70A9A0DA6123F89F2B170EADC; JSESSIONID=ABAAABAAAGFABEF99FDC084B4DD4212A14A64DF727D5DE3; l'
                 'ogin=true; unick=%E5%88%98%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublis'
                 'h=1; hasDeliver=484; gate_login_token=9bab46ab302e5fb100823f970892f091c4d3c025d498b866fd5b5e123e61383f'
                 '; privacyPolicyPopup=false; WEBTJ-ID=20190831125715-16ce608db5f19c-0678fd78efab6a-38607701-1296000-16c'
                 'e608db61409; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=ce058fc888af4680095822765105c5a77bbd9504f7; Hm_'
                 'lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567228590; _gat=1; LGRID=20190831131630-7da607fd-cbae-11e9-8de'
                 '9-525400f775ce; SEARCH_ID=f47d906e32284a7e8cfc556305c5a262',
        'X-Anit-Forge-Code': 0,
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        print(response.json())


def main():
    request_list_url()


if __name__ == '__main__':
    main()



