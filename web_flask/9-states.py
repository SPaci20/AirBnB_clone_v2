#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from uuid import UUID

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage"""
    storage.close()


@app.route('/states')
def states():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('9-states.html', states=states)


@app.route('/states/<uuid:state_id>')
def states_by_id(state_id):
    """Display a HTML page with information about a specific State"""
    state = storage.get(State, state_id)

    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
