from flask import Blueprint, request, jsonify, session


user = Blueprint('user', __name__, url_prefix='/v1')


@user.route('/update-user-info')
def update_user_info():
    pass