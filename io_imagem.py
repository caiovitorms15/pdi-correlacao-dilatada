from PIL import Image
import numpy as np

def abrir_imagem(caminho):
    img = Image.open(caminho)

    img = img.convert("RGB")

    array_img = np.array(img, dtype=np.uint8)

    return array_img

def salvar_imagem(array_img, caminho):
    img = Image.fromarray(array_img, mode="RGB")
    img.save(caminho)
