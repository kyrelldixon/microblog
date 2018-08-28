from app import app
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
  """
  Registers items in the context of the `flask shell` environment
  Items returned will not have to be manually imported
  """
  return {
    'db': db,
    'User': User,
    'Post': Post
  }