from database.models import Result, db, Rating


# Получить рейтинг пользователей
def get_rating_db(level):
    # Если по всем направлениям
    if level == 'all':
        rating = Result.query.all()

        rating_user = []


# Добавление ответа пользователя
def add_user_answer_db(user_id, user_answer, correctness):
    pass


# Добавление в рэйтинг
def add_user_rating_db(user_id, correct_answer):
    # Проверка есть ли пользователь в таблице (Rating)
    pass
