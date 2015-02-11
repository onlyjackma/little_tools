from flask import Flask,url_for,request
app = Flask(__name__)
@app.route('/hello')
def hello():
	return '00'

with app.test_request_context('/hello',method='GET'):
	assert request.path == '/hello'
	assert request.method == 'GET'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
