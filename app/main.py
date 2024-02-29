from flask import Flask
from api.auth.endpoints import auth
from api.v1.user.endpoints import user
from api.v1.cook_form.endpoints import cook_form


app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(cook_form)


if __name__ == '__main__':
    app.run()