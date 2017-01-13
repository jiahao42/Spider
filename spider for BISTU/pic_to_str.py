#!/usr/bin/env python
# coding=utf-8

import os
from PIL import Image
import pytesseract


image = Image.open('data.gif')

vcode = pytesseract.image_to_string(image)

print (vcode)