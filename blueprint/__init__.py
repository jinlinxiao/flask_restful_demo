# encoding: utf-8
"""
@author: jinlin.xiao
@file: __init__.py
@time: 2019/6/21 12:08 PM
@desc:
"""
from blueprint.v1 import create_blueprint_v1
from blueprint.v2 import create_blueprint_v2


def register_blueprints(app):
    # 注册版本
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
    app.register_blueprint(create_blueprint_v2(), url_prefix='/v2')
