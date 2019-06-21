# encoding: utf-8
"""
@author: jinlin.xiao
@file: upload_api.py
@time: 2019/6/19 11:59 AM
@desc:
"""
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class Upload(Resource):

    def get(self):
        return {'err_code': 0, 'err_msg': 'success'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']
        return file.name, 201



