# coding=utf-8
from django.shortcuts import render
import hashlib
from django.http import HttpResponse
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










