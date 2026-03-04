import numpy as np

def correlacao(img, mascara, stride=1, r=1, ativacao="identidade", pivo=None):

    img = img.astype(np.float64)
    mascara = np.array(mascara, dtype=np.float64)

    altura, largura, canais = img.shape
    k_altura, k_largura = mascara.shape

    if pivo is None:
        pivo = (k_altura // 2, k_largura // 2)
    
    pivo_i, pivo_j = pivo
    
    if not (0 <= pivo_i < k_altura and 0 <= pivo_j < k_largura):
        raise ValueError(f"Posição do pivô {pivo} inválida para máscara de tamanho {k_altura}x{k_largura}.")

    k_altura_dil = (k_altura - 1) * r + 1
    k_largura_dil = (k_largura - 1) * r + 1

    pivo_i_dil = pivo_i * r
    pivo_j_dil = pivo_j * r

    inicio_i = pivo_i_dil
    inicio_j = pivo_j_dil
    fim_i = altura - (k_altura_dil - 1 - pivo_i_dil)
    fim_j = largura - (k_largura_dil - 1 - pivo_j_dil)

    out_altura = (fim_i - inicio_i) // stride
    out_largura = (fim_j - inicio_j) // stride

    if out_altura <= 0 or out_largura <= 0:
        raise ValueError("Máscara maior que a imagem para os parâmetros escolhidos.")

    output = np.zeros((out_altura, out_largura, canais), dtype=np.float64)

    for c in range(canais):

        for i in range(out_altura):
            for j in range(out_largura):

                soma = 0.0

                centro_i = inicio_i + i * stride
                centro_j = inicio_j + j * stride

                for m in range(k_altura):
                    for n in range(k_largura):

                        i_img = centro_i + (m - pivo_i) * r
                        j_img = centro_j + (n - pivo_j) * r

                        soma += img[i_img, j_img, c] * mascara[m, n]

                if ativacao == "relu":
                    soma = max(0, soma)
                elif ativacao == "identidade":
                    pass
                else:
                    raise ValueError("Função de ativação inválida. Use 'relu' ou 'identidade'.")

                output[i, j, c] = soma

    return output
