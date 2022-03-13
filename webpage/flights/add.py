from sqlalchemy.exc import IntegrityError

from . import flights_bp
from flask import (request, render_template, redirect, url_for, flash)
from webpage.utils.flights import validate_flight_code, fetch_flight_information
from webpage.db.engine import create_flight
from psycopg2.errors import UniqueViolation


@flights_bp.route('add/', methods=('GET', 'POST'))
def add_flight():
    if request.method == 'POST':
        code = request.form.get('flight-code')
        is_valid, message = validate_flight_code(code)
        if not is_valid:
            flash(message, 'error')
        else:
            try:
                flight_data = fetch_flight_information(code)
                if not flight_data:
                    raise Exception(f'No flight data is available')
                flight_data = flight_data[0]
                create_flight(code=code, **flight_data)
                flash(f'Flight "{code}" has been successfully added', 'info')
                return redirect(url_for('flights.show_index'))
            except (IntegrityError, UniqueViolation):
                flash('This flight is already added', 'error')
            except Exception as e:
                flash(f'Something went wrong: {e}', 'error')

    return render_template('flights/add.html')
