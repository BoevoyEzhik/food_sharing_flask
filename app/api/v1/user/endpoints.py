from flask import Blueprint, request, jsonify, g
from app.db.users import db_update_user_info
from app.api.middleware import auth_required


user = Blueprint('user', __name__, url_prefix='/v1')


@user.route('/update-user-info', methods=('GET', 'PATCH'))
@auth_required
def update_user_info():
    if request.method == 'PATCH':
        content = request.get_json()
        try:
            db_update_user_info(g.id, content)
            return jsonify(status=200, response='success')
        except:
            return jsonify(status=500, response='DB ERROR')
    return jsonify(status=200, response='success')
