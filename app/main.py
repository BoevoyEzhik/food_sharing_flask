from flask import Flask
from api.auth.endpoints import auth

app = Flask(__name__)
app.register_blueprint(auth)


@app.route('/')
def index():
    return 'Hello, World'


if __name__ == '__main__':
    app.run()