import os
from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = os.environ.get('MAIN')
migrate = Migrate()

def create_app(config=Config):
    app = Flask(__name__, template_folder=os.environ.get('TEMPLATE_FOLDER'))
    app.config.from_object(config)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    with app.app_context():
        db.create_all()
    
    from .test import test
    app.register_blueprint(test)
    
    #from .auth import auth
    #app.register_blueprint(auth)

    #from .main import main
    #app.register_blueprint(main)
    
    return app