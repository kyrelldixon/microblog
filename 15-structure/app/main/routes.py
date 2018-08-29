from app import app
from app.main import bp
from flask import render_template, g, current_app
# !IMPORTANT login_required decorator requires current_user import
from flask_login import current_user, login_required

@bp.route('/')
@bp.route('/index')
@login_required
def index():
  posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
  ]

  return render_template("index.html",posts=posts)
