#!python
# -*- coding: utf-8 -*-
import re

f = open('revel3.txt', 'r')

for line in f:
    #3大文字１小文字３大文字
    m = re.search('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', line)
    if m != None:
        print m.group(1),
        
f.close()
print
