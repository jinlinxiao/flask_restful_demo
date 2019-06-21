# encoding: utf-8
"""
@author: jinlin.xiao
@file: __init__.py
@time: 2019/6/19 2:29 PM
@desc:
"""
from flask_restful import Api
from apps.task import task_api
from apps.upload import upload_api


def register(app):
    #
    # Actually setup the Api resource routing here
    #
    api = Api(app)
    api.add_resource(task_api.TaskList, '/tasks')
    api.add_resource(task_api.Task, '/tasks/<task_id>')
    api.add_resource(upload_api.Upload, '/upload')

