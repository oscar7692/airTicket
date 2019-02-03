from wtforms import Form
from wtforms import StringField, TextField, DateField
from wtforms.fields.html5 import EmailField

class TicketForm(Form):
    username = StringField('nombre completo')
    email = EmailField('email')
    date = DateField('fecha del viaje')
