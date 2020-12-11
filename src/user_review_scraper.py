import requests
import re
from bs4 import BeautifulSoup

# TODO: error checking, private profiles
def get_review_list(username):
	# returns a list of (game name, bgg game id, user rating) for a given bgg username

	URL = f'https://boardgamegeek.com/collection/user/{username}'
	params = {
		'rated': 1,
	}

	with requests.get(URL, params = params) as page:
		soup = BeautifulSoup(page.content, 'html.parser')
		games = soup.findAll('a', href = re.compile('^/boardgame/'))
		bgg_ids = [game['href'].split('/')[2] for game in games]
		game_names = [game.text for game in games]
		ratings = [rating.text for rating in soup.findAll(class_ = 'ratingtext')]

	return list(set(zip(game_names, bgg_ids, ratings)))

def main():
	username = 'ninjablaster'
	print(get_review_list(username))

if __name__ == '__main__':
	main()