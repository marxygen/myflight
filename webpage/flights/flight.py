from . import flights_bp
from flask import (render_template, flash)
from webpage.db.engine import get_flight as select_flight


@flights_bp.route('<flight_code>/')
def get_flight(flight_code: str):
    flight = select_flight(flight_code)
    if not flight:
        flash(f'No flight with code "{flight_code}" is found', 'error')
        return render_template('flights/index.html')
    flight = flight[0]
    return render_template('flights/details.html', flight=flight)
