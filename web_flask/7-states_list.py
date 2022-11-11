#!/usr/bin/python3
"""Flask web application that returns an alternating html page"""
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)


# @app.route("/", strict_slashes=False)
# def index():
#     return "Hello HBNB!"


# @app.route('/hbnb', strict_slashes=False)
# def hbnb():
#     return 'HBNB'


# @app.route('/c/<text>', strict_slashes=False)
# def variable(text):
#     return 'C {}'.format(text.replace('_', ' '))


# @app.route('/python', strict_slashes=False)
# @app.route('/python/<text>', strict_slashes=False)
# def python(text="is cool"):
#     return 'Python {}'.format(text.replace('_', ' '))


# @app.route('/number/<int:n>', strict_slashes=False)
# def number(n):
#     return '{} is a number'.format(n)


@app.route('/states_list', strict_slashes=False)
def states():
    from models.state import State
    # from models.city import City
    sl = storage.all(State)
    # cl = storage.all(City)
    return render_template('7-states_list.html', sl=sl)


# @app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
# def even_odd(num):
#     mod = num % 2
#     if mod > 0:
#         n = "{} is odd".format(num)
#     else:
#         n = "{} is even".format(num)
#     return render_template('6-number_odd_or_even.html', n=n)


@app.teardown_appcontext
def closing_time():
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
