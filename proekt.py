# Проект quize для Python PRO]
# // Регистрация пользователя где номер телефона берем как идентификационные данные method: [POST]
# endpoint: /register/<name>/<number>
# response: {'status': 1, 'user_id': integer}
# {'status': 0, 'message': 'Ошибка в данных' || 'Номер под другим именем'}
# // Получить список лидеров (top 5), будет выбор между уровнями или <level:all> выдаст лучших со всех уровней
# method: [GET]
# endpoint: /leaders/<level>
# response: {'level': 'hard', 'ledaers':[
# {'user': score}, {'user2': score}, {'user3': score}, {'user4': score}, {'user5': score},
# ] }
# // Выбор уровня сложности, каждый уровень имеет таймер по окончанию которого не будет возможности продолжить тест и результат не засчитывается
# method: [GET]
# endpoint: /get-questions/<level>
# response: {'timer': в секундах, 'questions':
# [
# {'question_id':
# {'question': ['variant1', 'variant2', 'variant3', 'variant4']} },
# {'question_id':
# {'question': ['variant1', 'variant2', 'variant3', 'variant4']} }
# ] }
# // Проверка ответа(на текущий вопрос) пользователя, каждый вопрос проверяется сразу method: [POST]
# endpoint: /check-answer/<question_id>/<user_answer>
# response: {'status': 1} - если правильно
# {'status': 0} - если неправильно
# // На последнем вопросе нужна кнопка завершить чтобы получить результат от выполненного теста
# method: [POST]
# endpoint: /done/<user_id>
# response: {'status': 1, 'correct_answers': integer, 'position_on_top': integer}
