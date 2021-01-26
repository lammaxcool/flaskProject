import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# export one of settings from config
app.config.from_object(os.environ['APP_SETTINGS'])
# set SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import City, Station


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)


if __name__ == '__main__':
    app.run()
