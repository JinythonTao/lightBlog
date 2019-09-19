from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object('config')
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "该页面需要用户登录之后才能访问哟~~"

# 数据库实例
db = SQLAlchemy(app)

# 邮件实例
mail = Mail(app)

# 前端样式bootstrap实例
bootstrap = Bootstrap(app)

# 日期统一
moment = Moment(app)


from app import views, models, errors
