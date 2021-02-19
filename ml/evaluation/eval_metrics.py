import numpy as np
import pandas as pd

from sklearn.metrics import (
	mean_squared_error,
	mean_absolute_error,
	
)
from math import sqrt


def _f1_score(precision, recall):
	return 2 * (precision * recall) / (precision + recall)

def rmse(predictied, actual):
	return sqrt(mean_squared_error(predicted, actual))

def mae(predicted, actual):
	return mean_absolute_error(predicted, actual)

