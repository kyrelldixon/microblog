# Microblog Flask Application

Project based on the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Chapter Notes

1. Hello World!
    - Remember to use `export FLASK_APP={filename}` if you want to use `flask run`
    - `flask run` doesn't work, use `python -m flask run` after the export
    - To prevent worrying about the export:
      1. `pip install python-dotenv`
      2. Create `.flaskenv` file
      3. Add `export FLASK_APP={filename}` to file

2. Templates
   - Use templates for modularity
   - Using [Jinja2](http://jinja.pocoo.org/docs/2.10/templates/) (included with Flask) as templating engine