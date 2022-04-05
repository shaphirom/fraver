from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired

class userForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = EmailField('Email', validators = [DataRequired()])