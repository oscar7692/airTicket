#!/usr/bin/python3.6
from flask import Flask
from flask import render_template
from flask import request
import forms


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    ticketform = forms.TicketForm()
    title = "airTicket"
    return render_template('index.html', title=title, form=ticketform)


@app.route('/emirates')
def emirates():
    title = "Emirates Airlines"
    return render_template('emirates_ticket.html', title=title)


@app.route('/qatar', methods=['GET', 'POST'])
def qatar():
    title = "Qatar Airlines"
    qatar_ticket = forms.TicketForm(request.form)
    if request.method == 'POST' and qatar_ticket.validate():
        print(qatar_ticket.username.data)
        print(qatar_ticket.email.data)
        print(qatar_ticket.date.data)
        print(qatar_ticket.carddetail.data)
    return render_template('qatar_ticket.html', title=title, form=qatar_ticket)


# test function
# @app.route('/params')
# def parameters():
#     param = request.args.get('param1', 'parametro')
#     return 'hello params is {}'.format(param)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
