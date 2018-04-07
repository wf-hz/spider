#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# 纪念一下第一个爬虫代码
# @wufeng 2018-04-07

import requests
from bs4 import BeautifulSoup

def get_movies():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Host':'movie.douban.com'
	}
	movie_list = []
	link = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
	r = requests.get(link,headers=headers,timeout=10)
	soup = BeautifulSoup(r.text,'html.parser')
	soup_all = soup.find(id="wrapper").find(id="content").find(class_='grid-16-8 clearfix').find(class_='article').find(id="nowplaying").find(class_='mod-bd').find(class_='lists').find_all(class_='list-item')
	x = len(soup_all)
	for i in range(1,x):
		dic1 = soup_all[i]
		dic2 = dic1.attrs
		res = dic2['data-title']
		movie_list.append(res)
	print(movie_list)
get_movies()
