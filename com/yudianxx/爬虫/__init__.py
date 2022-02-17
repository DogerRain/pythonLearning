import requests
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)

import urllib
import urllib2

values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print(response.read())