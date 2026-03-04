# 🎯 Correlação Dilatada (Atrous Correlation) em Imagens RGB

> Implementação manual de correlação dilatada aplicada a imagens RGB, com suporte a stride, funções de ativação e filtros espaciais configuráveis.

**Universidade Federal da Paraíba (UFPB)** — Centro de Informática  
**Disciplina:** Introdução ao Processamento Digital de Imagens  
**Professor:** Leonardo Vidal Batista  
**Aluno:** Caio Vitor Melo de Santana

---

## 📋 Sobre o Projeto

Este projeto implementa **manualmente** o operador de correlação dilatada (Atrous Convolution) aplicado a imagens RGB de 24 bits. Toda a lógica de acesso aos pixels e correlação foi desenvolvida sem uso de funções prontas de filtragem (como `cv2.filter2D`), com o objetivo de compreender de forma prática o funcionamento desses operadores.

---

## ✨ Funcionalidades

- ✅ Abertura e salvamento de imagens RGB (24 bits)
- ✅ Correlação dilatada com taxa de dilatação configurável (r = 1 a 5)
- ✅ Stride (passo) configurável (1 a 5)
- ✅ Suporte a máscaras de tamanho arbitrário (m × n)
- ✅ Pivô configurável para a máscara
- ✅ Funções de ativação: **ReLU** e **Identidade**
- ✅ Processamento independente nos canais R, G e B
- ✅ Configuração centralizada via JSON

---

## 🔧 Filtros Disponíveis

| Filtro | Tamanho | Descrição |
|--------|---------|-----------|
| **Gaussiano 5×5** | 5×5 | Suavização com distribuição gaussiana |
| **Box 1×10** | 1×10 | Borramento horizontal |
| **Box 10×1** | 10×1 | Borramento vertical |
| **Box 10×10** | 10×10 | Borramento intenso bidimensional |
| **Sobel Horizontal** | 3×3 | Detecção de bordas horizontais |
| **Sobel Vertical** | 3×3 | Detecção de bordas verticais |

---

## 📁 Estrutura do Projeto

```
pdi-correlacao-dilatada/
├── apresentacao.ipynb    # Notebook com demonstração completa
├── main.py               # Script principal para execução em lote
├── correlacao.py         # Implementação da correlação dilatada
├── io_imagem.py          # Funções de I/O de imagens
├── funcoesaux.py         # Funções auxiliares e visualização
├── config_filtros.json   # Configuração dos filtros e parâmetros
├── requirements.txt      # Dependências do projeto
├── Imagens/              # Imagens de entrada
│   └── resultados/       # Imagens processadas
└── README.md
```

---

## 🚀 Como Usar

### 1. Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/pdi-correlacao-dilatada.git
cd pdi-correlacao-dilatada

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### 2. Execução

**Via Script (processa todas as imagens):**
```bash
python main.py
```

**Via Notebook (interativo com visualizações):**
```bash
jupyter notebook apresentacao.ipynb
```

---

## 📐 Fórmulas

### Correlação Dilatada
$$Y(i,j) = \sum_{m=0}^{K-1} \sum_{n=0}^{K-1} I(i + rm,\; j + rn) \cdot H(m,n)$$

Onde:
- $r$ = taxa de dilatação ($r = 1$ → correlação comum)
- $K$ = tamanho da máscara
- $I$ = imagem de entrada
- $H$ = máscara/kernel

### Campo Receptivo Efetivo
$$K_{\text{efetivo}} = K + (K - 1)(r - 1)$$

---

## ⚙️ Configuração

Os filtros e parâmetros são configurados em `config_filtros.json`:

```json
{
    "filtros": [...],
    "parametros_globais": {
        "taxa_dilatacao_min": 1,
        "taxa_dilatacao_max": 5,
        "stride_min": 1,
        "stride_max": 5,
        "ativacoes_disponiveis": ["relu", "identidade"]
    }
}
```

---

## 📦 Dependências

- Python 3.8+
- NumPy
- Matplotlib
- Pillow

---

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos.
