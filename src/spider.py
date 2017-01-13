#!/usr/bin/env python
# coding=utf-8

import requests
import re
import os
from PIL import Image
from io import StringIO
from urllib import urlencode
from urllib import quote


class Spider:
	def __init__(self):
		self.base_url = "http://jwgl.bistu.edu.cn/"
		self.r = requests.post(self.base_url)
		self.special_code = ""
		self.view_state = ""
		self.check_code = ""
		self.id = "2014010919" # add your username here
		self.password = "caijiahao5246"	# add your password here
		self.cookies = self.r.cookies
		self.login_url = ""
		self.query_grade_url = "" 
		self.name = ""
		self.session = requests.Session()

	def get_url(self):
		# example http://jwgl.bistu.edu.cn/(d5njjm552sqn0j45ijyef3jn)/default2.aspx
		if_match = re.search(r'((.*)/)(.*)(/(.*))', self.r.url)
		print self.r.url
		if if_match:
			print "specialCode: " + if_match.group(3)
			self.special_code = if_match.group(3)
		# example <input type="hidden" name="__VIEWSTATE" value="dDwyODE2NTM0OTg7Oz4mM+1DtiCTrt9yiTmdm7ZDjXbNFw==" />
		if_match = re.search(r'((.*)VIEWSTATE" value=")(.*)(" />)', self.r.text)
		if if_match:
			print "ViewState: " + if_match.group(3)
			self.view_state = if_match.group(3)
			print quote(self.view_state)

	def get_pic(self):
		pic_url = self.base_url + self.special_code + "/CheckCode.aspx"
		img = requests.get(pic_url)
		# print img.content
		f = open("data.gif", "wb+")
		# 因为是aspx，直接用正则匹配出整个图片的二进制
		if_match = re.search(r'(((.*)\n)*)(<!DOC)', img.content)
		if if_match:
			# print "---group1: ---" + if_match.group(1)
			# 图片的末尾有两个冗余的字符 是0x0D 0x0A 分别对应\r \n 通过strip函数去掉
			f.write(if_match.group(1).strip())
		f.close()
		image = Image.open("data.gif")
		os.system("eog data.gif")
		# self.check_code = pytesseract.image_to_string(image)
		# print "CheckCode: " + self.check_code
		self.check_code = raw_input("please input the check code: ")

	def send_request(self):
		# example http://jwgl.bistu.edu.cn/(d5njjm552sqn0j45ijyef3jn)/default2.aspx
		self.login_url = self.base_url + self.special_code + "/default2.aspx"
		payload = {"__VIEWSTATE": self.view_state,
				   "txtUserName": self.id,
				   "TextBox2": self.password,
				   "txtSecretCode": self.check_code,
				   "RadioButtonList1": u'学生'.encode('gb2312'),
				   "Button1": "",
				   "lbLanguage": "",
				   "hidPdrs": "",
				   "hidsc": "",}
		headers = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "jwgl.bistu.edu.cn",
			"Origin": "http://jwgl.bistu.edu.cn",
			"Upgrade-Insecure-Requests": "1",
			"Referer": self.login_url,
			"Connection": "keep-alive",
			"Accept-Language": "en-US,en;q=0,8",
			"Accept-Encoding": "gzip, deflate",}
		# r = self.session.post(self.login_url, data=payload, headers=headers)
		r = self.session.post(self.login_url, data = payload, headers = headers)
		print r.content.decode('gb2312')
		print "[Sending Headers]: " + str(headers)
		print "[StatusCode]: " + str(r.status_code)
		print "[Receiving Headers]: " + str(r.headers)
		self.cookies = r.cookies # 提取cookies
		# example <span id="xhxm">蔡嘉豪同学</span></em>
		if_match = re.search('(<span id=\"xhxm\">)(.*)' + u'同学',r.content.decode('gb2312'))
		if if_match:
			print if_match.group(2)
			self.name = if_match.group(2)
	
	def query_grade(self):
		# example http://jwgl.bistu.edu.cn/(cf2nnfrhv3dtqi55fsstlsap)/xscj_gc.aspx?xh=2014010919&xm=%B2%CC%BC%CE%BA%C0&gnmkdm=N121623
		self.query_grade_url = self.base_url + self.special_code + "/xscj_gc.aspx?xh=" + self.id + "&xm=" + quote(self.name.encode('utf-8')) + "&gnmkdm=N121623"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Referer":"http://jwgl.bistu.edu.cn/(cf2nnfrhv3dtqi55fsstlsap)/xs_main.aspx?xh=" + self.id
			}
		r = self.session.get(self.query_grade_url,headers = headers)
		print r.content.decode('gb2312')
	
	def test(self):
		pass
	def getinfo(self):
		self.id = raw_input("please input your username: ")
		self.password = raw_input("please input your password: ")

if __name__ == '__main__':
	instance = Spider()
	instance.get_url()
	instance.get_pic()
	#instance.getinfo()
	instance.send_request()
	#instance.query_grade()
	#instance.test()