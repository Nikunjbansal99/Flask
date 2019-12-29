from flask import Flask
app = Flask(__name__)

@app.route('/python')
def hello_python():
	return 'Hello python'
#Its not work on http://127.0.0.1:5000/python/

@app.route('/flask')
def hello_flask():
	return 'Hello flask'
#Its not work on http://127.0.0.1:5000/flask/

if __name__ == '__main__':
	app.run(debug=True)