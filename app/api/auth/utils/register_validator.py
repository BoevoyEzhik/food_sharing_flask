import re
from datetime import date


def is_valid_email(email):
    regex = re.compile(r'[a-zA-Z][a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$')
    return bool(re.fullmatch(regex, email))


def is_valid_age(birthday):
    today = date.today()
    birthday = date(*(int(i) for i in birthday.split('-')))
    if today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) + 1 > 120:
        return False
    return True

