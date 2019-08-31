from bs4 import BeautifulSoup

html = """
    <ul class="c_feature">
            <li>
                <i class="icon-glyph-fourSquare"></i> <h4 class="c_feature_name">移动互联网,金融</h4>
                <span class="hovertips">领域</span>
            </li>
            <li>
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
"""
ret = BeautifulSoup(html,'lxml')    # 使用lxml解析
print(ret.prettify())   # prettify 是把html的代码展示的好看些







