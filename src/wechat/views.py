# coding=utf-8


from django.shortcuts import render
import hashlib
import time
from django.http import JsonResponse
from django.http import HttpResponse
import xml.dom.minidom
from xml.etree.ElementTree import Element, SubElement, tostring
from wechat_sdk import WechatConf
# Create your views here.
conf = WechatConf(
    token='Caterpillarous', 
    appid='your_appid', 
    appsecret='your_appsecret', 
    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='your_encoding_aes_key'  # 如果传入此值则必须保证同时传入 token, appid
)
from wechat_sdk import WechatBasic
wechat = WechatBasic(conf=conf)

def generate_text_reply(request):
	user = ''
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
	elif request.method == 'POST':
		return HttpResponse(process_msg(request))
		#return HttpResponse(generate_text_reply(request), content_type='application/xml; charset=utf-8')
	

def process_msg(request):
	from wechat_sdk.exceptions import ParseError
	try:
		wechat.parse_data(request.body)
	except ParseError:
		print 'Invalid Body Text'
	id = wechat.message.id          # 对应于 XML 中的 MsgId
	target = wechat.message.target  # 对应于 XML 中的 ToUserName
	source = wechat.message.source  # 对应于 XML 中的 FromUserName
	time = wechat.message.time      # 对应于 XML 中的 CreateTime
	type = wechat.message.type      # 对应于 XML 中的 MsgType
	content = wechat.message.content  
	xml = wechat.response_text(content = content)
	return xml










