from typing import List

import pandas as pd
from matplotlib import pyplot as plt


def swap(a: List, i: int, j: int) -> None:
    a[i], a[j] = a[j], a[i]


def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def read_file(path):
    ds = pd.read_csv(path, header=None)
    file = dict()
    for i in ds.itertuples():
        row = i[1].split()

        file[int(row[0]) - 1] = [int(row[1]), int(row[2])]

    return file


def plot_graph(results):
    plt.plot(results)
    plt.show()
    input()
