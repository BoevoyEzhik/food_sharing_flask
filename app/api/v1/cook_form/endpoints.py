from flask import Blueprint, request, g, jsonify
from app.api.middleware import auth_required
from app.db.cook_form import (insert_cook_form_info,
                              update_cook_form_info,
                              db_get_my_all_cook_form,
                              db_get_all_cook_form)
import uuid


cook_form = Blueprint('cook_form', __name__, url_prefix='/v1')


@cook_form.route('/create-cook-form', methods=('GET', 'POST'))
@auth_required
def create_cook_form():
    if request.method == 'POST':
        content = request.get_json()
        content['id'] = str(uuid.uuid4())
        content['user_id'] = g.id
        try:
            insert_cook_form_info(content)
            return jsonify(status=200, response='success')
        except:
            return jsonify(status=500, response='DB ERROR')
    return jsonify(status=200, response='success')


@cook_form.route('/update-cook-form/<cook_form_id>', methods=('GET', 'PATCH'))
@auth_required
def update_cook_form(cook_form_id):
    if request.method == 'PATCH':
        content = request.get_json()
        try:
            update_cook_form_info(cook_form_id, content)
            return jsonify(status=200, response='success')
        except:
            return jsonify(status=500, response='DB ERROR')
    return jsonify(status=200, response='success')


@cook_form.route('/get-my-all-cook-form', methods=['GET'])
@auth_required
def get_my_all_cook_form():
    limit = request.args.get('limit', default=10)
    offset = request.args.get('offset', default=0)
    user_id = g.id
    try:
        content = db_get_my_all_cook_form(user_id, limit, offset)
        return jsonify(status=200, content=content)
    except:
        return jsonify(status=500, response='DB ERROR')


@cook_form.route('/get-all-cook-form', methods=['GET'])
def get_all_cook_form():
    limit = request.args.get('limit', default=10)
    offset = request.args.get('offset', default=0)
    try:
        content = db_get_all_cook_form(limit, offset)
        return jsonify(status=200, content=content)
    except:
        return jsonify(status=500, response='DB ERROR')
