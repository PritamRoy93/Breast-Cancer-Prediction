from flask import Flask,render_template,request
import numpy as np
import joblib

app = Flask(__name__)

model=joblib.load("breast_cancer_prediction.pkl")

@app.route("/")
def home():   
    return render_template("index.html")


@app.route("/course")
def course(): 
    return render_template("course.html")

@app.route("/result",methods=['POST'])
def result():
    name=request.form['name']
    frm1=float(request.form['f1'])
    frm2=float(request.form['f2'])
    frm3=float(request.form['f3'])
    frm4=float(request.form['f4'])
    frm5=float(request.form['f5'])
    frm6=float(request.form['f6'])
    frm7=float(request.form['f7'])
    frm8=float(request.form['f8'])
    frm9=float(request.form['f9'])
    frm10=float(request.form['f10'])
    frm11=float(request.form['f11'])
    frm12=float(request.form['f12'])
    frm13=float(request.form['f13'])
    frm14=float(request.form['f14'])
    frm15=float(request.form['f15'])
    frm16=float(request.form['f16'])
    frm17=float(request.form['f17'])
    frm18=float(request.form['f18'])
    frm19=float(request.form['f19'])
    frm20=float(request.form['f20'])
    frm21=float(request.form['f21'])
    frm22=float(request.form['f22'])
    frm23=float(request.form['f23'])
    frm24=float(request.form['f24'])
    frm25=float(request.form['f25'])
    frm26=float(request.form['f26'])
    frm27=float(request.form['f27'])
    frm28=float(request.form['f28'])
    frm29=float(request.form['f29'])
    frm30=float(request.form['f30'])
    """"
    outp=frm30 ,fr1=frm1,fr2=frm2,fr3=frm3,fr4=frm4,fr5=frm5,fr6=frm6,fr7=frm7,fr8=frm8,fr9=frm9,fr10=frm10,fr11=frm11,fr12=frm12,fr13=frm13,fr14=frm14,fr15=frm15,fr16=frm16,fr17=frm17,fr18=frm18,fr19=frm19,fr20=frm20,fr21=frm21,fr22=frm22,fr23=frm23,fr24=frm24,fr25=frm25,fr26=frm26,fr27=frm27,fr28=frm28,fr29=frm29"""
    features=np.array([[frm1,frm2,frm3,frm4,frm5,frm6,frm7,frm8,frm9,frm10,frm11,frm12,frm13,frm14,frm15,frm16,frm17,frm18,frm19,frm20,frm21,frm22,frm23,frm24,frm25,frm26,frm27,frm28,frm29,frm30]])
    output=model.predict(features)
    if output[0]==1:
         return render_template("result.html",name=name,outp=", you have cancer but there are no reason to worry,take proper treatment as per doctor's advice and you will be fine.")
    else:
        return render_template("result.html",pname=name,a=", don't be afraid,you are fine,nothing happened to you,but take care of ypurself.")
    """
    features=np.array([frm1,frm2,frm3,frm4,frm5,frm6,frm7,frm8,frm9,frm10,frm11,frm12,frm13,frm14,frm15,frm16,frm17,frm18,frm19,frm20,frm21,frm22,frm23,frm24,frm25,frm26,frm27,frm28,frm29,frm30])
    output=model.predict([features])
    return render_template("result.html",a=name,b=age)"""


@app.route("/login")
def contact():
   
    return render_template("login.html")

@app.route("/signin",methods=['POST'])
def signin():
    n=request.form['nm']
    a=request.form['ag']
    return render_template("signin.html",Name=n,Age=a)

@app.route("/forgetpassword")
def forgetpassword():
   
    return render_template("forgetpassword.html")

@app.route("/forgetusername")
def forgetusername():
   
    return render_template("forgetusername.html")

app.run(debug=True)
