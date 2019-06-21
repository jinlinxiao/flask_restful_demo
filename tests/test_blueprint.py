# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_blueprint.py
@time: 2019/6/21 3:02 PM
@desc:
"""

import requests
import json

Host = 'http://0.0.0.0:5002'


class TestBlueprintV1(object):

    def test_get_providers(self):
        url = "%s/v1/providers" % Host
        res = requests.get(url, data=None)
        print(res.content)
        # print(res.headers)
        assert res.status_code == 200

    def test_get_provider(self):
        provider_id = "11234"
        url = "%s/v1/providers/%s" % (Host, provider_id)
        res = requests.get(url, data=None)
        print(res.content)
        # print(res.headers)
        assert res.status_code == 200


class TestBlueprintV2(object):

    def test_get_providers(self):
        url = "%s/v2/providers" % Host
        res = requests.get(url, data=None)
        print(res.content)
        # print(res.headers)
        assert res.status_code == 200

    def test_get_provider(self):
        provider_id = "11234"
        url = "%s/v2/providers/%s" % (Host, provider_id)
        res = requests.get(url, data=None)
        print(res.content)
        # print(res.headers)
        assert res.status_code == 200



