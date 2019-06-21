# encoding: utf-8
"""
@author: jinlin.xiao
@file: provider.py
@time: 2019/6/21 12:09 PM
@desc:
"""
from flask_restful import Resource
from exts import app_log


class Providers(Resource):

    def get(self):
        app_log.info("request v1 providers list.")
        return 'v1 providers list!'


class Provider(Resource):

    def get(self, provider_id):
        app_log.info("request v1 providers detail.")
        return 'v1 provider %s!' % provider_id
