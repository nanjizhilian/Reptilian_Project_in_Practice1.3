import lxml
from bs4 import BeautifulSoup
import json

html = """
<div id="header">
    <div class="inner home-inner">
        <div class="logo">
            <a href="https://www.zhipin.com/" ka="header-home-logo" title="BOSS直聘"><span>BOSS直聘</span></a>
        </div>
        <div class="nav">
            <ul>
                <li class=""><a ka="header-home" href="https://www.zhipin.com/">首页</a></li>
                <li class="cur"><a ka="header-job" href="https://www.zhipin.com/job_detail/">职位</a></li>
                <li class=""><a ka="header_brand" href="https://www.zhipin.com/gongsi/">公司</a></li>
                <li class=""><a ka="header-app" href="https://app.zhipin.com/">APP</a></li>
                <li class=""><a ka="header-article" href="https://news.zhipin.com/">资讯</a></li>
            </ul>
        </div>
        <div class="user-nav">
                <ul>
                    <li class=""><a ka="header-message" href="https://www.zhipin.com/web/geek/chat">消息<span class="nav-chat-num"></span></a></li>
                    <li class=""><a ka="header-resume" href="https://www.zhipin.com/web/geek/resume">简历</a></li>
                    <li class="nav-dot">·</li>
                    <li class="nav-up-file"><a class="header-resume-upload" ka="header-resume-upload-2" href="javascript:;">上传</a></li>
                    <li class="nav-figure">
                        <a href="https://www.zhipin.com/web/geek/recommend" ka="header-username">
                            <span class="label-text">刘先生</span><img src="https://img.bosszhipin.com/beijin/mcs/useravatar/20190313/8c9b055cbd22146182fcfcbe7c6ca4b5cfcd208495d565ef66e7dff9f98764da_s.jpg" alt=""/>
                        </a>
                        <div class="dropdown">
                            <a href="https://www.zhipin.com/web/geek/recommend" ka="header-personal">个人中心<span>推荐职位、编辑在线简历</span></a>
                            <a href="https://www.zhipin.com/web/geek/account?type=mobile" ka="account_manage">账号设置<span>修改密码、打招呼语和常用语</span></a>
                            <a href="https://www.zhipin.com/web/geek/account?type=privacySet" ka="privacy_set">隐私设置</a>
                            <a href="https://www.zhipin.com/web/geek/mall" class="link-mall" ka="recruit_assistant">求职助手</a>
                            <a href="javascript:;" class="link-recruit" ka="header-recruit">切换为招聘者</a>
                            <a href="javascript:;" class="link-logout" ka="header-logout">退出登录</a>
                            <p class="recruit-tip"><img src="https://static.zhipin.com/v2/web/geek/images/recruit-tip.gif" alt=""><span>在 APP 端“我的 - 设置”中切换为Boss身份后，刷新本页面即可进行招聘</span></p>
                        </div>
                    </li>
                </ul>
        </div>
    </div>
"""

text = BeautifulSoup(html,'lxml')
# print(text.prettify())

# response = text.find_all('li',limit='')[0]
# print(response)







