# encoding: utf-8
"""
@author: jinlin.xiao
@file: exts.py
@time: 2019/6/20 5:11 PM
@desc:
"""
from common import SafeDateFileHandler
import logging

app_log = logging.getLogger('flask.app.apps')

# db = Flask-SQLAlchemy()


def init_log(logger):
    logger.setLevel(logging.DEBUG)

    app_handler = SafeDateFileHandler.SafeDateFileHandler("hub")
    app_handler.setLevel(logging.DEBUG)  # DEBUG recommend
    # app_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    app_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s] %(message)s'))
    logger.addHandler(app_handler)


