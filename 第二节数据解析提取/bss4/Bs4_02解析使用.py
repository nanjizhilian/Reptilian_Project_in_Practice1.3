from bs4 import BeautifulSoup

html = """
     <ul class="c_feature">
            <li>
                <i class="icon-glyph-fourSquare"></i> <h4 class="c_feature_name">移动互联网,金融</h4>
                <span class="hovertips">领域</span>
            </li>
            <li span='text'>
                <i class="icon-glyph-trend"></i> <h4 class="c_feature_name">B轮</h4>
                <span class="hovertips">发展阶段</span>
            </li>
                        <li>
                <i class="icon-glyph-figure"></i> <h4 class="c_feature_name">500-2000人</h4>
                <span class="hovertips">规模</span>
            </li>
            <li>
                <i class="icon-glyph-home"></i>
                                <a href="http://www.oriente.com" target="_blank" title="http://www.oriente.com" rel="nofollow"><h4 class="c_feature_name">www.oriente.com</h4></a>
                <span class="hovertips">公司主页</span>
                            </li>
        </ul>
        <tr>
           <td class="text" id=text>王哈哈哈<td/>  
           <td class="name" id='1'>asdkj<td/>  
           <td><td/>  
           <td><td/>  
           <td><td/>  
        <tr/>
"""

soup = BeautifulSoup(html,'lxml')

# 获取所有的li标签
# li = soup.find_all('li')    # find_all是获取所有的，括号里的是所有的li标签
# for ts in li:
#     print(ts)
#     print('='*30)
#


# soup = BeautifulSoup(html,'lxml')
# # 获取第二个li标签
# li = soup.find_all('li',limit=2)[1] # limit是只获取2个，bs4下标是0开始，所以第二个标签是1，返回一个列表        注意：lxml下标是从1个开始
# print(li)



# 获取所有class等于icon-glyph-home属性的i标签
# li = soup.find_all('i',class_='icon-glyph-home')    # class是python内置的方法，为了区分后面加上一个_
# for i in li:
#     print(li)



# 将id等于text并且class等于text的td标签提取出来
# alist = soup.find_all('td',id='text',class_='text')
# for i in alist:
#     print(i)




# 获取所有i标签是class属性
# spanf = soup.find_all('i')
# for a in spanf:
#     #  2种方式
      # 1。通过下标方式获取
      # print(a['class'])

#     # 2,sttrs获取方式
#     spans = a.attrs['class']
#     print(spans)




# 获取所有职位信息，（纯文本）

li = soup.find_all('li')[0:]    # 从0获取到最后
for i in li:
    td = i.find_all('h4')
    title = td[0].string
    print(title)






