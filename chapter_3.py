#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-06

# 获取响应内容
import requests
r = requests.get('http://www.santostang.com/')
print("文本编码：",r.encoding)
print("响应状态码：",r.status_code)
print("字符串方式的响应体",r.text)

# 传递URL参数
import requests
key_dict = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=key_dict)
print("URL已经正确编码：",r.url)
print("字符串方式的响应体：\n",r.text)

#定制请求头
import requests
headers = {
'user_agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Host':'music.163.com'
}
r = requests.post('http://music.163.com',headers=headers)
print("响应状态码：",r.status_code)

# 发送post请求
import requests
key_dict = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=key_dict)
print(r.text)
