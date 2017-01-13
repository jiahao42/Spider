#!/usr/bin/env python
# coding=utf-8

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom
root = Element('root')

'''
lchild = SubElement(root, "lchild")
lchild.text = "I am a lchild"
rchild = SubElement(root, "rchild")
rchild.text = "I am a rchild"
child = SubElement(root, "<!CDATA[]>")
'''


user = ''
createtime = ''
content = ''
sample = '<xml><ToUserName><![CDATA[toUser]]></ToUserName><FromUserName><![CDATA[fromUser]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[this is a test]]></Content><MsgId>1234567890123456</MsgId></xml>'
DOMTree = xml.dom.minidom.parseString(sample)
collection = DOMTree.documentElement
nodes = collection.getElementsByTagName('FromUserName')
for node in nodes:
	print str(node.childNodes[0].data)
	if node.hasAttribute("FromUserName"):
		user = node.getAttribute("FromUserName")


server = '<![CDATA[Caterpillarous]]>'
type = '<![CDATA[text]]>'
MsgType = SubElement(root, "MsgType")
MsgType.text = type
FromUserName = SubElement(root, "FromUserName")
FromUserName.text = server


str = tostring(root)
print str
str = str.replace('&lt;','<')
str = str.replace('&gt;','>')
print str