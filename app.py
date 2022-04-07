# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, Response
import pandas as pd
import requests
from flask import Flask, render_template, request, url_for, flash, redirect

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/model', methods=['GET', 'POST'])
def model():
    data = pd.read_csv("data/final-data.csv")
	
    # For rendering results on HTML GUI
    marathi_sentence = request.form.get("emotion_calculator")
    # print(marathi_sentence)
	# मी काम करतोय
    inputstr=[marathi_sentence]

    if (inputstr in data['comment'].values):
        print()
    
    rslt_df = data[data['comment'].isin(inputstr)]
	# rslt_df['comment']
	# rslt_df['rating']
	# rslt_df['comment marathi']
	# rslt_df['stop word removed comment']
	
    return render_template("model.html", result=rslt_df.to_dict('list'))

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()