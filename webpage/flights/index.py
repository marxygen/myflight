from . import flights_bp
from flask import (render_template, )


@flights_bp.route('/')
def show_index():
    """List all currently tracked flights"""

    return render_template('flights/index.html')
