from . import flights_bp
from flask import (render_template, )
from webpage.db.engine import get_flights


@flights_bp.route('/')
def show_index():
    """List all currently tracked flights"""
    return render_template('flights/index.html', flights=get_flights())
