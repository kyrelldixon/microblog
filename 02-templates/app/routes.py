from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  user = { 
    "name": "Miguel",
    "shoe_size": 12
  }
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

  return render_template("index.html",user=user,posts=posts)
