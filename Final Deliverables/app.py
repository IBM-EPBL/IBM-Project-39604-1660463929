from flask import Flask,render_template, request
import pandas as pd
import numpy as np
import pickle
import os


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/') #rendering the html templates
def home():
     return render_template("home.html")
 
@app.route('/predict')
def predict():
    gender =[ {'gender': 'Female'}, {'gender': 'Male'}]
    mar = [{'married':'Yes'},{'married':'No'}]
    edu = [{'education':'Graduated'},{'education':'Not-Graduate'}]
    sel = [{'sel_emp':'Yes'},{'sel_emp':'No'}]
    pa = [{'property_area':'Urban'},{'property_area':'Semi-urban'},{'property_area':'Rural'}]
    return render_template("predict.html",gender = gender,mar = mar,edu = edu,sel=sel,pa=pa)

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        gen = request.form['Gender']
        print(gen)
        if gen == 'Female':
            gen = 0
        else:
            gen = 1
        mar = request.form['Married']
        print(mar)
        if mar == 'Yes':
            mar = 1
        else:
            mar= 0
        dept = request.form['Dependents']
        print(dept)
        edu = request.form['Education']
        print(edu)
        if edu == 'Graduated':
            edu = 0
        else:
            edu = 1
        sel = request.form['Self_Employed']
        print(sel)
        if sel == 'Yes':
            sel = 0
        else:
            sel = 1

        ai = request.form['AI']
        print(ai)
        ci = request.form['CI']
        print(ci)
        la = request.form['LA']
        print(la)
        lat = request.form['LAT']
        print(lat)
        ch = request.form['CH']
        print(ch)
        pa = request.form['Property_Area']
        print(pa)
        if pa =='Rural':
            pa = 0
        elif pa == 'Semi_urban':
            pa = 1
        else:
            pa = 2
        print(gen,mar,dept,edu,sel,ai,ci,la,lat,ch,pa)
        input_feature=[gen,mar,dept,edu,sel,ai,ci,la,lat,ch,pa]
        input_feature=[np.array(input_feature)]
        print(input_feature)
        names= ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'Applicant_Income', 'Co-applicant_Income', 'Loan_Amount', 
            'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        print(input_feature)
        data =pd.DataFrame(input_feature,columns=names)
        print(data)
        prediction=model.predict(data)
        print(prediction)
        prediction=int(prediction)
        print(type(prediction))
        if(prediction==0):
            return render_template("submit.html",result="Loan will not be Approved")
        else:
            return render_template("submit.html",result="Loan will be Approved") 
     
 
if __name__== '__main__':
    app.run()
    
