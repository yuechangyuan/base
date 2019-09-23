#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:22:59 2019

@author: root
"""
from base92 import *
import argparse
parse=argparse.ArgumentParser()
parse.add_argument('-s',type=str,default='D,')
args=parse.parse_args()
def base92_decode(string):
    try:
        decode=base92.decode(string)
        print '[*] base92 is ok -->'
        print decode
    except:
        print 'can not base92'
base92_decode(args.s)
