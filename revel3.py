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

#参考
'''
markers = ''.join( [ '0' if c in string.lowercase else '1' for c in t2 ] )
def f( res, t2, markers ):
    n = len(markers.partition('011101110')[0])
    return f( res+t2[n+4], t2[n+9:], markers[n+9:] ) if n != len(markers) else res
print f( '', t2, markers )
'''