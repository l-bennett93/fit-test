from flask.cli import FlaskGroup
from project import app

cli = FlaskGroup()

if __name__ == "__main__":
    cli()
