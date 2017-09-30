# -*- coding: UTF-8 -*-
"""
Created on 2017年9月29日
@author: Leo
"""

# 项目库
from . import billList
from .models import BillList as Query_bill

# Flask库
from flask import jsonify, request, make_response


@billList.route('/', methods=['GET'])
def test():
    print("Test /")
    return jsonify({"Test": "Test / Success!"})


# 分页查询 /list?page=<int>&pageSize=<int>
@billList.route('/list', methods=['GET'])
def page_bill_list():
    # 获取页码和每页个数
    page = int(request.args.get('page'))
    pageSize = int(request.args.get('pageSize'))

    # 限制每页查询上限
    if pageSize >= 100:
        return make_response(jsonify({'Msg': 'Over search limited!'}), 404)

    # 分页查询(判断页码和页数的有效性)
    if page is not None and pageSize is not None:
        bill_list = Query_bill(page, pageSize)
        data = bill_list.get_rows()
        return jsonify({"Msg": "Success", "Data": data})
    else:
        return make_response(jsonify({'error': 'Illegal request!'}), 404)

