#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-07

import requests
from bs4 import BeautifulSoup
import re
import os

class mm_pic():
	def all_url(self,url):
		html = self.request(url)
		all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a',href=re.compile('[0~9]'))
		for a in all_a:
			title = a.get_text()
			print('>>>>开始保存：',title)
			path = str(title).replace("?","_").replace(":"," ")
			self.mkdir(path)
			href = a['href']
			self.html(href)

	def html(self,href):  ##获得图片的页面地址
		html = self.request(href)
		max_span = BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
		for page in range(1,int(max_span)+1):
			page_url = href + '/' + str(page)
			self.img(page_url)   ##调用img函数

	def img(self,page_url):  ##处理图片页面地址获得图片的实际地址
		img_html = self.request(page_url)
		img_url = BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
		self.save(img_url)

	def save(self,img_url):  ##保存图片
		name = img_url[-9:-4]
		img = self.request(img_url)
		f = open(name + '.jpg','ab')
		f.write(img.content)
		f.close()

	def mkdir(self,path):   ##创建文件夹
		path = path.strip()
		isExists = os.path.exists(os.path.join("E:\mm_pic",path))
		if not isExists:
			print("建了一个名字叫做",path,"的文件夹")
			os.makedirs(os.path.join("E:\mm_pic",path))
			os.chdir(os.path.join("E:\mm_pic",path))
			return True
		else:
			print("文件夹已经存在")
			return False

	def request(self,url):   ##这个函数获取网页的response 然后返回
		headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'Referer':'http://www.mzitu.com/100260/2'
		}
		content = requests.get(url,headers=headers)
		return content

def main():
	Mzitu = mm_pic()  ##实例化
	Mzitu.all_url('http://www.mzitu.com/all')  ##给函数all_url传入参数

main()