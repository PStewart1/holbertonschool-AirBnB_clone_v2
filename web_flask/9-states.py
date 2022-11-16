#!/usr/bin/python3
"""Flask web application that returns an alternating html page"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    sl = storage.all(State)
    return render_template('9-states.html', sl=sl)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    states = storage.all(State)
    sl = None
    for state in states.values():
        if state.id == id:
            sl = state
    return render_template('9-states.html', sl=sl)


@app.teardown_appcontext
def closing_time(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
