from wtforms import Form
from wtforms import StringField, TextField, DateField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class TicketForm(Form):
    username = StringField('Full name',
                           [validators.length(min=4, max=30,
                                              message='field cannot sent'
                                              ' empty!')])
    email = EmailField('Email address')
    date = DateField('Travel date')
    carddetail = StringField('card number',
                             [validators.length(min=16, max=16,
                                                message='field cannot sent'
                                                ' empty')])
