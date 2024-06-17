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

bp = Blueprint('user', __name__, url_prefix="/user")

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

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
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # 查询用户
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # 生成token
    token = generate_token(user.id, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200
