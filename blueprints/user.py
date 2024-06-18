# -*- coding: utf-8 -*-  
# @Time : 2024/6/8 下午11:09  
# @Author : dengbanghan  
# @Email : dengbanghan@gmail.com  
# @File : user.py  
# @Software: PyCharm

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify
from models.user import User
from exts import db, app
from tools.token import generate_token
from tools.logger import Logger
from tools.utils import jsonDumps
import re

bp = Blueprint('user', __name__, url_prefix="/user")
log = Logger("debug")

# 手机号验证的正则表达式
PHONE_REGEX = re.compile(r'^1[3-9]\d{9}$')
# 邮箱验证的正则表达式（简单示例）
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or 'login_type' not in data or ('login_type' == 'phone' and 'username' not in data) or (
            'login_type' == 'email' and 'username' not in data):
        return jsonify({'error': '请提供login_type和对应的值（phone或email）'}), 400

    login_type = data['login_type']
    username = data['username']
    if login_type == 'phone':
        if not PHONE_REGEX.match(username):
            return jsonify({'error': '手机号格式不正确，请提供11位数的手机号'}), 400
            # 手机号注册的后续逻辑...
    elif login_type == 'email':
        if not EMAIL_REGEX.match(username):
            return jsonify({'error': '邮箱格式不正确，请提供有效的邮箱地址'}), 400
            # 邮箱注册的后续逻辑...
    else:
        return jsonify({'error': '不支持的login_type，请提供phone或email'}), 400

    password = data['password']

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # 检查用户名是否已存在
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    # 创建新用户
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# 登录路由
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    log.info("入参：\n{}".format(jsonDumps({"username": username, "password": password})))

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # 查询用户
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # 生成token
    token = generate_token(user.id, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200
