#!python
# -*- coding: utf-8 -*-
import urllib
import pickle
peakhell = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for line in peakhell:
    s = ''
    for char in line:
        s += char[0] * char[1]
    print s

