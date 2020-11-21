from microservice.models import (
    Booking,
)
from microservice.services import mock
from microservice import create_app


import os, connexion
from dotenv import load_dotenv

# DOT ENV
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# APP
app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.logger.info("Botting finished")

# Shell
@app.shell_context_processor
def make_shell_context():
    from microservice import db
    return {
        "db": db,
        "mock": mock,
        "Booking": Booking,
    }


@app.cli.command()
def deploy():
    """Run deployment tasks."""

    # Insert fake data
    # mock.everything()
