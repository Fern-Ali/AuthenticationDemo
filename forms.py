from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators, ValidationError, PasswordField
from wtforms.validators import InputRequired, Optional, Email, Length


class RegisterForm(FlaskForm):
    """Form for adding/editing friend."""

    username = StringField("username",
                       validators=[InputRequired()])
    password = PasswordField("password",
                        validators=[InputRequired(), Length(min= 10, max= 500, message="More than 10 chars please")])
    first_name = StringField("first name",
                        validators=[InputRequired()])
    last_name = StringField("last name",
                        validators=[InputRequired()])
    email = StringField("email",
                        validators=[InputRequired(), Email()])
    

class LoginForm(FlaskForm):
    """Form for adding/editing friend."""

    username = StringField("username",
                       validators=[InputRequired()])
    password = PasswordField("password",
                        validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    """Form for adding/editing friend."""

    title = StringField("title",
                       validators=[InputRequired()])
    content = StringField("comments",
                        validators=[InputRequired()])