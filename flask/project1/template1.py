#!/usr/bin/env python
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/hello/<name>')
@app.route('/')
def hello_world(name=None):
	return render_template('hello.html',name=name)

@app.route('/user/<username>')
def show_user_name(username):
	return "User is %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id
@app.route('/projects/')
def projects():	
	return "The project page"

@app.route('/about')
def about():
	return 'The about page'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
