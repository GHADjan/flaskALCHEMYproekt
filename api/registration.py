from flask import Blueprint
from typing import Dict, List

registration_bp = Blueprint('registration', __name__)


# запрос на регистрацию
@registration_bp.route('/register/<string:name>/<integer:number>', methods=['POST'])
def register_user(name: str, number: int) -> Dict[str, int]:
    pass


