from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, InputRequired
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Regexp('^[a-z]{4,10}$',message='Your username should be between 4 and 10 characters long, and can only contain lowercase letters.')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords do not match. Try again')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Username already exist. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Comments
class AddCommentForm(FlaskForm):
    comment = StringField(
        "Leave a comment here!", validators=[InputRequired()])
    submit = SubmitField("Post")

