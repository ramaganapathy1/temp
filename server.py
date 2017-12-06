from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)
import mysql.connector as mariadb
import datetime

# UTILITY FUNCTIONS
def decode(var):
        if isinstance(var,bytearray):
                return var.decode('utf-8')
        if isinstance(var,datetime.date):
                return str(var)
        if isinstance(var,int):
                return var
        if isinstance(var,str):
                return var
        return

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], map(decode,row)))
            for row in cursor.fetchall()]

########################################################

@app.route('/')
def index():
    #res=[[['Title 1','Description 1','date'],['Title2','Description 2','date'],['Title3','Description 3','date'],['Title 4','Description 4','date']],[['image1','News headline','news body'],['image2','News Headline 2','News body'],['image2','News Headline 2','News body']],[['person1Image','Name1'],['person2Image','Name2'],['person3Image','Name3']]]
    ann_res = []
    news_res = []
    emp_res = []
    res = []
    mariadb_connection = mariadb.connect(host="128.199.81.127",user='sree', password='asdf1234asdf', database='landt')

    cursor = mariadb_connection.cursor(prepared = True)
    cursor.execute("select subject,announcement,date from announcements ORDER BY id DESC LIMIT 4")
    all_announcement = dictfetchall(cursor)


    cursor.execute("select subject,content,iloc from news ORDER BY id DESC LIMIT 4")
    all_news = dictfetchall(cursor)


    cursor.execute("SELECT name,iloc from employee")
    all_employee = dictfetchall(cursor)
    cursor.close()
    mariadb_connection.close()

    for i in all_announcement:
        temp = []
        temp.append(str(i['subject']))
        temp.append(str(i['announcement']))
        temp.append(str(i['date']))
        ann_res.append(temp)

    for i in all_news:
        temp = []
        temp.append(str(i['iloc']))
        temp.append(str(i['subject']))
        temp.append(str(i['content']))
        news_res.append(temp)

    for i in all_employee:
        temp = []
        temp.append(str('iloc'))
        temp.append(str('name'))
        emp_res.append(temp)

    res.append(ann_res)
    res.append(emp_res)
    res.append(emp_res)

    #return str(res)

    return render_template('index.html',li=res)

@app.route('/campusInfo',methods=['GET'])
def info():
    return render_template('campusinfo.html')

@app.route('/ese',methods=['GET'])
def ese():
    return render_template('ese.html')

@app.route('/gen',methods=['GET'])
def gen():
    return render_template('gen.html')

@app.route('/ltvl',methods=['GET'])
def ltvl():
    return render_template('ltvl.html')

@app.route('/pdc',methods=['GET'])
def pdc():
    return render_template('pdc.html')

@app.route('/pmsc',methods=['GET'])
def pmsc():
    return render_template('pmsc.html')

@app.route('/sddc',methods=['GET'])
def sddc():
    return render_template('sddc.html')

@app.route('/nammaKovai',methods=['GET'])
def nammakovai():
    return render_template('sddc.html')


if __name__ == '__main__':
    app.run(debug = True)
