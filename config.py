# -*- coding: utf-8 -*-
# @Time : 2024/6/8 下午11:09
# @Author : dengbanghan
# @Email : dengbanghan@gmail.com
# @File : user.py
# @Software: PyCharm

class BaseConfig:
    SECRET_KEY ="dengbanghan"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:abcd9876@server.dengbanghan.top:3306/users?charset=utf8mb4"

class QaConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysgl://[测试服务器MySQL 用户名]:[测试服务器 MySQL 密码]@[测试服务器 MySQL 域名]:[测试服务器 MySQL 端口号]/pythonbbs?charset=utf8mb4n"

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://[生产环境服务器MySOL 用户名1:1生产环境服务器 MySQL 密码]@[生产环境服务器 MySQL 域名]:[生产环境服务器 MSQI端口号]/pythonbbs?charset=utf8mb4"