import os

def recommend(model, reviews, n = 10, candidates = 'top_100'):
	''' Generate a list of recommendations for a user
	
	Args:
		model: the model that generates a rating score
		reviews: a list of dictionary objects containing user reviews
			reviews[0].keys() = ['game', 'bgg_game_id', 'score'] 
		n (optional): the number of recommendations to generate
		candidates (optional): a criterion for which games to check 

	Returns:
		list: containing the name of top n games to recommend
	'''

	if candidates == 'top_100':
		DATA_PATH = os.getcwd() + '/data/'
		with open(DATA_PATH + 'top_100_ids.txt', 'r') as file:
			candidates = [int(id) for id in file.read().splitlines()]

	# After processing, candidates is a list of bgg_ids

	# Set up for the surprise model currently. predict(user id, item id)
	# User ID 60 is arbitrary, should do an embedding step first
	# Also it is overfit
	scores = [(ID, model.predict(60, ID)) for ID in candidates]
	scores.sort(key = lambda x: -x[1].est)
	best_n_ids = [x[0] for x in scores[:n]]
	print([(score[0], score[1].est) for score in scores])
	return best_n_ids
