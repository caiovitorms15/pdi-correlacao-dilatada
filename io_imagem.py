import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def abrir_imagem(caminho):
    img = Image.open(caminho)

    img = img.convert("RGB")

    array_img = np.array(img, dtype=np.uint8)

    return array_img

def exibir_imagem(array_img):

    if len(array_img.shape) == 2:
        array_img = np.stack([array_img]*3, axis=2)

    img = Image.fromarray(array_img.astype(np.uint8), mode="RGB")
    img.show()

def normalizar_para_uint8(img):

    img = img.astype(np.float64)

    minimo = np.min(img)
    maximo = np.max(img)

    if maximo - minimo == 0:
        return np.zeros_like(img, dtype=np.uint8)

    img = (img - minimo) / (maximo - minimo)
    img = img * 255

    return img.astype(np.uint8)



def salvar_imagem(array_img, caminho):
    img = Image.fromarray(array_img, mode="RGB")
    img.save(caminho)


def exibir_imagem_inline(array_img, titulo=None):
    
    if len(array_img.shape) == 2:
        plt.imshow(array_img, cmap='gray')
    else:
        plt.imshow(array_img.astype(np.uint8))
    
    if titulo:
        plt.title(titulo)
    
    plt.axis("off")
    plt.show()