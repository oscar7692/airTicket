from wtforms import Form
from wtforms import StringField, TextField, DateField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators


def honeypot_val(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('field has to be empty')


class TicketForm(Form):
    username = StringField('Full name',
                           [
                               validators.Required(message='full name is '
                                                   'required'),
                               validators.length(
                                   min=3, max=40,
                                   message='field length is invalid min=3 '
                                   'max=40 characters')
                           ])
    email = EmailField('Email address',
                       [
                           validators.Required(message='email is needed'),
                           validators.Email(message='invalid email format')
                       ])
    origin = StringField('Origen',
                         [
                             validators.Required(message='origin is required'),
                             validators.length(min=2, max=25,
                                               message='field length is '
                                               'invalid min=2 max=25 characters')
                         ])
    destination = StringField('Destino',
                              [
                                  validators.Required(message='destination is '
                                                      'required'),
                                  validators.length(min=2, max=25,
                                                    message='field length is '
                                                    'invalid min=2 max=25 '
                                                    'characters')
                              ])
    date = DateField('Travel date (YYYY-MM-DD)', format='%Y-%m-%d')
    # pasenger = IntegerField('Number of passengers' [validators.Required(
    #     message='number of passengers is required'),
    #                                                 validators.length(min=1,
    #                                                                   max=5,
    #                                                 message='passengers required')])
    carddetail = StringField('card number',
                             [
                                 validators.Required(message='card data is '
                                                     'empty'),
                                 validators.length(min=16, max=16,
                                                   message='field cannot sent '
                                                   'empty min/max=16 '
                                                   'characters')
                             ])
    honeypot = HiddenField('', [honeypot_val])
