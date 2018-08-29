from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# Main app
app = Flask(__name__)
app.config.from_object(Config)

# DB Middleware
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Custom Middleware
login = LoginManager(app)
bootstrap = Bootstrap(app)
login.login_view = 'auth.login'

# Blueprints
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app import routes, models
