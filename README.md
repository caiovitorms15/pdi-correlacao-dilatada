# pdi-correlacao-dilatada
Implementação manual de correlação dilatada (Atrous Convolution) aplicada a imagens RGB, com suporte a stride, funções de ativação e filtros espaciais.

# PDI - Correlação Dilatada em Imagens RGB

Sistema de Processamento Digital de Imagens desenvolvido para a disciplina 
Introdução ao Processamento Digital de Imagens da Universidade Federal da Paraíba (UFPB).

O projeto implementa manualmente o operador de correlação dilatada 
(Atrous Convolution) aplicado a imagens RGB de 24 bits, 
com suporte a stride, funções de ativação e filtros espaciais.

---

## Objetivo

Desenvolver um sistema capaz de:

- Abrir e salvar imagens RGB (24 bits)
- Aplicar correlação dilatada (taxa r entre 1 e 5)
- Aplicar stride (1 a 5)
- Utilizar diferentes máscaras (m x n)
- Aplicar funções de ativação (ReLU ou Identidade)
- Realizar processamento independente nos canais R, G e B
- Aplicar filtros como Gaussiano, Box e Sobel

Toda a lógica de acesso aos pixels e correlação foi implementada manualmente,
sem uso de funções prontas de filtragem (ex: cv2.filter2D).

---
