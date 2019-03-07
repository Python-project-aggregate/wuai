import urllib.request
import re
url = "https://www.52pojie.cn/forum-2-1.html"
page = urllib.request.urlopen(url).read()
page = page. decode ('gbk')
zz = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'
html =re.findall(zz,page,re.S)
for i in html:
        print(i)
