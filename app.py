# encoding: utf-8
"""
@author: jinlin.xiao
@file: app.py
@time: 2019/6/17 8:47 AM
@desc:
启动方式
flask run
详细见：
http://note.youdao.com/noteshare?id=f43e871a39fa94abaf8c24ff3999193a

"""
from flask import Flask
from apps import register
from blueprint import register_blueprints
from exts import init_log


app = Flask(__name__)

init_log(app.logger)

register(app)
register_blueprints(app)


@app.route('/')
def index():
    return 'Index Page'



