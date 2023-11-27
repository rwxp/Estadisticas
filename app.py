from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes.usuario_routes import usuarios_blueprint
from config import config


def create_app():
    app = Flask(__name__, template_folder='src/templates')
    app.config.from_object(config['development'])  # o config['production'] para producción

    app.register_blueprint(usuarios_blueprint)

    return app

app = create_app()
# Config setup


if __name__ == '__main__':
    app.run(debug=True)