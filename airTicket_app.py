#!/usr/bin/python3.7
from flask import Flask
from flask import make_response
from flask_mail import Message
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import render_template, redirect
from flask import request
from flask import Response
from flask import url_for
from flask_wtf import CSRFProtect
from flask_wkhtmltopdf import Wkhtmltopdf
from getpass import getuser
import pdfkit
# import forms


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'my_secret_key'
app.config['MONGO_DBNAME'] = 'airTicketdb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/airTicketdb"
mongo = PyMongo(app)
csrf_token = CSRFProtect(app)
wkhtmltopdf = Wkhtmltopdf(app)


@app.route('/')
def index():
    # ticketform = forms.TicketForm()
    title = "airTicket"
    # back_to_home = redirect(url_for('index'),302)
    return render_template('index.html', title=title)

@app.route('/ana', methods=["GET", "POST"])
def ana():
    title = "Ana Airlines"
    if request.method == "POST":
        ana = mongo.db.ana
        data = request.form.to_dict()
        ana.insert({"ana": data})
        print("JSON", data)
    return render_template('ana.html', title=title)

@app.route('/cathay', methods=["GET", "POST"])
def cathay():
    title = "Cathay Airlines"
    if request.method == "POST":
        cathay = mongo.db.cathay
        data = request.form.to_dict()
        cathay.insert({"cathay": data})
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
    title = "Eva Airlines"
    if request.method == 'POST':
        eva = mongo.db.eva
        data = request.form.to_dict()
        eva.insert({'eva': data})
        print('JSON', data)
    return render_template('eva.html', title=title)

@app.route('/qatar', methods=['GET', 'POST'])
def qatar():
    title = "Qatar Airlines"
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
        singapore.insert({'singapore': data})
        print('JSON', data)
    return render_template('singapore.html', title=title)

# @app.route('/preview', methods=['GET','POST'])
# def preview():
#     if request.method == 'POST':
#         result = request.form
#         pdf = pdf_gen('127.0.0.1:5000:/preview.html')
#         return render_template("preview.html", result=result)

@app.route("/preview")
def preview():
    data_query = mongo.db.qatar
    # datalist = [data for data in data_query.find()]
    # datalist = datalist[0]["qatar"]
    data_arr = []
    for data in data_query.find():
        print(data['_id'])
        data['qatar']['id']=data['_id']
        data_arr.append(data["qatar"])
        endData = render_template("preview.html", data=data_arr)
    return endData

@app.route("/<id>")
def printer(id):
    print(id)
    data_query = mongo.db.qatar
    data = data_query.find_one({'_id':ObjectId(id)})
    print(data)
    # pdf = pdf_gen("http://localhost:5000/{}".format(id))
    endData = render_template("printer.html", data=data['qatar'])
    return endData

#pdfkit
def pdf_gen(url):
    url = url
    filename = '{}.pdf'.format(getuser())
    # pdfconf = {
    #     'page-size': 'A4',
    #     'margin-top': '0.75in',
    #     'margin-right': '0.75in',
    #     'margin-bottom': '0.75in',
    #     'margin-left': '0.75in',
    #     }
    pdfkit.from_url(url, filename)
    pdfDownload = open(filename, 'rb').read()
    return Response(pdfDownload, mimetype='application/pdf',
                    headers={
                        "Content-disposition": "attachment; filename=" + filename,
                        "Content-type": "application/force-download"
                    })

#Wkhtmltopdf
# pdf = Wkhtmltopdf.render_template_to_pdf('qatar.html',
#                                             download=True,
#                                             save=False,
#                                             param=data)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
