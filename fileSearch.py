#coding:utf-8

import os
import sys


try:
    dirName = sys.argv[1]
except:
    dirName = os.path.abspath('.')
try:
    fileName = sys.argv[2]
except:
    fileName = r'.'

names = os.listdir(dirName)
for name in names:
    if fileName in name:
        print name
    
