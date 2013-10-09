from flask.ext.wtf import Form, TextField, BooleanField, IntegerField, SubmitField, validators, ValidationError, PasswordField
from flask.ext.wtf import Required

class LoginForm(Form):
    #openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    name = TextField('Name', validators = [Required()])   
    email = TextField('email', validators = [validators.Required(),validators.Email(message="Please enter a valid email address")])
    phone_number = IntegerField('Phone Number', validators = [Required()])
    #amount = IntegerField('Amount', validators = [Required()])


class StartPage(Form):
    a = BooleanField('placeholder', default = False)   

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=5, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


class AdminForm(Form):
    hyperlink = TextField('hyperlink', [validators.Length(min=4, max=999)])
    amount = TextField('Amount', [validators.Length(min=1, max=35)])
    description = TextField('Description', [validators.Length(min=1, max=999)])
