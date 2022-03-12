from flask import (Flask, redirect)
from .flights import flights_bp
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)  # Apply Flask-Bootstrap

    app.register_blueprint(flights_bp)

    @app.route('/')
    def redirect_to_dashboard():
        """Redirect user to /flights/ page when visiting index"""
        return redirect('flights/')

    return app
