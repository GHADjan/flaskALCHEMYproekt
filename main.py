from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import leaders, registration, test_process


app = Flask(__name__)
db = SQLAlchemy()

# Задать конфигурации для базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

# Задать приложение
db.init_app(app)

# Регистрация компонентов
app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bp)
app.register_blueprint(test_process.test_bp)





