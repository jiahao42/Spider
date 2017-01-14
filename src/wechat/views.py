# coding=utf-8


from django.shortcuts import render
import hashlib
import time
from django.http import JsonResponse
from django.http import HttpResponse
import xml.dom.minidom
from xml.etree.ElementTree import Element, SubElement, tostring
# Create your views here.


def generate_text_reply(request):
	user = ''
	server = '<![CDATA[Caterpillarous]]>'
	type = '<![CDATA[text]]>'
	createtime = ''
	content = ''
	
	# parse
	DOMTree = xml.dom.minidom.parseString(request.body)
	collection = DOMTree.documentElement
	node = collection.getElementsByTagName('FromUserName')[0]
	user = node.childNodes[0].data
	node = collection.getElementsByTagName('CreateTime')[0]
	createtime = node.childNodes[0].data
	node = collection.getElementsByTagName('Content')[0]
	content = node.childNodes[0].data
	
	
	#generate
	replytext = '''<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[%s]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>'''
	result = replytext % (user, 'Caterpillarous', str(int(time.time())), 'text', content)
	
	return result


def auth(request):
	if request.method == 'GET':
		signature = request.GET.get('signature','')
		timestamp = request.GET.get('timestamp','')
		nonce = request.GET.get('nonce','')
		token = 'caterpillarous'
		echostr = request.GET.get('echostr','')

		list = [token,timestamp,nonce]
		list.sort()
		sha1=hashlib.sha1()
		map(sha1.update,list)
		hashcode=sha1.hexdigest()
		
		response = HttpResponse(echostr.encode('utf-8'), content_type='content-type:text')
		
		if hashcode == signature:
			return response
		else:
			return HttpResponse(echostr)
	else:
		response = HttpResponse(generate_text_reply(request), content_type='application/xml; charset=utf-8')
		return response
			













