from flask import Flask
from extensions import db
from middleware import request_logger, validate_item_data
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import models to register them with SQLAlchemy
    with app.app_context():
        import models
        db.create_all()

    # Register routes
    from routes import register_routes
    register_routes(app)

    # Apply logging middleware
    app.before_request(request_logger)

    # Apply validation middleware for POST and PUT requests
    @app.before_request
    def validate_request():
        error_response = validate_item_data()
        if error_response:
            return error_response

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
