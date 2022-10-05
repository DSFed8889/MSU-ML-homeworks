import numpy as np


def sum_non_neg_diag(X: np.ndarray) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    X = np.diag(X)
    if True not in (X >= 0):
        return -1
    return np.sum(X[X > 0])


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return np.array_equal(np.sort(x), np.sort(y))


def max_prod_mod_3(x: np.ndarray) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    muls = x[:-1] * x[1:]
    return -1 if muls[muls % 3 == 0].size == 0 else max(muls[muls % 3 == 0])


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    return (image * weights).sum(axis=2)


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    if x[:, 1].sum() != y[:, 1].sum():
        return -1
    return np.dot(np.repeat(x[:, 0], x[:, 1], axis=0), np.repeat(y[:, 0], y[:, 1], axis=0))


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    Xnorm = np.linalg.norm(X, axis=1)
    Ynorm = np.linalg.norm(Y, axis=1)
    X = X / Xnorm[:, np.newaxis]
    Y = Y / Ynorm[:, np.newaxis]
    res = np.dot(X, Y.T)
    res[np.dot(Xnorm.reshape((-1, 1)), Ynorm.reshape((1, -1))) == 0] = 1
    return res
