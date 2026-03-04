import os
import json
import numpy as np

from funcoesaux import processar_sobel, gerar_nome_saida
from correlacao import correlacao
from io_imagem import abrir_imagem, normalizar_para_uint8, salvar_imagem, exibir_imagem


def carregar_mascara(filtro_config):
    mascara = np.array(filtro_config["mascara"], dtype=np.float64)
    if filtro_config.get("normalizar_mascara", False):
        mascara = mascara / np.sum(mascara)
    return mascara


def eh_sobel(nome):
    return "sobel" in nome.lower()


def main():
    with open("config_filtros.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    params = config["parametros_globais"]
    r_min, r_max = params["taxa_dilatacao_min"], params["taxa_dilatacao_max"]
    s_min, s_max = params["stride_min"], params["stride_max"]

    pasta_saida = "Imagens/resultados"
    os.makedirs(pasta_saida, exist_ok=True)

    imagens = {
        "shapes": abrir_imagem("Imagens/Shapes.png"),
        "testpat": abrir_imagem("Imagens/testpat.1k.color2.tif"),
    }

    # aplicacao padrao com parametros do json
    print("aplicando filtros padrao...")
    for filtro_cfg in config["filtros"]:
        nome_filtro = filtro_cfg["nome"]
        mascara = carregar_mascara(filtro_cfg)
        stride = filtro_cfg["stride"]
        r = filtro_cfg["taxa_dilatacao"]
        ativacao = filtro_cfg["ativacao"]

        for nome_img, img in imagens.items():
            resultado = correlacao(img, mascara, stride=stride, r=r, ativacao=ativacao)

            if eh_sobel(nome_filtro):
                resultado = processar_sobel(resultado)
            else:
                resultado = np.clip(resultado, 0, 255).astype(np.uint8)

            caminho = gerar_nome_saida(pasta_saida, nome_img, nome_filtro, r=r, stride=stride, ativacao=ativacao)
            salvar_imagem(resultado, caminho)
            print(f"  {caminho}")

    # variacao do r
    print("\nvariando taxa de dilatacao...")
    for filtro_cfg in config["filtros"]:
        nome_filtro = filtro_cfg["nome"]
        if nome_filtro not in ("Gaussiano 5x5", "Sobel Horizontal"):
            continue

        mascara = carregar_mascara(filtro_cfg)

        for nome_img, img in imagens.items():
            for r_val in range(r_min, r_max + 1):
                resultado = correlacao(img, mascara, stride=1, r=r_val, ativacao="identidade")

                if eh_sobel(nome_filtro):
                    resultado = processar_sobel(resultado)
                else:
                    resultado = np.clip(resultado, 0, 255).astype(np.uint8)

                caminho = gerar_nome_saida(pasta_saida, nome_img, nome_filtro, r=r_val)
                salvar_imagem(resultado, caminho)
                print(f"  {caminho}")

    # variacao do stride
    print("\nvariando stride...")
    gauss_cfg = next(f for f in config["filtros"] if f["nome"] == "Gaussiano 5x5")
    mascara_gauss = carregar_mascara(gauss_cfg)

    for nome_img, img in imagens.items():
        for s_val in range(s_min, s_max + 1):
            resultado = correlacao(img, mascara_gauss, stride=s_val, r=1, ativacao="identidade")
            resultado = np.clip(resultado, 0, 255).astype(np.uint8)

            caminho = gerar_nome_saida(pasta_saida, nome_img, "Gaussiano 5x5", stride=s_val)
            salvar_imagem(resultado, caminho)
            print(f"  {caminho}")

    # relu vs identidade com sobel
    print("\ntestando relu vs identidade...")
    for filtro_cfg in config["filtros"]:
        nome_filtro = filtro_cfg["nome"]
        if not eh_sobel(nome_filtro):
            continue

        mascara = carregar_mascara(filtro_cfg)

        for nome_img, img in imagens.items():
            for ativacao in params["ativacoes_disponiveis"]:
                resultado = correlacao(img, mascara, stride=1, r=1, ativacao=ativacao)
                resultado = processar_sobel(resultado)

                caminho = gerar_nome_saida(pasta_saida, nome_img, nome_filtro, ativacao=ativacao)
                salvar_imagem(resultado, caminho)
                print(f"  {caminho}")

    print(f"\npronto, resultados em {os.path.abspath(pasta_saida)}")

    for nome_img, img in imagens.items():
        exibir_imagem(img)


if __name__ == "__main__":
    main()
