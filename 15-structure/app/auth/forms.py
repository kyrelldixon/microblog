from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  remember_me = BooleanField('Remember Me?')
  submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired(), Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    """
    Ensures username is not present in the database.
    Function automatically called by WTForms
    """
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Please use a different username.')

  def validate_email(self, email):
    """
    Ensures email is not present in the database.
    Function automatically called by WTForms
    """
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Please use a different email.')
