from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class TicketForm(Form):
    username = StringField('nombre completo', 
            [validators.required(), validators.length(max=40)])
    email = EmailField('email', 
            [validators.required(), validators.length(max=40)])
    date = DateField('fecha del viaje', 
            [validators.required(), validators.length(max=40)])
