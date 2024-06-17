# -*- coding: utf-8 -*-  
# @Time : 2024/6/16 上午11:45  
# @Author : dengbanghan  
# @Email : dengbanghan@gmail.com  
# @File : token.py  
# @Software: PyCharm

import jwt
from datetime import datetime, timezone, timedelta
from jwt import PyJWTError


# 密钥（请确保在生产环境中使用安全的密钥）
SECRET_KEY = 'your-secret-key'
# 定义JWT的有效期（可选）
EXPIRATION_DELTA = timedelta(days=1)
def generate_token(id, secret_key):
    # 定义载荷（Payload）
    payload = {
        'sub': id,  # 用户的唯一标识
        'name': 'John Doe',  # 用户名或其他标识信息
        'admin': True,  # 管理员权限标志
        'iat': datetime.now(timezone.utc),  # JWT 的签发时间
        'exp': datetime.now(timezone.utc) + EXPIRATION_DELTA  # JWT 的过期时间
    }
    # 生成 JWT 令牌
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def analysis_token(token, secret_key):
    # 解析 JWT 令牌
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except PyJWTError as e:
        print(f"Error decoding JWT: {e}")
