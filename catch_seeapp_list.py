#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-17

import requests
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 定义存在最终数据的list，为全局变量
item_info = []

# 登录&获取cookie
def getCookie():
	browser = webdriver.Chrome()
	browser.get("https://portal.xiaodianpu.com/auth.html?#!/entry")
	element = browser.find_element_by_xpath('//*[@id="login-block"]/div/div/div/ul/li[2]/a') #切换登录标签至账号登录
	element.click()

	# 审查username和password 并点击登录
	user = browser.find_element_by_name("username")
	user.send_keys("15088639258")
	password = browser.find_element_by_name("password")
	password.send_keys("youni*****")
	password.send_keys(Keys.RETURN) #点击登陆


# 处理ajax页面
def getItemInfo():
	# 存储filter_class_id下面的5个参数
	key = ['%5B%5D&','%5B%223%22%5D&','%5B%222%22%5D&','%5B%224%22%5D&','%5B%225%22%5D&']
	#定制请求头
	headers = {'Accept':'application/json, text/plain, */*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
	'Connection':'keep-alive',
	'Cookie':'seller_from=100; MANAGER_TOKEN=ZGvhxFxzEKSX6L6p6hzwcmD7urQov%2BuGm6EmzARXcNY5nqbmoooYpaVNTxH5%2BFC4v9YOHF9Z%2FrYZPx7UWjZ52BQ%2F7xZ39wuW3bpTzqXXdATlsEETCkMxd6jgjgTmkF0i; block_with_dd=0; seller_name=Bleu.; seller_privilege=30; seller_email=15088639258; JSESSIONID=node018pcglz2pqcr55aqow5sm6o7u6446.node0',
	'Host':'portal.xiaodianpu.com',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
	}
	x = len(key)
	for x in range(0,x):
		for y in range(1,200):
			url = "https://portal.xiaodianpu.com/api/data_api/materialSelectItemV2?filter_class_id=" + str(key[x])\
			+ "filter_price_end=0&filter_price_start=0&goods_flag=0&keyword=&kol_flag=1&page=" + str(y)\
			+ "&page_size=20&profit_flag=0&select_flag=0&seller_privilege=30&time_flag=0"
			r = requests.get(url,headers=headers)
			data1 = r.json()
			data2 = data1['data']['list_item']
			n = len(data2)
			for n in range(0,n):
				dic = {}
				dic['item_id'] = data2[n]['item_id']
				dic['item_name'] = data2[n]['item_name']
				dic['brand_name'] = data2[n]['brand_name']
				dic['class_id'] = data2[n]['class_id']
				dic['class_name'] = data2[n]['class_name']
				dic['price'] = data2[n]['price']
				dic['ori_price'] = data2[n]['ori_price']
				dic['str_margin'] = data2[n]['str_margin']
				dic['supply_price_end'] = data2[n]['supply_price_end']
				dic['stock'] = data2[n]['stock']
				dic['order_num'] = data2[n]['order_num']
				item_info.append(dic)
		print("取完了第" + str(x+1) + "部分！")

# 将数据写入文件
def saveData():
	localdate = time.strftime("%Y%m%d",time.localtime())
	filename = localdate + "data.txt"
	file = open(filename,'w')
	file.write(str(item_info))
	file.close()
	print("数据写入完毕！")

# main
def main():
	getItemInfo()
	saveData()

if __name__ == '__main__':
	main()