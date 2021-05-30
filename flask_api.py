from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import os
import flasgger
from flasgger import Swagger
app=Flask(__name__)
Swagger(app)


pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
   return "Welcome All"
@app.route('/predict',methods=["GET"])
def predictFromInput():

   """Checking heart attack prediction by user inputs
   This is using docstrings for specifications. (0:Female, 1: Male)
   ---
   parameters:
     - name: age
       in: query
       type: number
       required: true
     - name: sex
       in: query
       type: bool
       required: true
     - name: cp
       in: query
       type: number
       required: true
     - name: trtbps
       in: query
       type: number
       required: true
     - name: chol
       in: query
       type: number
       required: true
     - name: fbs
       in: query
       type: number
       required: true
     - name: restecg
       in: query
       type: number
       required: true
     - name: thalachh
       in: query
       type: number
       required: true
     - name: exng
       in: query
       type: number
       required: true
     - name: oldpeak
       in: query
       type: float
       required: true
     - name: caa
       in: query
       type: number
       required: true
     - name: thall
       in: query
       type: number
       required: true
   responses:
      200:
         description: The output values

   """
   age=request.args.get('age')
   sex=request.args.get('sex')
   cp = request.args.get('cp')
   trtbps  = request.args.get('trtbps')
   chol = request.args.get('chol')
   fbs = request.args.get('fbs')
   restecg = request.args.get('restecg')
   thalachh = request.args.get('thalachh')
   exng = request.args.get('exng')
   oldpeak = request.args.get('oldpeak')
   slp  = request.args.get('slp')
   caa = request.args.get('caa')
   thall = request.args.get('thall')
   prediction = classifier.predict([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh, exng, oldpeak, slp, caa, thall]])
   #127.0.0.1:5000/predict?age=63&sex=1&cp=3&trtbps=145&chol=233&fbs=1&restecg=0&thalachh=150&exng=0&oldpeak=2&slp=0&caa=0&thall=1
   return "The prediction is " + str(prediction)
@app.route('/predict_file',methods=["POST"])
def predictFromCSV():

   """Checking heart attack prediction by file
   This is using docstrings for specifications.
   ---
   parameters:
     - name: file
       in: formData
       type: file
       required: true
   responses:
       200:
           description: The output values

   """
   data_test = pd.read_csv(request.files.get('file')) #testData.csv
   predictions = classifier.predict(data_test)
   return "The predictions are: "+ str(list(predictions))
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)