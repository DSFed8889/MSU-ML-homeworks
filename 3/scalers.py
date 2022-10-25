import numpy as np


class MinMaxScaler:
    def __init__(self):
        self.max = None
        self.min = None

    def fit(self, data):
        """Store calculated statistics

        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """
        self.max = data.max(axis=0)
        self.min = data.min(axis=0)

    def transform(self, data):
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)

        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        return (data - self.min) / (self.max - self.min)


class StandardScaler:
    def __init__(self):
        self.std = None
        self.expect = None

    def fit(self, data):
        """Store calculated statistics

        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """
        self.expect = data.mean(axis=0)
        self.std = data.std(axis=0)

    def transform(self, data):
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)

        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        return (data - self.expect) / self.std
