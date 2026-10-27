"""
Exercício Tutoreado 2 — Vendas da farmácia com NumPy

Uma rede de farmácias tem 3 filiais e vende 4 produtos. As quantidades
vendidas na semana ficam em uma matriz (linha = filial, coluna = produto)
e os preços em um vetor. Usando a biblioteca NumPy, faça um programa que:

  a) Crie os arrays a partir de listas e mostre ndim, size e shape.
  b) Crie arrays com arange + reshape, zeros e ones.
  c) Aplique operações posição a posição (+, -, *, /, **): reajuste
     de 10% nos preços e meta de vendas 20% maior.
  d) Mostre a diferença entre A * B (posição a posição) e np.dot(A, B)
     (multiplicação de matrizes).
  e) Calcule o faturamento de cada filial com np.dot(vendas, precos).
  f) Calcule totais por produto e por filial com sum(axis=...) e
     compare com a função total_por_coluna(mat), feita com laços.

Antes de rodar, instale o NumPy (uma única vez):
    pip install numpy

Saída esperada (trecho):
    vendas.ndim: 2
    vendas.size: 12
    vendas.shape: (3, 4)
    ...
    Faturamento por filial:
      Centro: R$ 965.00
      Norte: R$ 731.00
      Sul: R$ 1152.50
"""

import numpy as np  # "np" é o apelido usado por toda a comunidade


def main():
    filiais = ["Centro", "Norte", "Sul"]
    produtos = ["dipirona", "paracetamol", "vitamina c", "soro"]

    # =================================================================
    # a) Criando arrays a partir de listas
    # =================================================================
    # Vetor (1 dimensão): preço de cada produto
    precos = np.array([12.50, 8.00, 25.00, 4.50])

    # Matriz (2 dimensões): mesma lista de listas da aula, mas como array
    vendas = np.array([[30, 20, 10, 40],   # Centro
                       [25, 15, 6, 33],    # Norte
                       [40, 30, 12, 25]])  # Sul

    print("precos:", precos)
    print("vendas:")
    print(vendas)

    print("precos.ndim:", precos.ndim)    # número de dimensões -> 1
    print("vendas.ndim:", vendas.ndim)    # -> 2
    print("vendas.size:", vendas.size)    # total de posições -> 12
    print("vendas.shape:", vendas.shape)  # (linhas, colunas) -> (3, 4)

    # O acesso continua [linha][coluna]; o NumPy aceita também [linha, coluna]
    print("Soro vendido no Norte:", vendas[1][3], "=", vendas[1, 3])

    # Array é HOMOGÊNEO: todos os elementos têm o mesmo tipo
    print(np.array([1, 2.5, 3]))  # o 1 e o 3 viram float: [1.  2.5 3. ]

    print("-" * 40)

    # =================================================================
    # b) Outras formas de criar arrays
    # =================================================================
    print(np.arange(12))                # 0, 1, ..., 11 (como o range)
    print(np.arange(12).reshape(3, 4))  # os mesmos 12 valores em 3 x 4
    print(np.zeros((2, 4)))             # o argumento é uma TUPLA
    print(np.ones((2, 3)))
    # np.arange(12).reshape(5, 3)   # descomente: ValueError (12 != 5 * 3)

    print("-" * 40)

    # =================================================================
    # c) Operações posição a posição: SEM laço!
    # =================================================================
    # Com listas, precos * 1.10 daria TypeError. Com arrays, cada posição
    # é multiplicada por 1.10.
    novos_precos = precos * 1.10
    print("Preços com reajuste de 10%:", novos_precos.round(2))

    meta = vendas * 1.2
    print("Meta (20% a mais):")
    print(meta)

    # Também funciona entre dois arrays do mesmo formato
    semana_passada = np.array([[28, 22, 8, 35],
                               [20, 15, 7, 30],
                               [41, 25, 10, 20]])
    print("Diferença em relação à semana passada:")
    print(vendas - semana_passada)

    print("Quadrado de cada posição de [1, 2, 3]:", np.array([1, 2, 3]) ** 2)

    print("-" * 40)

    # =================================================================
    # d) A * B  x  np.dot(A, B)
    # =================================================================
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])
    print("A * B (posição a posição):")
    print(A * B)
    print("np.dot(A, B) (multiplicação de matrizes):")
    print(np.dot(A, B))

    print("-" * 40)

    # =================================================================
    # e) Faturamento por filial = vendas (3 x 4) . precos (4) -> 3 valores
    #    Cada filial: soma de quantidade * preço de cada produto
    # =================================================================
    faturamento = np.dot(vendas, precos)
    print("Faturamento por filial:")
    for i in range(len(filiais)):
        print(f"  {filiais[i]}: R$ {faturamento[i]:.2f}")

    print("-" * 40)

    # =================================================================
    # f) Totais com sum(axis=...)
    #    axis=0 -> "desce" pelas linhas: um total por COLUNA (produto)
    #    axis=1 -> "anda" pelas colunas: um total por LINHA (filial)
    # =================================================================
    por_produto = vendas.sum(axis=0)
    por_filial = vendas.sum(axis=1)

    print("Unidades por produto:")
    for j in range(len(produtos)):
        print(f"  {produtos[j]}: {por_produto[j]}")
    print("Unidades por filial:", por_filial)
    print("Total geral:", vendas.sum())
    print(f"Média de unidades por posição: {vendas.mean():.2f}")

    # A MESMA conta do total por produto, com laços e listas comuns.
    # tolist() converte o array de volta para lista de listas.
    print("Por produto (com laços):", total_por_coluna(vendas.tolist()))


def total_por_coluna(mat):
    # Versão "na mão" do sum(axis=0): uma soma para cada coluna
    totais = []
    for j in range(len(mat[0])):
        soma = 0
        for i in range(len(mat)):
            soma += mat[i][j]
        totais.append(soma)
    return totais


if __name__ == "__main__":
    main()
