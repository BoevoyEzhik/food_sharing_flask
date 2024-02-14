from flask import Blueprint, request, jsonify, session


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        content = request.json
    pass


@auth.route('login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        pass
    pass


@auth.route('logout')
def logout():
    session.clear()
