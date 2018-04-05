#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-05

#第一步，获取页面
import requests

link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(link,headers = headers)
print(r.text)

#第二步，提取需要的数据
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(link,headers = headers)
soup = BeautifulSoup(r.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

#第三步，存储数据
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(link,headers = headers)
soup = BeautifulSoup(r.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

with open('title.txt',"a+") as f:
	f.write(title)
	f.close()
