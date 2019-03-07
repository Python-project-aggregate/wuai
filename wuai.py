import urllib.request
import re
url = "https://www.52pojie.cn/forum-2-1.html"
page =urllib.request.urlopen(url).read()
page = page.decode ('gbk')
#print (page)
#正则表达式
zz =r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'
#匹配所有符合规则的内容到html集合里
html =re.findall(zz,page,re.S)
#print(html)
for i in range(0,20):
    print(html[i])
    i=i+1

'''for line in html:
#html_link = re.findall(zz,line.re.S)
        title = html_link[0]

        print (title)'''

