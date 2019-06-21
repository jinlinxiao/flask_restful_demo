# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_task.py
@time: 2019/6/18 8:09 PM
@desc:
"""
import requests
import json

Host = 'http://0.0.0.0:5002'


def test_flask():
    res = requests.get("%s/" % Host, data=None)
    print(res.content)
    # print(res.headers)
    # print(res.json())
    assert res.status_code == 200


def test_get_task_list():
    res = requests.get("%s/tasks" % Host, data=None)
    # print(res.content)
    # print(res.headers)
    tasks = res.json()
    print(tasks)
    print(list(tasks.keys())[-1])
    assert res.status_code == 200


def test_add_task():
    test_get_task_list()
    data = {
        'task': 'task4'
    }
    res = requests.post("%s/tasks" % Host, data=data)
    # res = requests.post("%s/tasks" % Host, data=json.dumps(data))
    # print(res.headers)
    print(res.json())
    assert res.status_code == 200
    test_get_task_list()


def test_delete_task():
    res = requests.get("%s/tasks" % Host, data=None)
    # print(res.content)
    # print(res.headers)
    tasks = res.json()
    print(tasks)
    task_id = list(tasks.keys())[-1]
    assert res.status_code == 200
    res = requests.delete("%s/tasks/%s" % (Host, task_id), data=None)
    # print(res.json())
    assert res.status_code == 204
    res = requests.get("%s/tasks" % Host, data=None)
    print(res.json())


def test_add_task_illegal():
    data = {'task': 5}
    res = requests.post("%s/tasks" % Host, data=json.dumps(data))
    print(res.content)
    assert res.status_code == 400


def test_add_task_illegal_no_task():
    data = {'task': '5', 'bb': '6'}
    res = requests.post("%s/tasks" % Host, data=json.dumps(data))
    print(res.content)
    assert res.status_code == 400


def test_get_one_task():
    task_id = 'task1'
    url = "%s/tasks/%s" % (Host, task_id)
    res = requests.get(url, data=None)
    assert res.status_code == 200
    print(res.json())


def test_update_one_task():
    task_id = 'task1'
    url = "%s/tasks/%s" % (Host, task_id)

    res = requests.get(url, data=None)
    assert res.status_code == 200
    print(res.json())

    task = "test_parser"
    data = {
        'task': task
    }
    res = requests.put(url, data=data)
    assert res.status_code == 201
    print(res.json())


def test_parser_legal():
    task_id = 'task5'
    task = "test_parser"
    data = {
        'task': task
    }
    url = "%s/tasks/%s" % (Host, task_id)
    res = requests.put(url, data=data)
    assert res.status_code == 201
    print(res.json())
    res = requests.get(url, data=None)
    assert res.status_code == 200
    print(res.json())
    res = requests.get("%s/tasks" % Host, data=None)
    assert res.status_code == 200
    print(res.json())


def test_parser_illegal():
    task_id = 'task6'
    task = 4
    data = {
        'task': task
    }
    url = "%s/tasks/%s" % (Host, task_id)
    res = requests.put(url, data=json.dumps(data))
    assert res.status_code == 400
    print(res.json())
    res = requests.get("%s/tasks" % Host, data=None)
    assert res.status_code == 200
    print(res.json())

