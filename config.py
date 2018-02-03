# coding=utf-8

class Config(object):
    SQLALCHEMY_DATABASE_URI='mysql://root:mysql@127.0.0.1/home_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    pass



config_dict={'develop':DevelopmentConfig,
             'product':ProductionConfig}