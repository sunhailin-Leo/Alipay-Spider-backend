# -*- coding: UTF-8 -*-
"""
Created on 2017年9月29日
@author: Leo
"""

# 项目库
from conf.mgo import return_mgo


class BillList:
    def __init__(self, page, page_size):
        self.page = page
        self.page_size = page_size

    # 分页查询时调用获取数据
    def get_rows(self):
        # 偏移量
        pos = self.page * self.page_size

        # 获取数据库对象
        db = return_mgo()
        rows = [doc for doc in db.bill_info.find({}, {"_id": 0}).skip(pos).limit(self.page_size)]
        return rows
