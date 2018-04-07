#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-07

import requests
import time
from bs4 import BeautifulSoup

def get_all_movie():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Host':'movie.douban.com'
	}
	city_list = []
	movies = {}
	# #从杭州地区页面获取city字典
	link1 = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
	result1 = requests.get(link1,headers=headers,timeout=10)
	soup1 = BeautifulSoup(result1.text,'html.parser') #html字符串创建BeautifulSoup对象
	soup1_tag = soup1.find(id='wrapper').find(id='content').find(class_='grid-16-8 clearfix').find(class_='article').find(id='hd').find(id='location').find(id='cities-list').find(class_='cities-list-bd').find_all(class_='cities-list-item')
	#循环取出city_list
	n = len(soup1_tag)
	for i in range(0,n):
		dic = soup1_tag[i].find_all(class_='city-item')
		x = len(dic)
		for i in range(0,x):
			dic1 = dic[i].attrs
			res = dic1['uid']
			city_list.append(res)

	for city in city_list:
		movie = []
		key = city
		link2 = 'https://movie.douban.com/cinema/nowplaying/' + str(key) + '/'
		r = requests.get(link2,headers=headers,timeout=10)
		soup = BeautifulSoup(r.text,'html.parser')
		soup2 = soup.find(id="wrapper").find(id="content").find(class_='grid-16-8 clearfix').find(class_='article').find(id="nowplaying").find(class_='mod-bd').find(class_='lists').find_all(class_='list-item')
		x = len(soup2)
		for i in range(0,x):
			dic = soup2[i].attrs
			res = dic['data-title']
			movie.append(res)
		value = movie
		movies[key] = value
		print("=====正在爬取数据=====")
		time.sleep(0.1)
	print(city_list)
	print(movies)
get_all_movie()