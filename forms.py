from wtforms import Form
from wtforms import StringField, TextField, DateField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators


def honeypot_val(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('field has to be empty')


class TicketForm(Form):
    username = StringField('Full name',
                           [
                               validators.Required(message='full name is required'),
                               validators.length(
                                   min=3, max=40, message='field length is invalid min=3 max=40 characters')
                           ])
    email = EmailField('Email address',
                       [
                           validators.Required(message='email is needed'),
                           validators.Email(message='invalid email format')
                       ])
    date = DateField('Travel date (YYYY-MM-DD)', format='%Y-%m-%d')
    carddetail = StringField('card number',
                             [
                                 validators.Required(message='card data is empty'),
                                 validators.length(min=16, max=16,
                                                   message='field cannot sent empty min/max=16 characters')
                             ])
    honeypot = HiddenField('', [honeypot_val])
