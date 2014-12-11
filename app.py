#!/usr/bin/python
from flask import Flask, render_template
import crime_stats as cs
import pandas as pd
import random
import cStringIO

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/coolmap')
def coolmap():
	return render_template('chiCrimesCircles.html')

@app.route('/fact')
def fact():
	df = cs.get_df()
	maxcrime = cs.most_dangerous_block(df)
	facts = [cs.most_dangerous_block(df), cs.worst_place(df), cs.domestic(df), cs.community(df), cs.theft(df)]
	fact_num = random.randint(0,4)
	if fact_num == 0 or fact_num == 2: 
		return render_template('fact.html', fact=facts[fact_num])
	if fact_num == 1:
		return render_template('fact.html', fact=facts[fact_num], graph=1)
	if fact_num == 3:
		return render_template('fact.html', fact=facts[fact_num], graph=3)
	if fact_num == 4:
		return render_template('fact.html', fact=facts[fact_num], graph=4)


@app.route('/mypng')
def mypng(graph):
	graph = worst_place_graph(df)
	f = cStringIO.cStringIO()
	graph.savefig(f, format='png')
	data = f.seek(0)
	return send_file(data, mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True)


	




	