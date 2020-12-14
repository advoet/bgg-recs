from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from wtforms.validators import ValidationError

import pickle
import os
import numpy as np

import requests
from bs4 import BeautifulSoup

#### PREPARING THE MODEL

ABS_PATH = '/Users/adv/Programming/bgg_recs/ml/'
MODEL_PATH = ABS_PATH + 'pkl_objects/'
MODEL = MODEL_PATH + 'simple_svd.pkl'
model = pickle.load(open(MODEL, 'rb'))



#### RECOMMENDATIONS

recommend_from = None
BGG_ERROR_MESSAGE = 'Error: User does not exist'


#### FLASK APP

app = Flask(__name__)

class UserForm(Form):
	username = TextAreaField('BGG username:',[validators.DataRequired()])

	def validate_username(form, field):
		page = requests.get('https://boardgamegeek.com/user/{username}')
		if page.text.find('User does not exist') > -1:
			raise ValidationError('User does not exist')

@app.route('/')
def index():
	form = UserForm(request.form)
	return render_template('first_app.html', form = form)

@app.route('/hello', methods = ['POST'])
def hello():
	form = UserForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['sayhello']
		return render_template('hello.html', name = name)
	return render_template('first_app.html', form = form)

if __name__ == '__main__':
	app.run(debug = True)