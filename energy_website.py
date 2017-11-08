# coding: utf-8
'''
value="316"大同(股)
value="362"大同板橋廠
value="109"日立家電
value="584"台松
value="214"台灣三星電子
value="9"台灣三洋
value="61"台灣三菱電機
value="32"台灣奇異
value="18"台灣松下
value="351"台灣惠而浦
value="22"台灣樂金
value="299"禾聯碩
value="28"東元電機
value="30"東穎惠而浦
value="456"美第
value="528"茂年興業
value="85"夏寶
value="179"新禾
value="14"新格
value="280"新視代
value="23"歌林
value="486"憶聲
value="200"環球瑞寶
value="29"聲寶
'''
import requests
from bs4 import BeautifulSoup
from bmpdownload import BmpDownload
import urllib.parse
cid2='280'  # 新視代
p0 = '0'
pageno = 1
url = 'http://www.energylabel.org.tw/purchasing/psearch/upt.aspx'
url = url+'?&p0='+p0+'&uid=0&con=1&cid=4&cid2='+cid2+'&year=&month=&day=&key=&cid1=0&pageno='+str(pageno)
print(url)
res = requests.get(url)
bs = BeautifulSoup(res.text,'lxml')
pages = bs.select('.Paging')
spans = pages[0].select('span')
print (spans[1].text)
page_max = int(spans[1].text)
#download = BmpDownload()
f = open(cid2+'energy.csv','w')
for page_num in range(1,page_max+1):
    pageno = page_num
    url = 'http://www.energylabel.org.tw/purchasing/psearch/upt.aspx'
    url = url+'?&p0='+p0+'&uid=0&con=1&cid=4&cid2='+cid2+'&year=&month=&day=&key=&cid1=0&pageno='+str(pageno)
    #print(url)
    res = requests.get(url)
    bs = BeautifulSoup(res.text,'lxml')    
    rows = bs.select('.GridTrORow')
    for row in rows:
        tds = row.select("td")
        #print(tds[0].text+','+tds[2].text+','+tds[3].text+','+tds[4].text)
    gridtds = bs.select('.GridTD')
    for gridtd in gridtds:
        product_url = 'http://www.energylabel.org.tw/purchasing/psearch/'+gridtd.select('a')[0]['href']
        res = requests.get(product_url)
        bs = BeautifulSoup(res.text,'lxml')
        xss = bs.select('.col-xs-6')
        data=''
        for index in range(0,len(xss)):
            data = data+xss[index].text+","
        #print(data)
        f.write(data+'\n')
        btns = bs.find_all('iframe')
        print(btns[0]['src'])
        img_url = btns[0]['src']
        res = requests.get(img_url)
        res.encoding = 'big5'
        bs = BeautifulSoup(res.text,'lxml')
        imgas = bs.select('a')
        for imga in imgas:
            url= 'http://61.219.118.186/energylbapply/'+urllib.parse.quote(imga['href'])
            file = imga['href'].split('/')[-1]
            print(url,file,type(file))
            download.setUrlAndFilename(url,file)
            download.download()
f.close()