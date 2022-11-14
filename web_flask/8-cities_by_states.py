#!/usr/bin/python3
"""Flask web application that returns an alternating html page"""
from flask import Flask, render_template
from models import storage
from models.state import State
# from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_states():
    sl = storage.all(State)
    # cl = storage.all(City)
    return render_template('8-cities_by_states.html', sl=sl)


@app.teardown_appcontext
def closing_time(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
