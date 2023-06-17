from database.models import Result, db, Rating, User


# Получить рейтинг пользователей
def get_rating_db(level):
    # Если по всем направлениям
    if level == 'all':
        rating = Result.query.all()

        rating_user = []
        for user_rating in rating:
            user = User.query.filter(id=user_rating.user_id).first()
            rating_user.append((user.name, user_rating.user_correct_ansswer))
            return rating_user


# Добавление ответа пользователя
def add_user_answer_db(user_id, user_answer, correctness):
    result = Rating(user_id=user_id,
                    user_answer=user_answer,
                    correctness=correctness)
    db.session.add(result)
    db.session.commit()


# Добавление в рэйтинг
def add_user_rating_db(user_id, correct_answer):
    # Проверка есть ли пользователь в таблице (Rating)
    user_rating = Rating.query.filter(user_id=user_id).first()
    if user_rating:
        user_rating.user_correct_ansswer += correct_answer

    else:
        user_rating = Rating(user_id=user_id,
                             user_correct_answer=correct_answer)
        db.session.add(user_rating)
    db.session.commit()
