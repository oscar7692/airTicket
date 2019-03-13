#!/usr/bin/python3.6
from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
import forms
import json


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'my_secret_key'
csrf_token = CSRFProtect(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/airticket"
mongo = PyMongo(app)


@app.route('/')
def index():
    data_qry = mongo.db.qatar_ticket
    for data in data_qry.find():
        data = data['qatar']
        enddata = render_template('index.html', data=data)
    return enddata
    # ticketform = forms.TicketForm()
    # title = "airTicket"
    # return render_template('index.html', title=title, form=ticketform)


@app.route('/emirates')
def emirates():
    title = "Emirates Airlines"
    return render_template('emirates_ticket.html', title=title)


@app.route('/qatar', methods=['GET', 'POST'])
def qatar_ticket():
    title = "Qatar Airlines"
    qatar_ticket = forms.TicketForm(request.form)
    if request.method == 'POST' and qatar_ticket.validate():
        qatar = mongo.db.qatar_ticket
        data = request.form.to_dict()
        qatar_ticket.insert({'qatar': data})
        print('JSON', data)
        # print(qatar_ticket.username.data)
        # print(qatar_ticket.email.data)
        # print(qatar_ticket.date.data)
        # print(qatar_ticket.carddetail.data)
    else:
        print('form error')
    return render_template('qatar_ticket.html', title=title, form=qatar_ticket)


# test function
# @app.route('/params')
# def parameters():
#     param = request.args.get('param1', 'parametro')
#     return 'hello params is {}'.format(param)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
