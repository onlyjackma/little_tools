#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello_world():
	return 'Hello world!'

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
	app.run(host='0.0.0.0',port=8080)
