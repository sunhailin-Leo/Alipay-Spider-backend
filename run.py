# -*- coding: UTF-8 -*-
"""
Created on 2017年9月29日
@author: Leo
"""

# 项目库
from bill import billList
from conf.mgo import return_mgo as mgo

# Flask库和第三方库
from flask import Flask


# 初始化
def create_app():
    app = Flask(__name__)
    app.register_blueprint(billList, url_prefix='/v1/billList')

    return app


if __name__ == '__main__':
    if mgo().client is not None:
        service = create_app()
        service.run(port=9100, debug=True)
    else:
        exit(1)
