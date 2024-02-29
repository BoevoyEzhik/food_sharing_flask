from functools import wraps
from flask import request, Response, g
from .utils import validate_jwt_token


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sign_cookie = request.cookies.get('token')
        user = validate_jwt_token(sign_cookie)
        if user:
            g.id = user['token']
            return func(*args, **kwargs)
        return Response(status=403, response='Invalid token')
    return wrapper
