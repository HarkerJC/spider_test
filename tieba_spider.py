import  urllib2
def load_page(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
    headers={"User-Agent":user_agent}

    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req)
    html=response.read()
    return  html
def tieba_spider(url,begin_page,end_page):

    for i in range(begin_page,end_page+1):
        pn=(i-1)*50
        html=load_page(url+str(pn))
        file_name=str(i)+".html"
        print("now download the "+str(i)+" page")
        write_file(file_name,html)
def write_file(file_name,text):
    print("storing file "+file_name+ " now")
    with open(file_name,"w") as f:
        f.write(text)
        f.close()
if __name__=="__main__":
    bdurl=raw_input("please input the address:")
    begin_page = int(input("please input begin page:"))
    end_page = int(input("please input end page:"))
    tieba_spider(bdurl, begin_page, end_page)


