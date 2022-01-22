from models import Movie
from flask import Flask,request,redirect,url_for
from flask.helpers import url_for
from flask.templating import render_template

import database as db
import os

app = Flask(__name__)

@app.route('/')
def index():
    movielist = db.all()
    return render_template('index.html',movielist=movielist)

@app.route('/movieform')
def empform():
    movieobj = Movie(0,"","",0,"")
    return render_template('movieform.html',movieobj=movieobj,action="add")

@app.route("/delete/<int:mid>")
def empdelete(mid):
    db.delete(mid)
    print("Delete ",mid)
    return redirect(url_for('index'))

@app.route('/edit/<int:mid>')
def empeditform(mid):
    movieobj = db.get(mid)
    return render_template('movieform.html',movieobj=movieobj,action='update')

@app.route('/update',methods=['POST'])
def empupdate():
    mid = int(request.form.get('mid'))
    mname = request.form.get('mname')
    mdirector = request.form.get('mdirector')
    mboxoffice = request.form.get('mboxoffice')
    # code for image

    print(request) 
    imgfile = request.files['mimg']
    
    imgname = imgfile.filename
    if imgname == '':
        imgname=db.get(mid).mimg
    else:
        path = os.path.join('static/uploadedimg',imgname)
        imgfile.save(path)  

    
    db.update(mid,mname,mdirector,mboxoffice,imgname)
    return redirect(url_for('index'))

@app.route('/add',methods=['POST'])
def empadd():
    mname = request.form.get('mname')
    mdirector = request.form.get('mdirector')
    mboxoffice = request.form.get('mboxoffice')
    # code for image
    imgfile = request.files['mimg']
    mimg = imgfile.filename  
    path = os.path.join('static/uploadedimg',mimg)
    imgfile.save(path) 

    db.add(mname,mdirector,mboxoffice,mimg)
    return redirect(url_for('index'))




if __name__=='__main__':
    app.run(debug=True)