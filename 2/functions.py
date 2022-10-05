from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    count = 0
    res = 0
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            count += 1
            res += X[i][i]
    return -1 if count == 0 else res


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return sorted(x) == sorted(y)


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    count = 0
    res = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            if count == 0 or x[i] * x[i + 1] > res:
                res = x[i] * x[i + 1]
                count += 1
    return res


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    res = []
    for i in range(len(image)):
        tempList = []
        for j in range(len(image[0])):
            tempList.append(0.0)
        res.append(tempList)
    for i in range(len(image[0][0])):
        for j in range(len(image[0])):
            for k in range(len(image)):
                res[k][j] += image[k][j][i] * weights[i]
    return res


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    res = 0
    x_decode = []
    for i in range(len(x)):
        x_decode += [x[i][0]] * x[i][1]
    y_decode = []
    for i in range(len(y)):
        y_decode += [y[i][0]] * y[i][1]
    if len(x_decode) != len(y_decode):
        return -1
    for i in range(len(x_decode)):
        res += x_decode[i] * y_decode[i]
    return res


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """

    pass
