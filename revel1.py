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

K �� M  11 �� 13
O �� Q  15 �� 17
E �� G   5 �� 7   
'''