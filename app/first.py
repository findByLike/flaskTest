'''
Created on 2017年6月18日

@author: Administrator
'''
from flask import Flask, render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        flash('you get it')
        return redirect(url_for('index')) 
    return render_template('index.html',form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    
    print(name)
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if(__name__ == '__main__'):
    app.run(debug=True)
