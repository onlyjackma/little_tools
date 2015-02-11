from flask import Flask,request
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return "the request method is post"
	else:
		return "the request method is get"
		
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
