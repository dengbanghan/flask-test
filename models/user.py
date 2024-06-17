# -*- coding: utf-8 -*-  
# @Time : 2024/6/8 下午11:20  
# @Author : dengbanghan  
# @Email : dengbanghan@gmail.com  
# @File : user.py  
# @Software: PyCharm

from exts import db, app


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # 这里可以是手机号或邮箱
    password_hash = db.Column(db.String(255))

# 在创建应用之后调用 db.create_all() 生成表的字段
with app.app_context():
    db.create_all()
