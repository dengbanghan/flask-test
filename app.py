# -*- coding: utf-8 -*-
# @Time : 2024/6/8 下午11:09
# @Author : dengbanghan
# @Email : dengbanghan@gmail.com
# @File : user.py
# @Software: PyCharm

from flask import Flask
from blueprints.user import bp as user_bp
from flask_migrate import Migrate
from exts import db, app
import config

app.config.from_object(config.DevConfig)
app.register_blueprint(user_bp)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
