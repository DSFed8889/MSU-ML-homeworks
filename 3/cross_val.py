import numpy as np
from collections import defaultdict


def kfold_split(num_objects, num_folds):
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects (int): number of objects in train set
    num_folds (int): number of folds for cross-validation split

    Returns:
    list((tuple(np.array, np.array))): list of length num_folds, where i-th element of list contains tuple of 2 numpy arrays,
                                       the 1st numpy array contains all indexes without i-th fold while the 2nd one contains
                                       i-th fold
    """
    obj = np.arange(num_objects)
    folds = list(np.array_split(obj[:num_objects - num_objects % num_folds], num_folds))
    if num_objects % num_folds:
        folds[-1] = obj[folds[-1][0]:]
    print(folds)
    for i, fold in enumerate(folds):
        folds[i] = (np.delete(obj, fold), fold)
    return folds


def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    """Takes train data, counts cross-validation score over grid of parameters (all possible parameters combinations)

    Parameters:
    X (2d np.array): train set
    y (1d np.array): train labels
    parameters (dict): dict with keys from {n_neighbors, metrics, weights, normalizers}, values of type list,
                       parameters['normalizers'] contains tuples (normalizer, normalizer_name), see parameters
                       example in your jupyter notebook
    score_function (callable): function with input (y_true, y_predict) which outputs score metric
    folds (list): output of kfold_split
    knn_class (obj): class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight), value - mean score over all folds
    """
    ans = {}
    for normalizer, normalizer_name in parameters['normalizers']:
        for n_neighbors in parameters['n_neighbors']:
            for metric in parameters['metrics']:
                for weight in parameters['weights']:
                    ans[(normalizer_name, n_neighbors, metric, weight)] = 0
                    for fold in folds:
                        x_train, x_test = X[fold[0]], X[fold[1]]
                        y_train, y_test = y[fold[0]], y[fold[1]]
                        if normalizer:
                            normalizer.fit(x_train)
                            x_train = normalizer.transform(x_train)
                            x_test = normalizer.transform(x_test)
                        classifier = knn_class(n_neighbors=n_neighbors, metric=metric, weights=weight)
                        classifier.fit(x_train, y_train)
                        pred = classifier.predict(x_test)
                        ans[(normalizer_name, n_neighbors, metric, weight)] += score_function(y_test, pred)
                    ans[(normalizer_name, n_neighbors, metric, weight)] /= len(folds)
    return ans


X_1 = kfold_split(5, 3)
print(X_1, len(X_1))
