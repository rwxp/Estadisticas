from flask import Flask
from src.routes.routes import app_blueprint
from src.routes.course_routes import course_blueprint
from src.routes.user_routes import user_blueprint
from config import config


def create_app():
    app = Flask(__name__, template_folder='src/templates')
    app.config.from_object(config['development'])  # o config['production'] para producción

    app.register_blueprint(app_blueprint)
    app.register_blueprint(course_blueprint)
    app.register_blueprint(user_blueprint)
    return app

app = create_app()
# Config setup


if __name__ == '__main__':
    app.run(debug=True)