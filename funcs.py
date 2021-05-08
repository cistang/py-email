#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   funcs.py.py
@Contact :   tc.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/26 2:11 下午   tc      1.0         None
'''

# import lib
# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import requests
import json

SHDistrictNames=['黄浦','长宁','浦东','静安','徐汇','嘉定','杨浦','虹口','金山','青浦','闵行','普陀','奉贤','松江','宝山','崇明']

def getDistrictFromAddress(address_str):
    baiduAK="fFSM2MAeqLpG8gnkvBVheBH2N5UsRMYo"
    address_query=address_str
    url="http://api.map.baidu.com/place/v2/search?query="+address_query+"&region=上海&output=json&ak="+baiduAK
    res = requests.get(url)
    json_data = json.loads(res.text)
    #print(json_data)
    #return json_data['results'][0]['address']
    return json_data['results'][0]['area']
    '''
    for disc in SHDistrictNames:
        if disc in json_data['results'][0]['address']:
            return disc
    return 0
    '''

#print(getDistrictFromAddress("南期昌路"))