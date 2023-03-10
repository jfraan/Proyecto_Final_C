from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)

#     from app.routes import main_routes, api_routes
#     app.register_blueprint(main_routes)
#     app.register_blueprint(api_routes, url_prefix='/api')

#     return app


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app
