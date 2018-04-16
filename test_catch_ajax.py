#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-16

import requests
import json

link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112407862416704612774_1523883580635&limit=10&offset=3&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1523883580641'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(link, headers=headers)
json_string = r.text
json_string = json_string[json_string.find('{'):-2]
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']
for eachone in comment_list:
	massage = eachone['content']
	print(massage)