import numpy as np

def box_kernel(linhas, colunas):
    
    valor = 1.0 / (linhas * colunas)
    kernel = np.full((linhas, colunas), valor)
    return kernel

def gaussiano_5x5():
    
    kernel = np.array([
        [1,  4,  6,  4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1,  4,  6,  4, 1]
    ], dtype=float)

    soma = np.sum(kernel)
    kernel = kernel / soma

    return kernel

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