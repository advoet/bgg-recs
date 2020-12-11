def generate_recommendations(model, ratings_by_user, game_id_list, n = 10):
	''' Generates a prediction score for games from game_id_list and returns the top n

	Args:
		model:
		ratings_by_user:
		game_id_list: a list of games to recommend from (e.g. top 100 bgg)
		n (int) : the number of predictions to generate
	'''
	preds = model.predict(game_id_list).reshape(-1)
	top_n_indices = (-preds).argsort()[:n]
	return [game_id_list[k] for k in top_n_indices]