from flask import Blueprint, request, make_response, jsonify

from .utils.register_validator import is_valid_email, is_valid_age
from .utils.password import is_valid_password, generating_hash
from .utils.jwt_utils import generate_jwt_token

from app.api.middleware import auth_required
from app.db.users import get_user_by_email, insert_user_info

import uuid


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        content = request.get_json()
        if not is_valid_email(content['email']):
            return jsonify(status=403, response='Incorrect email format')
        if get_user_by_email(content['email']):
            return jsonify(status=403, response='This email already registered')
        if not is_valid_age(content['birthday']):
            return jsonify(status=403, response='Incorrect birthday')
        content['id'] = str(uuid.uuid4())
        content['password'] = generating_hash(content['password'])
        try:
            insert_user_info(content)
            return jsonify(status=200, response='Successfully registration')
        except:
            return jsonify(status=500, response='DB ERROR')
    return jsonify(status=200, response='success')


@auth.route('login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        content = request.get_json()
        user = get_user_by_email(content['email'])
        if not user:
            return jsonify(status=403, response='Email not registered')
        if not is_valid_password(content['password'], user['password_hash']):
            return jsonify(status=403, response='Wrong password')
        resp = make_response(jsonify(status=200, response='ok'))
        resp.set_cookie('token', generate_jwt_token(user['id']))
        return resp
    return jsonify(status=200, response='success')


@auth.route('logout')
@auth_required
def logout():
    resp = make_response(jsonify(status=200, response='ok'))
    cookies = request.cookies
    for cookie in cookies:
        resp.delete_cookie(cookie)
    return resp

