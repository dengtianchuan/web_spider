#!/usr/bin/python3.5
# 2017中国最好大学排名定向爬虫
"""
Created on May 24 2018
"""

import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
#            print(tds[0].contents[0])
#            print('\t')
#            print(tds[1])
#            print('\t')
#            print(tds[3])
            ulist.append([tds[0].contents[0],tds[1].string,tds[3].string])



def printUnivList(ulist,num):
    tplt='{0:^10}\t{1:^12}\t{2:^12}'
    print(tplt.format('排名','学校名称','总分'))#表头的后两个元素的槽的宽度进行调整才对齐
    for i in range(num):
        u=ulist[i]
        print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    #print(uinfo)
    printUnivList(uinfo,80)#打印80个大学

main()
