import numpy as np

def box_mascara(linhas, colunas):
    
    valor = 1.0 / (linhas * colunas)
    mascara = np.full((linhas, colunas), valor)
    return mascara

def gaussiano_5x5():
    
    mascara = np.array([
        [1,  4,  6,  4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1,  4,  6,  4, 1]
    ], dtype=float)

    soma = np.sum(mascara)
    mascara = mascara / soma

    return mascara

def sobel_horizontal():
    
    return np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=float)


def sobel_vertical():
    
    return np.array([
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ], dtype=float)