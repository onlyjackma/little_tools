from flask import Flask,url_for
app = Flask(__name__)
@app.route('/')
def index():pass

@app.route('/login')
def login():pass

@app.route('/user/<username>')
def profile(username):pass

with app.test_request_context():
	print url_for('index')
	print url_for('login')
	print url_for('login',next='/')
	print url_for('profile',username='John Doe')
	print url_for('profile',username='John Doe',id=22)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=3333,debug=True)
