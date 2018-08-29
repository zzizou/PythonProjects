from flask import Flask,render_template,request
from readcsv import read
import os
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barcapage', methods=['GET'])
def barcapage():
    data=read()
    return render_template('barca.html',hundata=data)

if __name__=="__main__":
    app.run(debug=True)
