import requests
import re
from bs4 import BeautifulSoup

# TODO: error checking, private profiles
def get_review_list(username):
	# returns a list of dictionaries with keys 'game', 'bgg_game_id', 'score'

	URL = f'https://boardgamegeek.com/collection/user/{username}'
	params = {
		'rated': 1,
	}

	page = requests.get(URL, params = params)
	soup = BeautifulSoup(page.content, 'html.parser')
	games = soup.findAll('a', href = re.compile('^/boardgame/'))
	bgg_ids = [game['href'].split('/')[2] for game in games]
	game_names = [game.text for game in games]
	ratings = [rating.text for rating in soup.findAll(class_ = 'ratingtext')]
	review_list = list(set(zip(game_names, bgg_ids, ratings)))
	keys = ('game', 'bgg_game_id', 'score')
	return [dict(zip(keys, review)) for review in review_list]

def main():
	username = 'ninjablaster'
	print(get_review_list(username))

if __name__ == '__main__':
	main()