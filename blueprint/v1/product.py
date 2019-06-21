# encoding: utf-8
"""
@author: jinlin.xiao
@file: product.py
@time: 2019/6/21 12:10 PM
@desc:
"""
from flask_restful import Resource
from exts import app_log


class Products(Resource):

    def get(self):
        app_log.info("request v1 products list.")
        return 'v1 Products list!'


class Product(Resource):

    def get(self, product_id):
        app_log.info("request v1 product detail.")
        return 'v1 provider %s!' % product_id
