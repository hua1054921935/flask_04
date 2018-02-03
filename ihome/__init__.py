# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_dict




app = Flask(__name__)


# 目前, db的创建, 放入了函数中. 其他文件用的的时候, 希望直接获取db
db=SQLAlchemy(app)




def create_config(config_name):

    # 配置需要紧跟着app创建
    app.config.from_object(config_dict[config_name])

    # 可以延迟导入app对象 --> 用app核心是为了获取配置文件
    db.init_app(app)
    # db=SQLAlchemy(app)
    # 注册蓝图对象
    # 为了解决循环导入, 可以将某一方延迟导入(用到时再导入)
    from ihome.api_1_0 import api
    app.register_blueprint(api,url_prefix='/api_1_0')


    return app,db



