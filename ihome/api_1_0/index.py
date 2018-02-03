# coding=utf-8
# 使用蓝图对象
from . import api

@api.route('/')
def hello_world():

    return 'hello flask'

