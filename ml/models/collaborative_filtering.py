import os
import surprise
import pandas as pd
import pickle

ABS_PATH = '/Users/adv/Programming/bgg_recs/ml/'
PKL_PATH = ABS_PATH + 'pkl_objects/'
DATA_PATH = ABS_PATH + 'data/'
DATA = 'bgg-1m-top-reviewers.csv'

def load_data():
	return pd.read_csv(os.path.join(ABS_PATH, DATA_PATH, DATA))


def pre_process(data):
	data = data[['user', 'name', 'rating']]
	reader = surprise.Reader(rating_scale = (data.rating.min(), data.rating.max()))
	return surprise.Dataset.load_from_df(data, reader)

# PARAMETERS
N_FACTORS = 16 # 30
N_EPOCHS = 50 # 20 

if __name__ == '__main__':
	data = pre_process(load_data())
	model = surprise.SVD(n_factors = N_FACTORS, n_epochs = N_EPOCHS, verbose = True)
	output = surprise.model_selection.cross_validate(model, data, verbose = True)
	# SAVE MODEL
	file_name = PKL_PATH + 'simple_svd.pkl'
	with open(file_name, 'wb') as f:
		pickle.dump(model, f)

	print(f'Model saved to: {file_name}')