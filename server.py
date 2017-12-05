from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    res=[[['Title 1','Description 1','date'],['Title2','Description 2','date'],['Title3','Description 3','date'],['Title 4','Description 4','date']],[['image1','News headline','news body'],['image2','News Headline 2','News body'],['image2','News Headline 2','News body']],[['person1Image','Name1'],['person2Image','Name2'],['person3Image','Name3']]]
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
    app.run()
