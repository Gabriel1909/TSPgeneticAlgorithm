import pandas as pd


def distancia_euclidiana(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def ler_arquivo():
    ds = pd.read_csv('./problem/assets/st70.tsp.txt', header=None)
    arquivo = dict()
    for row in ds.itertuples():
        linha = row[1].split()

        arquivo[int(linha[0]) - 1] = [int(linha[1]), int(linha[2])]

    return arquivo
