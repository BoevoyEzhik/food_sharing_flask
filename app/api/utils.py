import jwt


def validate_jwt_token(token):
    secret_key = 'secret_key'
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms='HS256')
        return decoded_token
    except jwt.DecodeError:
        return False
    except jwt.ExpiredSignatureError:
        return False
