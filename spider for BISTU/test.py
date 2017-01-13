#!/usr/bin/env python
# coding=utf-8

import requests
import re
import os
import sys
from time import sleep
from io import StringIO
from urllib import urlencode
from urllib import quote

reload(sys)  
sys.setdefaultencoding('utf8')


f = open('log.txt', 'w+')

for i in range(225,1000):
	progress = (i - 225.0) / 900.0
	print str(progress) + '%...'
	r = requests.get('http://222.249.130.197/' + 'default' + str(i) + '.aspx')
	f.write(str(i) + ': \n')
	f.write('http://222.249.130.197/' + 'default' + str(i) + '.aspx' + ': \n')
	text = r.content.decode('gb2312')
	f.write(text)
	sleep(5)
	
f.close()