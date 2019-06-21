# encoding: utf-8
"""
@author: jinlin.xiao
@file: product.py
@time: 2019/6/21 12:10 PM
@desc:
"""
from flask_restful import Resource


class Products(Resource):

    def get(self):
        return 'v1 Products list!'


class Product(Resource):

    def get(self, product_id):
        return 'v1 provider %s!' % product_id
