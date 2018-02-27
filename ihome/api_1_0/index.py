# coding=utf-8
# 使用蓝图对象
import logging
from . import api
from ihome import redis_store

#TODO 记得导入models否则无法迁移成功
# 操作步骤init migrate upgrade
from ihome import models

@api.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'index'

