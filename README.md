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

3. Webforms
4. Database
   - Requirements:
      - `flask-sqlalchemy` for class based sql tables
      - `flask-migrate` for easy migration to other sql types (PostgreSQL, MySQL, SQLite)
   - [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) steps
      1. `flask db init`
          - This creates the initial migrations folder
      2. `flask db migrate -m "users table"`
          - Creates migration script
      3. `flask db upgrade`
          - Runs migration script which makes changes to database
          - Can also use `downgrade` to go back to earlier states
   - You can use Flask-Alchemy to [query](http://flask-sqlalchemy.pocoo.org/2.3/queries/) records in the database
   - Shell Context