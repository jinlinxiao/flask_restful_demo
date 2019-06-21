# encoding: utf-8
"""
@author: jinlin.xiao
@file: provider.py
@time: 2019/6/21 12:09 PM
@desc:
"""
from flask_restful import Resource


class Providers(Resource):

    def get(self):
        return 'v2 providers list!'


class Provider(Resource):

    def get(self, provider_id):
        return 'v2 provider %s!' % provider_id
