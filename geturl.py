#/usr/bin/env python
# -*- coding:utf-8 -*-
#Author Tianming

import urllib, urllib2, sys

file = sys.argv[1]
headers = {"Content-type": "application/x-www-form-urlencoded",
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Connection": "close",
           "Cache-Control": "no-cache"}
f = open(file,'r')
res = f.readlines()
for val in res:
    try:
        request = urllib2.Request(val, headers=headers)
        res_data = urllib2.urlopen(request)  # 创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据
    except Exception, e:
        result = e
    else:
        result1 = res_data.geturl()
        result2 = res_data.getcode()  # 返回响应的HTTP状态代码
        print ("[*]" + result1 + " --- " + str(result2))

# python geturl.py 1.txt
# 1.txt里面的URL需要一行一行的