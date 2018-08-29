from flask import Blueprint

bp = Blueprint('errors', __name__)

# !IMPORTANT location here to prevent circular import
from app.errors import views
