from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email

class MyForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired('Please enter your name')])
    email = StringField('E-mail',validators=[DataRequired("Please enter your email address."), Email("Please enter a vaild email address.")])  
    subject = StringField('Subject',validators=[DataRequired("Please enter a subject")])
    message = TextAreaField('Message',validators=[DataRequired("Please type a message")])
    