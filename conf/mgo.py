# -*- coding: UTF-8 -*-
"""
Created on 2017年9月26日
@author: Leo
"""

# 系统库
import json

# 第三方库
from pymongo import MongoClient


# 返回一个数据库对象
def return_mgo():
    # 数据库基本配置
    mgo_conf = json.load(open("./conf/mgo.conf"))

    client = MongoClient(host=mgo_conf['address'], port=mgo_conf['port'])

    # 数据库名
    db = client[mgo_conf['database']]
    return db
