# -*- coding: UTF-8 -*-
"""
Created on 2017年9月29日
@author: Leo
"""

from flask import Blueprint

# 功能:账单列表分页展示
billList = Blueprint('billList', __name__)

# 加载完蓝图后导入
from . import views
