from flask_sqlalchemy import SQLAlchemy
from config import config

import connexion

db = SQLAlchemy()


def create_app(config_name, updated_variables=None):
    connexion_app = connexion.App(__name__, specification_dir="../")
    connexion_app.add_api("swagger.yml")
    app = connexion_app.app
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

    app.logger.info("Booting up")

    return app
