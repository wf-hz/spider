#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-17

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree

# 模拟登录过程
browser = webdriver.Chrome()
browser.get("https://portal.xiaodianpu.com/auth.html?#!/entry")
element = browser.find_element_by_xpath('//*[@id="login-block"]/div/div/div/ul/li[2]/a')
element.click() #切换登录标签至账号登录

user = browser.find_element_by_name("username") #审查元素username的name
user.send_keys("15088639258")
password = browser.find_element_by_name("password") #审查元素password的name
password.send_keys("youniyouzan2017")
password.send_keys(Keys.RETURN) #点击登陆
print('1...2...3...登录账号成功！')

# 打开页面获取item_list
x = 1
url = 'https://portal.xiaodianpu.com/fashion/hot-goods-v2?show_btn=0&kol_flag=1&order_id=&class_type=' + str(x) + '&filter_price_start=NaN&filter_price_end=NaN&page=1&keyword='
r = requests.get(url)
c = r.etree.HTML(r.content).xpath('//*[@id="lead_item_0"]/div[2]/a')
print(c)




# for x in range(1,6): #总共5个大类标签
# 	url = 'https://portal.xiaodianpu.com/fashion/hot-goods-v2?show_btn=0&kol_flag=1&order_id=&class_type=' + str(x) + '&filter_price_start=NaN&filter_price_end=NaN&page=1&keyword='
# 	headers = {
# 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
# 	'Host':'portal.xiaodianpu.com'
# 	}
# 	r = requests.get(url,headers=headers,timeout=1)
# 	t = etree.HTML(r.content).xpath('//*[@id="lead_item_0"]/div[2]/a')



