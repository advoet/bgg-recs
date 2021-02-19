import numpy as numpy
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class MFNet(nn.Module):
	def __init__(self, n_users, n_features, n_items):
		super(MFNet, self).__init__()
		self.user_embedding = nn.Linear(n_users, n_features)
		self.feature_eval = nn.Linear(n_features, n_items)

	def forward(self, user, item):
		user_features = self.user_embedding(user)
		x = 10*F.sigmoid(self.feature_eval(x))
		return x

	def loss()
