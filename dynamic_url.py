from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
	return 'Hello %s!' % name
#return name
#app.add_url_rule()

@app.route('/employee/<int:employeeID>')
def employee_detail(employeeID):
	return 'Employee Number %d' % employeeID
#return int

@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number %f' % revNo
#return float

if __name__ == '__main__':
	app.run(debug=True)