"""
Exercício 1 — Posições não nulas

Peça ao usuário o número de linhas e de colunas de uma matriz e leia a
matriz linha por linha: cada linha é digitada de uma vez, com os valores
separados por espaço. Crie as funções:

- le_matriz(linhas, colunas): lê e retorna a matriz. Se a quantidade de
  valores digitados em uma linha for diferente de colunas, mostra uma
  mensagem e pede a linha novamente;
- imprime_matriz(mat): mostra a matriz em formato de tabela (não retorna nada);
- posicoes_nao_nulas(mat): retorna uma LISTA de TUPLAS (linha, coluna)
  com as posições diferentes de zero, contando a partir de 1.

Na main(), mostre a matriz, quantas posições são não nulas, a lista de
posições e o percentual de posições não nulas.

Dica: input().split() devolve uma lista de textos; converta cada um com int().

Saída esperada:
    Linhas: 3
    Colunas: 4
    Linha 1: 0 5 0 2
    Linha 2: 0 0 0
    Digite exatamente 4 valores.
    Linha 2: 0 0 0 0
    Linha 3: 7 0 1 0
    Matriz:
       0   5   0   2
       0   0   0   0
       7   0   1   0
    Posições não nulas: 4
    Posições: [(1, 2), (1, 4), (3, 1), (3, 3)]
    Percentual não nulo: 33.3%
"""


def main():
    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))

    matriz = le_matriz(linhas, colunas)

    print("Matriz:")
    imprime_matriz(matriz)

    posicoes = posicoes_nao_nulas(matriz)
    total = linhas * colunas
    print("Posições não nulas:", len(posicoes))
    print("Posições:", posicoes)
    print(f"Percentual não nulo: {len(posicoes) / total * 100:.1f}%")


def le_matriz(linhas, colunas):
    mat = []
    while len(mat) < linhas:
        valores = input(f"Linha {len(mat) + 1}: ").split()
        if len(valores) != colunas:
            print(f"Digite exatamente {colunas} valores.")
        else:
            mat.append([int(v) for v in valores])
    return mat


def imprime_matriz(mat):
    for linha in mat:
        for valor in linha:
            print(f"{valor:4}", end="")
        print()


def posicoes_nao_nulas(mat):
    posicoes = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                posicoes.append((i + 1, j + 1))  # como o usuário enxerga
    return posicoes


if __name__ == "__main__":
    main()
