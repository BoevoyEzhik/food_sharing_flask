import jwt


def generate_jwt_token(user_id):
    key = 'secret_key'
    sign_data = jwt.encode({"token": user_id}, key, algorithm="HS256")
    return sign_data





