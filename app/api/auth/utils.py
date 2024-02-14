import re
import datetime
from functools import wraps


def email_validator(email):
    pass


def age_validator(age):
    pass


def generating_hash(password):
    pass


def check_password(password):
    pass


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
