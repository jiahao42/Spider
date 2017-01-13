#!/usr/bin/env python
# coding=utf-8

from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('root')
lchild = SubElement(root, "lchild")
lchild.text = "I am a lchild"
rchild = SubElement(root, "rchild")
rchild.text = "I am a rchild"

print tostring(root)