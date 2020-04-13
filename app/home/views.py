from flask import  Blueprint


home = Blueprint('home', __name__)


@home.route('/')
def hello_world():
  return 'This is my first flask app using docker and travis-ci!'
