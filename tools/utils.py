# -*- coding: utf-8 -*-  
# @Time : 2024/6/18 上午12:40  
# @Author : dengbanghan  
# @Email : dengbanghan@gmail.com  
# @File : utils.py  
# @Software: PyCharm

import json


def jsonDumps(content):
    '''用于将 Python 对象编码成 JSON 字符串'''
    return json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def jsonLoads(content):
    '''用于解码 JSON 数据。该函数返回 Python 字段的数据类型'''
    return json.loads(content)
