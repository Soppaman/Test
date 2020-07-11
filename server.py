
# To activate type 'Scripts\activate' in cmd
# > python server.py
# > set FLASK_APP=server.py
# > flask run
# > debug mode: set FLASK_ENV=development

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def myhome():
	return render_template('index.html')	

@app.route('/<string:page_name>')
def htmlPage(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode = 'a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
	
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
	   try:
		   data = request.form.to_dict()
		   #write_to_file(data)
		   write_to_csv(data)
		   return redirect ('/submit.html')
	   except:
		   return 'Did not save to database'
	else:
	   return 'something wrong'

'''
@app.route('/')
def myhome():
	return render_template('index.html')

@app.route('/index.html')
def myhome2():
	return render_template('index.html')

@app.route('/about.html')
def about():
	return render_template('about.html')
	
@app.route('/works.html')
def works():
	return render_template('works.html')	
	
@app.route('/work.html')
def work():
	return render_template('work.html')	
	
@app.route('/contact.html')
def contact():
	return render_template('contact.html')		

@app.route('/components.html')
def components():
	return render_template('components.html')		
#components.html	
'''