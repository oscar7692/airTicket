#!/usr/bin/python3.6
from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template, redirect
from flask import request
from flask import url_for
from flask_wtf import CSRFProtect
import forms


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'my_secret_key'
app.config["MONGO_URI"] = "mongodb://localhost:27017/airTcketdb"
mongo = PyMongo(app)
csrf_token = CSRFProtect(app)


@app.route('/')
def index():
    ticketform = forms.TicketForm()
    title = "airTicket"
    # back_to_home = redirect(url_for('index'),302)
    return render_template('index.html', title=title)


@app.route('/emirates')
def emirates():
    title = "Emirates Airlines"
    return render_template('emirates_ticket.html', title=title)


@app.route('/qatar2', methods=['GET', 'POST'])
def qatar2():
    title = "Qatar Airlines"
    # qatar_ticket = forms.TicketForm(request.form)
    if request.method == 'POST':
        qatar = mongo.db.qatar
        data = request.form.to_dict()
        qatar.insert({'qatar2': data})
        print('JSON', data)
    return render_template('qatar2.html', title=title)


@app.route('/singapore', methods=['GET', 'POST'])
def singapore():
    title = "Singapore Airlines"
    if request.method == 'POST':
        singapore = mongo.db.singapore
        data = request.form.to_dict()
        singapore.insert({'singapore':data})
        print('JSON', data)
    return render_template('singapore_ticket.html', title=title)
# test function
# @app.route('/params')
# def parameters():
#     param = request.args.get('param1', 'parametro')
#     return 'hello params is {}'.format(param)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
