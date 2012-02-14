#!python
# -*- coding: utf-8 -*-
import string
'''
master = """
g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""
'''
master = 'map.html'

dst = master.translate(string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"))

print dst

'''
abcdefghijklmnopqrstu

K Å® M  11 Å® 13
O Å® Q  15 Å® 17
E Å® G   5 Å® 7   
'''