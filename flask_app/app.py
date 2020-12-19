# FLASK APP
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from wtforms.validators import ValidationError
from flask_table import Table, Col

# MODEL
import pickle
import os
import numpy as np

# WEB
import requests
from bs4 import BeautifulSoup

# UTIL
from utils.user_review_scraper import get_review_list
from utils.recommend import recommend

#### PREPARING THE MODEL

ABS_PATH = '/Users/adv/Programming/bgg_recs/ml/'
MODEL_PATH = ABS_PATH + 'pkl_objects/'
MODEL = MODEL_PATH + 'simple_svd.pkl'
model = pickle.load(open(MODEL, 'rb'))

#### RECOMMENDATIONS

#### OBJECTS

class UserForm(Form):
	username = TextAreaField('BGG username:',[validators.DataRequired()])

	def validate_username(form, field):
		page = requests.get(f'https://boardgamegeek.com/user/{field.data}')
		if page.text.find('User does not exist') > -1:
			raise ValidationError('User does not exist')

class ReviewTable(Table):
    bgg_id = Col('Game ID')
    game = Col('Game')
    rating = Col('Rating')
class Item(object):
	def __init__(self, game, bgg_id, rating):
		self.game = game
		self.bgg_id = bgg_id
		self.rating = rating

#### FLASK APP

app = Flask(__name__)

@app.route('/')
def index():
	form = UserForm(request.form)
	return render_template('first_app.html', form = form)

@app.route('/reviews', methods = ['POST'])
def get_reviews():
	form = UserForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['username']
		reviews = get_review_list(name)
		# order is not preserved
		reviews = [Item(*review.values()) for review in reviews]
		reviews = ReviewTable(reviews)
		return render_template('reviews.html', name = name, reviews = reviews)
	return render_template('first_app.html', form = form)

@app.route('/recommendations', methods = ['POST'])
def get_recommendations():
	form = UserForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['username']
		reviews = get_review_list(name)
		# reviews[0].keys() = ['game', 'bgg_game_id', 'score']
		recommendations = recommend(model, reviews)
		return render_template('recommendations.html', name = name, recommendations = recommendations)
	return render_template('first_app.html', form = form)

if __name__ == '__main__':
	app.run(debug = True)