import numpy as np

def correlacao(img, kernel, stride=1, r=1, ativacao="identidade"):

    img = img.astype(np.float64)
    kernel = np.array(kernel, dtype=np.float64)

    altura, largura, canais = img.shape
    k_altura, k_largura = kernel.shape

    # Tamanho efetivo do kernel dilatado (Atrous)
    k_altura_dil = (k_altura - 1) * r + 1
    k_largura_dil = (k_largura - 1) * r + 1

    # Sem padding
    out_altura = (altura - k_altura_dil) // stride + 1
    out_largura = (largura - k_largura_dil) // stride + 1

    if out_altura <= 0 or out_largura <= 0:
        raise ValueError("Kernel maior que a imagem para os parâmetros escolhidos.")

    output = np.zeros((out_altura, out_largura, canais), dtype=np.float64)

    # Percorrer cada canal separadamente
    for c in range(canais):

        for i in range(out_altura):
            for j in range(out_largura):

                soma = 0.0

                for m in range(k_altura):
                    for n in range(k_largura):

                        i_img = i * stride + m * r
                        j_img = j * stride + n * r

                        soma += img[i_img, j_img, c] * kernel[m, n]

                # Aplicação da função de ativação
                if ativacao == "relu":
                    soma = max(0, soma)
                elif ativacao == "identidade":
                    pass
                else:
                    raise ValueError("Função de ativação inválida. Use 'relu' ou 'identidade'.")

                output[i, j, c] = soma

    return output
