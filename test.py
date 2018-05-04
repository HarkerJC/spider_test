import  urllib2
# response=urllib2.urlopen("http://www.baidu.com")
# html=response.read()
# print(html)

user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
headers={"User-Agent":user_agent}
req=urllib2.Request("http://www.baidu.com",headers=headers)
response=urllib2.urlopen(req)
my_page=response.read()
print(my_page)