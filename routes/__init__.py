from .item_routes import item_bp


def register_routes(app):
    app.register_blueprint(item_bp)
