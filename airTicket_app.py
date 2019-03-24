#!/usr/bin/python3.6
from flask import Flask
from flask_mail import Message
from flask_pymongo import PyMongo
from flask import render_template, redirect
from flask import request
from flask import url_for
from flask_wtf import CSRFProtect
# import forms


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'my_secret_key'
app.config["MONGO_URI"] = "mongodb://localhost:27017/airTcketdb"
mongo = PyMongo(app)
csrf_token = CSRFProtect(app)


@app.route('/')
def index():
    # ticketform = forms.TicketForm()
    title = "airTicket"
    # back_to_home = redirect(url_for('index'),302)
    return render_template('index.html', title=title)

@app.route('/ana', methods=["GET", "POST"])
def ana():
    title = "Emirates Airlines"
    if request.method == "POST":
        emirates = mongo.db.emirates
        data = request.form.to_dict()
        emirates.insert({"ana": data})
        print("JSON", data)
    return render_template('ana.html', title=title)

@app.route('/cathay', methods=["GET", "POST"])
def cathay():
    title = "Emirates Airlines"
    if request.method == "POST":
        emirates = mongo.db.emirates
        data = request.form.to_dict()
        emirates.insert({"cathay": data})
        print("JSON", data)
    return render_template('cathay.html', title=title)

@app.route('/emirates', methods=["GET", "POST"])
def emirates():
    title = "Emirates Airlines"
    if request.method == "POST":
        emirates = mongo.db.emirates
        data = request.form.to_dict()
        emirates.insert({"emirates": data})
        print("JSON", data)
    return render_template('emirates.html', title=title)

@app.route('/eva', methods=['GET', 'POST'])
def eva():
    title = "Singapore Airlines"
    if request.method == 'POST':
        singapore = mongo.db.singapore
        data = request.form.to_dict()
        singapore.insert({'eva':data})
        print('JSON', data)
    return render_template('eva.html', title=title)

@app.route('/qatar', methods=['GET', 'POST'])
def qatar():
    title = "Qatar Airlines"
    # qatar_ticket = forms.TicketForm(request.form)
    if request.method == 'POST':
        qatar = mongo.db.qatar
        data = request.form.to_dict()
        qatar.insert({'qatar': data})
        print('JSON', data)
    return render_template('qatar.html', title=title)

@app.route('/singapore', methods=['GET', 'POST'])
def singapore():
    title = "Singapore Airlines"
    if request.method == 'POST':
        singapore = mongo.db.singapore
        data = request.form.to_dict()
        singapore.insert({'singapore':data})
        print('JSON', data)
    return render_template('singapore.html', title=title)

# test function
# @app.route('/params')
# def parameters():
#     param = request.args.get('param1', 'parametro')
#     return 'hello params is {}'.format(param)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
