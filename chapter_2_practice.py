#!/usr/bin/python  
# -*- coding: utf-8 -*- 
# @wufeng 2018-04-05

# 第二章python基础试题
# 练习1：使用python循环打印输出从1到100所有奇数
i = 1
while i < 100:
	print(i)
	i = i + 2

for i in range(1,101):
	if i % 2 ==1:
		print(i)

# 练习2：将字符串“你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串”中的符号变成一个空格
#        输出的格式为“你好 我正在学 Python 现在需要 修改字符串”

a = '你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串'
b = a.replace('$$$',' ').replace('@#@#',' ').replace('&*&*&',' ')
print(b)

import re
a = '你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串'
b = re.sub('[$@#&*%]+',' ',a)
print(b)

# 练习3：输出9*9乘法口诀
for i in range(1,10):  #range(x,y)中i的值含x，但是不含y
	for x in range(1,i+1):  #此处如果用range(1,10)的话，会输出9*9的矩阵
		print ("%dx%d=%d\t" %(x,i,x*i),end="")  #我们习惯性在使用口诀的时候，小的数字放前面，故此处应该用 %(x,i,i*x)
	print("")

