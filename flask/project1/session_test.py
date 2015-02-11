#!/usr/bin/env python
from flask import Flask,render_template,redirect,url_for,abort,escape,request,session
app = Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
		<form action="" method="POST" >
			<p><input type=text name=username></p>
			<p><input type=submit value=Login></p>
		</form>
		'''

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

app.secret_key = 'fsadfasdfsdfsdfasfasdfasfd'

@app.route('/error_401')
def error_401():
	abort(401)
	return '401'


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
