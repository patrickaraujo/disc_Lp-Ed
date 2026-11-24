"""
Exercício 4 — Conta de energia com NumPy

Uma vila tem 3 casas. O consumo (kWh) de cada casa em 4 meses foi lido
em sequência, casa por casa:

    leituras = [210, 185, 230, 250,   150, 140, 160, 175,   320, 300, 290, 335]

  a) Transforme as leituras em um array NumPy 3 x 4 (casas x meses) com
     reshape.
  b) Calcule a matriz de custos: R$ 0,85 por kWh mais uma taxa fixa de
     R$ 12,00 por mês. Faça a conta com o array inteiro, sem laço.
  c) Crie com np.zeros um array para o total de cada casa e preencha-o
     com laços aninhados.
  d) Mostre a casa com o maior total e quantos meses, somando todas as
     casas, passaram de 250 kWh.
  e) Simule uma meta de economia de 10% (consumo * 0.9) e mostre a nova
     matriz de consumo.

Saída esperada:
    Consumo (kWh):
    [[210 185 230 250]
     [150 140 160 175]
     [320 300 290 335]]
    Custos (R$):
    [[190.5  169.25 207.5  224.5 ]
     [139.5  131.   148.   160.75]
     [284.   267.   258.5  296.75]]
    Total por casa: [ 791.75  579.25 1106.25]
    Casa com maior conta: 3 (R$ 1106.25)
    Meses acima de 250 kWh: 4
    Consumo com 10% de economia:
    [[189.  166.5 207.  225. ]
     [135.  126.  144.  157.5]
     [288.  270.  261.  301.5]]
"""

import numpy as np

TARIFA = 0.85
TAXA_FIXA = 12.0


def main():
    leituras = [210, 185, 230, 250, 150, 140, 160, 175, 320, 300, 290, 335]

    # a) lista com 12 valores -> array 3 linhas x 4 colunas
    consumo = np.array(leituras).reshape(3, 4)
    print("Consumo (kWh):")
    print(consumo)

    # b) Operação ELEMENTO A ELEMENTO: cada posição é multiplicada por
    #    0.85 e somada a 12. Com lista de listas, isso exigiria dois laços.
    custos = consumo * TARIFA + TAXA_FIXA
    print("Custos (R$):")
    print(custos)

    # c) np.zeros(3) -> [0. 0. 0.], um total para cada casa
    totais = np.zeros(3)
    for i in range(3):
        for j in range(4):
            totais[i] = totais[i] + custos[i][j]
    print("Total por casa:", totais)

    # d) Maior total (sem max) e contagem de meses acima de 250 kWh
    maior = 0
    for i in range(1, 3):
        if totais[i] > totais[maior]:
            maior = i
    print(f"Casa com maior conta: {maior + 1} (R$ {totais[maior]:.2f})")

    acima = 0
    for i in range(3):
        for j in range(4):
            if consumo[i][j] > 250:
                acima = acima + 1
    print("Meses acima de 250 kWh:", acima)

    # e) Nova matriz: a original não muda
    print("Consumo com 10% de economia:")
    print(consumo * 0.9)


if __name__ == "__main__":
    main()
