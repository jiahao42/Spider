from django.shortcuts import render
import hashlib
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
# -- coding: utf-8 --


def auth(request):
	if request.method == 'GET':
		signature = request.GET.get('signature','')
		timestamp = request.GET.get('timestamp','')
		nonce = request.GET.get('nonce','')
		token = ''
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