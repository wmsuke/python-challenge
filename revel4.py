#!python
# -*- coding: utf-8 -*-
import urllib
import re

option = "12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
for i in range(400):
    print str(i)+"çsñ⁄"
    f = urllib.urlopen(url+option)
    line = f.read()
    print line
    option = re.sub("[a-z\s]","", line)
    print option




