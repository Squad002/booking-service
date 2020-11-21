from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import connexion
from config import config


# Debug
import flask_profiler

db = SQLAlchemy()

def create_app(config_name, updated_variables=None):
    application = connexion.App(__name__)
    application.add_api('swagger.yml')
    app = application.app
    app.config.from_object(config[config_name])
    if updated_variables:
        app.config.update(updated_variables)

    config[config_name].init_app(app)
    context = app.app_context()
    context.push()

    from microservice.views import blueprints

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    db.init_app(app)
    db.create_all(app=app)

    # from microservice.services import mock
    # mock.everything()

    app.logger.info("Booting up")

    return app
