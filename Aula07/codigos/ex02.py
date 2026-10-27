"""
Exercício 2 — Operações com matrizes quadradas

Crie as funções abaixo para matrizes quadradas n x n (listas de listas).
As funções de cálculo devem RETORNAR uma nova matriz, sem alterar as
matrizes recebidas:

- le_matriz(n, nome): lê a matriz linha por linha (valores separados
  por espaço) e retorna a matriz;
- imprime_matriz(mat): mostra a matriz em formato de tabela;
- soma(m1, m2): retorna m1 + m2;
- subtracao(m1, m2): retorna m1 - m2;
- transposta(mat): retorna a transposta (a linha i vira a coluna i);
- eh_simetrica(mat): retorna True se a matriz for igual à sua transposta.

Na main(), leia n, as matrizes A e B, e mostre A + B, A - B, a
transposta de A e se A e B são simétricas.

Dica: na transposta, a posição [i][j] do resultado recebe mat[j][i].

Saída esperada:
    Dimensão n: 3
    Matriz A, linha 1: 1 2 3
    Matriz A, linha 2: 4 5 6
    Matriz A, linha 3: 7 8 9
    Matriz B, linha 1: 1 0 2
    Matriz B, linha 2: 0 3 4
    Matriz B, linha 3: 2 4 5
    A + B:
       2   2   5
       4   8  10
       9  12  14
    A - B:
       0   2   1
       4   2   2
       5   4   4
    Transposta de A:
       1   4   7
       2   5   8
       3   6   9
    A é simétrica? False
    B é simétrica? True
"""


def main():
    n = int(input("Dimensão n: "))
    a = le_matriz(n, "A")
    b = le_matriz(n, "B")

    print("A + B:")
    imprime_matriz(soma(a, b))
    print("A - B:")
    imprime_matriz(subtracao(a, b))
    print("Transposta de A:")
    imprime_matriz(transposta(a))
    print("A é simétrica?", eh_simetrica(a))
    print("B é simétrica?", eh_simetrica(b))


def le_matriz(n, nome):
    mat = []
    for i in range(n):
        valores = input(f"Matriz {nome}, linha {i + 1}: ").split()
        mat.append([int(v) for v in valores])
    return mat


def imprime_matriz(mat):
    for linha in mat:
        for valor in linha:
            print(f"{valor:4}", end="")
        print()


def soma(m1, m2):
    n = len(m1)
    resultado = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            resultado[i][j] = m1[i][j] + m2[i][j]
    return resultado


def subtracao(m1, m2):
    n = len(m1)
    resultado = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            resultado[i][j] = m1[i][j] - m2[i][j]
    return resultado


def transposta(mat):
    n = len(mat)
    resultado = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            resultado[i][j] = mat[j][i]
    return resultado


def eh_simetrica(mat):
    # Duas listas de listas podem ser comparadas com ==
    return mat == transposta(mat)


if __name__ == "__main__":
    main()
