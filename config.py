import os
from logging import FileHandler, Formatter

fileHandler = FileHandler("microservice.log", encoding="utf-8")
fileHandler.setFormatter(
    Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "top secret"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///gooutsafe.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # https://avatars.dicebear.com/api/avataaars/roma%20molesta.svg
    # AVATAR_PROVIDER = "https://avatars.dicebear.com/api/avataaars/{seed}.svg"

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    @staticmethod
    def init_app(app):
        app.logger.addHandler(fileHandler)


class DevelopmentConfig(Config):

    DEBUG = True

    @staticmethod
    def init_app(app):
        app.debug = True
        app.logger.addHandler(fileHandler)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("TEST_DATABASE_URL") or "sqlite:///gooutsafe_test.db"
    )


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "docker": DockerConfig,
    "default": DevelopmentConfig,
}