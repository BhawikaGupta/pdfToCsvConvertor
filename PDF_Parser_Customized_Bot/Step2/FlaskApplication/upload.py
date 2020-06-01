from flask import render_template, request, redirect, url_for, flash, current_app, send_file, send_from_directory
from flask import Flask
import pymysql.cursors
import json
import flask
#from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os
from logging.config import dictConfig
import tabula
import pandas as pd
import numpy as np

import sqlalchemy

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='pdftocsv',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                             

engine = sqlalchemy.create_engine('mysql+mysqldb://root:password@localhost:3306/pdftocsv', echo = False)
#__name__ is a predefined python variable
app = Flask(__name__)
app.secret_key = 'my unobvious secret key'

UPLOAD_FOLDER = 'C:\\Software\\PDF_Parser_Customized_Bot\\Step2\\FlaskApplication'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def convertPdfToExcel(fileLocation):
    df = tabula.read_pdf(fileLocation, stream="True",pages='1')
    df = df[0].fillna('')
    df['2016.1'], df['Particulars.1'] = df['2016 Particulars'].str.split(" ",1).str
    df.drop(['Unnamed: 0'], axis = 1)
    df = df[['Particulars', '2015','2016.1','Particulars.1','Unnamed: 1','2015.1','2016']]
    df = df.fillna('')
    df = df.rename(columns={"Unnamed: 1": "", "2016.1": "2016", "2015.1":"2015", "Particulars.1":"Particulars"})
    csvLocation = fileLocation.replace(".pdf",".csv")
    df.to_csv (csvLocation, index = False, header=True)
    df = df.groupby(df.columns.values, axis=1).agg(lambda x: x.values.tolist()).sum().apply(pd.Series).T
    df['Particulars'].replace('', np.nan, inplace=True)
    df = df[~df['Particulars'].isnull()]
    df = df[['Particulars', '2015','2016']]
    df = df.rename(columns={"2015": "year2015", "2016": "year2016"})
    df.to_sql(name='balancesheet', con=engine, if_exists = 'replace')

@app.route("/")
def index():
    return render_template('index.html')
    
    
@app.route('/downloads/<path:filename>')
def download(filename):
    uploads = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)    

@app.route('/upload_file', methods=['POST'])
def ask_for_dir():
    if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            queryVariable = request.form.get('query_variable')
            queryYear = request.form.get('query_year')
            if file.filename.endswith(('pdf', 'PDF')):
                print(file.filename)
                app.logger.info('%s', file.filename)
                uploads = app.config['UPLOAD_FOLDER']
                location = os.path.join(uploads, file.filename) 
                file.save(location)
                convertPdfToExcel(location)
                cursor = connection.cursor() 
                sql = "SELECT year"+queryYear+" from balancesheet where Particulars like %s"
                print(sql)
                cursor.execute(sql, ("%"+queryVariable))
                rows = cursor.fetchone()
                print({queryVariable : rows["year"+queryYear]})
                connection.commit()
                csvName = file.filename.replace(".pdf",".csv")
                return render_template('index_success.html',rows={"Value of "+queryVariable+" in "+queryYear+" " : rows["year"+queryYear]},filename=csvName)
            else:
                flash('File name is incorrect')
                return render_template("index.html")
                
    #flash('File is not uploaded successfully')
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run()