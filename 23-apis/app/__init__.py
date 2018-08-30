from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# DB Middleware
db = SQLAlchemy()
migrate = Migrate()

# Custom Middleware
login = LoginManager()
bootstrap = Bootstrap()
login.login_view = 'auth.login'

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  migrate.init_app(app, db)
  login.init_app(app)
  bootstrap.init_app(app)

  from app.errors import bp as errors_bp
  app.register_blueprint(errors_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.api import bp as api_bp
  app.register_blueprint(api_bp, url_prefix='/api/v1')

  return app

from app import models