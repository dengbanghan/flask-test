# -*- coding: utf-8 -*-
# @Time : 2024/6/8 下午11:09
# @Author : dengbanghan
# @Email : dengbanghan@gmail.com
# @File : user.py
# @Software: PyCharm
# @Description: exts.py文件主要是用来存放一些第三方插件的对象，如SQLAlchemy对象、Flask-Mail对象等

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import BaseConfig, DevConfig

app = Flask(__name__)

app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DevConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = BaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
