from io_imagem import normalizar_para_uint8
from correlacao import correlacao
import matplotlib.pyplot as plt
import numpy as np

def exibir_lado_a_lado(img_original, img_resultado, titulo_original="Original", titulo_resultado="Resultado"):

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].imshow(img_original.astype(np.uint8))
    axes[0].set_title(titulo_original)
    axes[0].axis("off")
    
    if len(img_resultado.shape) == 2:
        axes[1].imshow(img_resultado, cmap='gray')
    else:
        axes[1].imshow(img_resultado.astype(np.uint8))
    axes[1].set_title(titulo_resultado)
    axes[1].axis("off")
    
    plt.tight_layout()
    plt.show()


def processar_sobel(resultado):
    resultado = np.abs(resultado)
    return normalizar_para_uint8(resultado)


def aplicar_e_exibir(img, mascara, nome_filtro, nome_imagem, stride=1, r=1, ativacao="identidade", sobel=False):
    resultado = correlacao(img, mascara, stride=stride, r=r, ativacao=ativacao)
    
    if sobel:
        resultado = processar_sobel(resultado)
        titulo = f"{nome_filtro} (abs + expansão histograma) r={r}, stride={stride}"
    else:
        resultado = np.clip(resultado, 0, 255).astype(np.uint8)
        titulo = f"{nome_filtro} r={r}, stride={stride}, ativação={ativacao}"
    
    exibir_lado_a_lado(img, resultado, titulo_original=f"{nome_imagem} - Original", titulo_resultado=titulo)
    return resultado