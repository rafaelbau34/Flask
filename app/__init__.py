from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "chavo"

    # Importa y registra las rutas
    from .routes import main
    app.register_blueprint(main)

    return app
