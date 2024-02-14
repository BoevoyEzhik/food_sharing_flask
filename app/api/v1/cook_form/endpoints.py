from flask import Blueprint, request, jsonify, session


cook_form = Blueprint('cook_form', __name__, url_prefix='/v1')


@cook_form.route('/create-cook-form')
def create_cook_form():
    pass


@cook_form.route('/update-cook-form')
def update_cook_form():
    pass


@cook_form.route('/get-my-all-cook-form')
def create_cook_form():
    pass