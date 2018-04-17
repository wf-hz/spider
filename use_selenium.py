#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-16

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close() 