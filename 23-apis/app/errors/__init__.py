from flask import Blueprint

bp = Blueprint('errors', __name__, template_folder='templates')

# !IMPORTANT location here to prevent circular import
from app.errors import handlers
