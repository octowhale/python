#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@software: PyCharm Community Edition
@file: python_optget.py
@time: 2016/11/7 15:56
"""

import sys
import os
import getopt


def switch(argvs):
    try:
        opts, args = getopt.getopt(argvs, 'ho:', ['help', 'output='])

        for o, a in opts:
            # @ o for opt
            # @ a for arg
            print ' %s -> %s  ' % (o, a)
            if o in ('-h', '--help'):
                print "����ȫ�����ǰ�����Ϣ"
            if o in ('-o', '--output'):
                print "�µ�����ļ���Ϊ %s" % a
    except getopt.GetoptError, err:
        print err


if __name__ == '__main__':
    argvs = ['-h', '-o', 'filename1', '--help', '--output', 'filename2', 'arg1', 'arg2']
    switch(argvs)
    