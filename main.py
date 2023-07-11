from flask import Flask
from database .models import db
from flask_sqlalchemy import SQLAlchemy
from api import leaders, registration, test_process


app = Flask(__name__)


# Задать конфигурации для базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

# Задать приложение
db.init_app(app)

# Регистрация компонентов
app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bp)
app.register_blueprint(test_process.test_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
