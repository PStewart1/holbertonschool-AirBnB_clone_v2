#!/usr/bin/python3
"""Flask web application that returns an alternating html page"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    sl = storage.all(State)
    al =storage.all(Amenity)
    return render_template('10-hbnb_filters.html', sl=sl, al=al)


@app.teardown_appcontext
def closing_time(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
