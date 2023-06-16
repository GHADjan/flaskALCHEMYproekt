import random

from database.models import Question, db



# Получить вопросы
def get_questions_db(level):
    # Если левел не указан
    if level == 'all':
        questions = []
        all_questions = Question.query.all()

        # 20 рандомных вопросов
        for i in range(20):
            questions.append(random.choice(all_questions))
        return questions

    # Если указал сложность , то фильтр по вопросам
    questions_from_level = Question.query.filter(level=level).all()

    question = [random.choice(questions_from_level) for i in range(20)]
    return question

# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    current_question = Question.query.get(question_id)

    # Проверка ответа пользователя с реальным ответом в базе
    if current_question.correct_answer == user_answer:
        return True
    return False

# добавление вопросов в базу (ДЗ)
