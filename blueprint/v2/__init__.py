# encoding: utf-8
"""
@author: jinlin.xiao
@file: __init__.py
@time: 2019/6/21 12:08 PM
@desc:
"""
from flask import Blueprint
from flask_restful import Api
from blueprint.v2.provider import Providers, Provider
from blueprint.v2.product import Products, Product


def register_views(app):
    api = Api(app)
    api.add_resource(Providers, '/providers')
    api.add_resource(Provider, '/providers/<provider_id>')
    api.add_resource(Products, '/products')
    api.add_resource(Product, '/products/<product_id>')


def create_blueprint_v2():
    """
    注册蓝图->v2版本
    """
    bp_v2 = Blueprint('v2', __name__)
    register_views(bp_v2)
    return bp_v2

