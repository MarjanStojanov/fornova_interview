import sys
import traceback

from flask import Flask

from config import Config
from errors import ConnectorError


def _load_config(app: Flask):
    app.config.from_object(Config)
    return app


def _register_blueprints(app: Flask):
    from hotel_routes import hotels_bp

    app.register_blueprint(hotels_bp)
    return app


def _register_error_handlers(app: Flask):
    @app.errorhandler(404)
    def handle_404(error: Exception):
        return "Page Not Found", 404

    @app.errorhandler(405)
    def handle_405(error: Exception):
        return "Method Not Allowed", 405

    @app.errorhandler(ConnectorError)
    def handle_connector_error(error: ConnectorError):
        return f"Upstream Service Error: {error.error_json}", error.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_errors(error):
        etype, value, tb = sys.exc_info()
        print(traceback.print_exception(etype, value, tb))
        return "Internal Server Error", 500

    return app


def _register_healthcheck(app: Flask):
    @app.get("/ping")
    def ping():
        return "pong"

    return app


def create_app():
    app = Flask(__name__)

    app = _load_config(app)

    app = _register_blueprints(app)
    app = _register_error_handlers(app)
    app = _register_healthcheck(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
