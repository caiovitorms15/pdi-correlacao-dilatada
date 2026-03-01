import numpy as np

def correlacao (img, kernel, stride=1, r=1, ativacao=None):
    
    img = img.astype(np.float64)

    altura, largura = img.shape
    altura_kernel = len(kernel)
    largura_kernel = len(kernel[0])

    altura_kernel_dil = (altura_kernel -1) * r + 1     
    largura_kernel_dil = (largura_kernel -1) * r + 1

    out_altura = (altura - altura_kernel_dil) // stride + 1
    out_largura = (largura - largura_kernel_dil) // stride + 1

    output = np.zeros((out_altura, out_largura), dtype=np.float64)

    for i in range(out_altura):
        for j in range(out_largura):
            soma = 0.0

            for m in range(altura_kernel):
                for n in range(largura_kernel):

                    i_img = i * stride + m * r
                    j_img = j * stride + n * r

                    soma += img[i_img, j_img] * kernel[m][n]

            if ativacao == "relu":
                soma = max(0, soma)
                
            output[i, j] = soma

    return output

