#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-03

# urllib is a package that collects several modules for working with URLs:
# urllib.request for opening and reading URLs (https://github.com/python/cpython/blob/3.6/Lib/urllib/request.py)
# urllib.error containing the exceptions raised by urllib.request
# urllib.parse for parsing URLs
# urllib.robotparser for parsing robots.txt files

# python3中urllib是基于HTTP的高层库
# request 处理客户端的请求
# response 处理服务端的响应
# parse 解析URL

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

# 最简单的
import urllib.request as urlrequest

response = urlrequest.urlopen('http://python.org/')
html = response.read()
print(html)

# 使用Request
import urllib.request

req = urllib.request.Request('http://python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)

# 发送数据
import urllib.parse
import urllib.request 

url = ''
values = {'act':'login','login[email]':'','login[password]':''}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url,data)
req.add_header('Referer','http://www.python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))

# 发送数据和header
import urllib.parse
import urllib.request
url = ''
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'act':'login','login[email]':'','login[password]':''}
headers = { 'User-Agent' : user_agent}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url,data,headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))


