from flask import Flask
from .config      import Config
from .extensions  import db, migrate
from app.routes.chat import chat_bp
from app.routes.history_routes import history_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1) Init des extensions
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(chat_bp)
    app.register_blueprint(history_bp, url_prefix='/history') 

    # 2) Import manuel des modules modèles pour les enregistrer
    with app.app_context():
        from app.models import user, search_history, assistant, history, execution_count, roles, session

        

    return app
