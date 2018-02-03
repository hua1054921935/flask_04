# coding=utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from ihome import create_config
# from ihome import app,db
app,db=create_config('develop')

# 创建命令行启动
manager=Manager(app)
# 创建迁移对象绑定app和db
Migrate(app,db)

# 给命令行添加数据库迁移指令
manager.add_command('db',MigrateCommand)





if __name__ == '__main__':
    manager.run()