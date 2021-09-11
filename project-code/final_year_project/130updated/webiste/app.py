from flask import Flask, render_template, request, session, url_for, redirect, jsonify,make_response,flash
import pymysql

from werkzeug.utils import secure_filename
import pandas as pd
import os
from tensorflow import keras
import os
import random as rn
import numpy as np
import tensorflow as tf

from pprint import pprint as pp

import tensorflow 
from tensorflow import keras

import sklearn


from sklearn.model_selection import train_test_split
import pickle

filename1='Logistic_regression.sav'
loaded_model = pickle.load(open(filename1, 'rb'))
filename2='nb.sav'
loaded_model1= pickle.load(open(filename2, 'rb'))
filename3='rf.sav'
loaded_model2=  pickle.load(open(filename3, 'rb'))
filename4='SVM.sav'
loaded_model3=  pickle.load(open(filename4, 'rb'))
filename5='dt.sav'
loaded_model4=  pickle.load(open(filename5, 'rb'))
filename6='ada.sav'
loaded_model5=  pickle.load(open(filename6, 'rb'))
filename7='ann_new.hp5'
loaded_model6= tensorflow.keras.models.load_model(filename7)
filename8='mlp_new.sav'
loaded_model7=  pickle.load(open(filename8, 'rb'))


def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="cropiot")
    return connection

def dbClose():
    dbConnection().close()
    return

app=Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def house():
    return render_template('index.html')



@app.route('/user.html')
def user():
    return render_template('user.html')
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))
@app.route('/register.html', methods=["GET","POST"])
def register():
    if request.method == "POST":
        try:
            status=""
            name = request.form.get("Name")
            Email = request.form.get("Email")
            pass1 = request.form.get("pass1")
            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM userdetails WHERE email = %s', (Email))
            res = cursor.fetchone()
            #res = 0
            if not res:
                sql = "INSERT INTO userdetails (name, email, password) VALUES (%s, %s, %s)"
                val = (name, Email, pass1)
                print(sql," ",val)
                cursor.execute(sql, val)
                con.commit()
                status= "success"
                return redirect(url_for('login'))
            else:
                status = "Already available"
            #return status
            return redirect(url_for('index'))
        except:
            print("Exception occured at user registration")
            return redirect(url_for('index'))
        finally:
            dbClose()
    return render_template('register.html')

@app.route('/login.html', methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST":
        session.pop('user',None)
        mailid = request.form.get("Name")
        password = request.form.get("Pas")
        #print(mobno+password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM userdetails WHERE email = %s AND password = %s', (mailid, password))
        #a= 'SELECT * FROM userdetails WHERE mobile ='+mobno+'  AND password = '+ password
        #print(a)
        #result_count=cursor.execute(a)
        result = cursor.fetchone()
        if result_count>0:
            print(result_count)
            session['userid']= result[0]
            session['user'] = mailid
            return render_template("home.html")
        else:
            print(result_count)
            msg = 'Incorrect username/password!'
            return msg
        #dbClose()
    return  render_template('login.html')
@app.route('/home.html')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return render_template("user.html")
@app.route('/image.html', methods=["GET","POST"])
def image():
    if 'user' in session:
        dstfolder='static/pie_chart/new.png'
        return render_template('image.html', user_image = dstfolder,user=session['user'])
    return render_template("user.html")
@app.route('/prediction', methods=["GET","POST"])
def prediction():
    if 'user' in session:
        if request.method == "POST":
            temp= request.form.get("Name")
            humid= request.form.get("Name1")
            moist=request.form.get("Name2")
            light= request.form.get("Name3")
            height= request.form.get("Name4")
            width= request.form.get("Name5")
            temp=float(temp)
            humid=float(humid)
            moist=float(moist)
            light=float(light)
            height=float(height)
            width=float(width)
            growth=height/width
            new=[]
            array=[]
            new.append(temp)
            new.append(humid)
            new.append(moist)
            new.append(light)
            new.append(growth)
            myprediction = loaded_model.predict([np.array(new)])
            print(myprediction)
            if myprediction[0] == '1':
                a='Crop Yeild Possibility is there'
                #array.append(myprediction[0])
                array.append(1)
                print(a)
            else:
                b="There is No Crop Yeild Possible"
                array.append(0)
                #array.append(myprediction[0])
                print(b)
            myprediction1= loaded_model1.predict([np.array(new)])
            if myprediction1[0] == '1':
                c="Crop Yeild Possibility is there"
                array.append(1)
                #array.append(myprediction1[0])
                print(c)
            else:
                d="There is No Crop Yeild Possible"
                array.append(0)
                #array.append(myprediction1[0])
                print(d)
            myprediction2= loaded_model2.predict([np.array(new)])
            if myprediction2[0]== '1':
                c="Crop Yeild Possibility is there"
                array.append(1)
                #array.append(myprediction2[0])
                print(c)
            else:
                d="There is No Crop Yeild Possible"
                array.append(0)
                #array.append(myprediction2[0])
                print(d)
            myprediction3= loaded_model3.predict([np.array(new)])
            if myprediction3== '1':
                e="Crop Yeild Possibility is there"
                array.append(1)
                #array.append(myprediction3[0])
                print(e)
            else:
                f="There is No Crop Yeild Possible"
                array.append(0)
                #array.append(myprediction3[0])
                print(f)
            myprediction4= loaded_model4.predict([np.array(new)])
            if myprediction4== 1:
                g="Crop Yeild Possibility is there"
                array.append(1)
                #array.append(myprediction4[0])
                print(g)
            else:
                h="There is No Crop Yeild Possible"
                array.append(0)
                #array.append(myprediction4[0])
                print(h)
            myprediction5= loaded_model5.predict([np.array(new)])
            if myprediction5=='1':
                #array.append(myprediction5[0])
                print("Crop Yeild Possibility is there")
                array.append(1)
            else:
                #array.append(myprediction5[0])
                array.append(0)
                print("There is No Crop Yeild Possible")
            #print(new)
            myprediction6 = loaded_model6.predict([(new)])
            #print(myprediction6)
            if myprediction6[0][0]==1:
                array.append(1)
                #array.append(str(myprediction6[0][0]))
                print("Crop Yeild Possibility is there")
            else:
                #array.append(str(myprediction6[0][0]))
                print("There is No Crop Yeild Possible")
                array.append(0)
            myprediction7= loaded_model7.predict([np.array(new)])
            print(myprediction7)
            if myprediction7==1:
                array.append(1)
                #array.append(str(myprediction7[0]))
                print("Crop Yeild Possibility is there")
            else:
                #array.append(str(myprediction7[0]))
                array.append(0)
                print("There is No Crop Yeild Possible")
            print(array)
            l=array.count(0)
            m=array.count(1)
            print(l)
            print(m)
            def most_frequent(List): 
                counter = 0
                num = List[0] 
                for i in List: 
                    curr_frequency = List.count(i) 
                    if(curr_frequency> counter): 
                        counter = curr_frequency 
                        num = i 
                return num 
            u=most_frequent(array)
            print(u)
              
            #print(u)
            if u==1:
                flash("Favourable conditions is there")
            else:
                flash("There is No Favourable conditions")
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO data(Temperature,Humidity,Light,Moisture,PlantHeight,Plantwidth,Growth,Outcome) VALUES (%s,%s, %s, %s, %s,%s,%s,%s)"
            val = (temp,humid,light,moist,height,width,growth,u)
            cursor.execute(sql, val)
            con.commit()



    
           
            
            #print(dict1)

            #print(gender)
            return render_template('prediction.html', user=session['user'],data1=l,data2=m)



    
           
            
            #print(dict1)

            #print(gender)
        return render_template('prediction.html', user=session['user'])
    return render_template("user.html")





if __name__=="__main__":
    app.run("0.0.0.0")