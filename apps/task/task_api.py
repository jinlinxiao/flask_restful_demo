# encoding: utf-8
"""
@author: jinlin.xiao
@file: task_api.py
@time: 2019/6/19 9:54 AM
@desc:
"""
from flask_restful import reqparse, abort, Resource
from flask import request
# from flask import request, current_app
from exts import app_log


Tasks = {
    'task1': {'task': 'build an API'},
    'task2': {'task': '?????'},
    'task3': {'task': 'profit!'},
}


def abort_if_task_doesnt_exist(task_id):
    if task_id not in Tasks:
        abort(404, message="Todo {} doesn't exist".format(task_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


#   show a single
class Task(Resource):
    def get(self, task_id):
        """
        获取
        :param task_id:
        :return:
        """
        app_log.info('logged by flask.app.module')
        # current_app.app_log.info('logged by current_app.app_log')
        app_log.info("get task task_id=%s, type=%s" % (task_id, type(task_id)))
        # type = <class 'str'>
        abort_if_task_doesnt_exist(task_id)
        return Tasks[task_id]

    def delete(self, task_id):
        """
        删除
        :param task_id:
        :return:
        """
        abort_if_task_doesnt_exist(task_id)
        del Tasks[task_id]
        return '', 204

    def put(self, task_id):
        """
        更新
        :param task_id:
        :return:
        """
        abort_if_task_doesnt_exist(task_id)
        args = parser.parse_args()
        # 当 传入的task不是str类型时，args['task'] 是 None
        if not args['task']:
            abort(400, message="put task is not str.")
        app_log.info('task=%s,type(task)=%s' % (args['task'], type(args['task'])))
        task = {'task': args['task']}
        Tasks[task_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TaskList(Resource):

    def get(self):
        """
        获取 List
        :return:
        """
        # app_log.info('logged by flask.app')
        app_log.info('logged by flask.app task list')
        # current_app.app_log.info('logged by current_app.app_log')
        # 返回的json status 以及增加的header
        return Tasks, 200, {'Etag': 'some-opaque-string'}

    def post(self):
        """
        添加
        :return:
        """
        # args = parser.parse_args()
        print("=" * 20)
        print(request.args)
        print(request.data)
        print("=" * 20)
        args = parser.parse_args(strict=True)   # strict=True有作用？
        # 当 传入的task不是str类型时，args['task'] 是 None
        if not args['task']:
            abort(400, message="put task is not str.")
        task_id = int(max(Tasks.keys()).lstrip('task')) + 1
        task_id = 'task%i' % task_id
        Tasks[task_id] = {'task': args['task']}
        return Tasks[task_id]

