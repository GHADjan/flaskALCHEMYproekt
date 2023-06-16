from flask import Blueprint
from typing import Dict, List
from pydantic import BaseModel

test_bp = Blueprint('test_process', __name__)


# Валидатор вопросов
class Questions(BaseModel):
    timer: int
    questions: List[Dict[int, Dict[str, List[str]]]]



# Запрос на получение всех вопросов
@test_bp.route('/get-questions/<string:level>', methods=['GET'])
def get_user_question(level: str) -> Questions:
    pass


# Запрос на проверку ответа от пользователя
@test_bp.route('/check-answer/<int:question_id>/<string:user_answer', methods=['POST'])
def check_current_user_answer(question_id: int, user_answer: str) -> Dict[str, int]:
    pass


# Запрос на вывод результата
@test_bp.route('/done/<int:user_id>', methods=['POST'])
def user_done_test(user_id: int) -> Dict[str, int]:
    pass


