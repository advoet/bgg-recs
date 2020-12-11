import pandas as pd
import pickle

DATA_PATH = '..'
DATA = '/bgg-15m-reviews.csv'

if __name__ == '__main__':

	df = pd.read_csv(DATA_PATH + DATA, index_col = 0)
	df = df[df.user.notna()]
	df.drop(columns = 'comment')
	df['user_id'] = df.groupby('user').ngroup()

	## CLEANED FULL SET
	df.to_csv(DATA_PATH + '/bgg-15m-clean.csv')

	## RANDOM SAMPLE
	m_sampled = df.sample(n = 10**6, random_state = 42)
	m_sampled.to_csv(DATA_PATH + '/bgg-1m-sampled.csv')

	## TOP REVIEWERS
	review_counts = df.user.value_counts(sort = True, ascending = False)
	
	top_reviewers = []
	total = 0
	for name, count in review_counts.items():
		if total > 10**6:
			break
		top_reviewers.append(name)
		total += count

	m_top_reviewers = df[df.user.isin(top_reviewers)]
	m_top_reviewers.to_csv(DATA_PATH + '/bgg-1m-top-reviewers.csv')


	# TO-DO: Sample but make sure each game is represented