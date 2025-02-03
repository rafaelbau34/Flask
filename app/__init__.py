from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "chavo"

    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a la base de datos MySQL")
        except Exception as e:
            print(f"❌ Error conectando a MySQL: {e}")

    # Importa y registra las rutas
    from .routes import main
    app.register_blueprint(main)

    return app
