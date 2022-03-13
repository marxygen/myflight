import random
import string

from flask import (Flask, redirect)
from .flights import flights_bp
from flask_bootstrap import Bootstrap
from .db.engine import create_tables


def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=random.choices(string.ascii_letters+string.digits, k=50)
    )
    Bootstrap(app)  # Apply Flask-Bootstrap

    app.register_blueprint(flights_bp)
    create_tables()

    @app.route('/')
    def redirect_to_dashboard():
        """Redirect user to /flights/ page when visiting index"""
        return redirect('flights/')

    return app
