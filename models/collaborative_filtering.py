import os
import surprise
import pandas as pd
import pickle

DATA_PATH = '../data/'
DATA = 'bgg-15m-reviews.csv'

def load_data():
	return pd.read_csv(os.path.join(DATA_PATH, DATA))


def pre_process(data):
	data = data[data.user.notna()]
	data = data[['user', 'name', 'rating']]
	reader = surprise.Reader(rating_scale = (data.rating.min(), data.rating.max()))
	return surprise.Dataset.load_from_df(data, reader)

# PARAMETERS
N_FACTORS = 1 # 30
N_EPOCHS = 1 # 20 

if __name__ == '__main__':
	data = pre_process(load_data())
	model = surprise.SVD(n_factors = N_FACTORS, n_epochs = N_EPOCHS, verbose = True)
	output = surprise.model_selection.cross_validate(model, data, verbose = True)
	# SAVE MODEL
	file_name = '../pkl_objects/simple_svd.pkl'
	with open(file_name, 'wb') as f:
		pickle.dump(model, f)

	print(f'Model saved to: {file_name}')