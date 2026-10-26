"""
Exercício Tutoreado 1 — Boletim da turma (matrizes com listas)

As notas de uma turma ficam em uma MATRIZ: cada LINHA é um aluno e cada
COLUNA é uma avaliação (P1, P2, Trabalho). Faça um programa que:

  a) Crie a matriz de notas e mostre quantas linhas e colunas ela tem.
  b) Acesse posições com matriz[linha][coluna]: a 2ª nota do 1º aluno
     e a última nota do último aluno.
  c) Mostre a matriz em formato de tabela com a função imprime_matriz().
  d) Calcule a média de cada ALUNO com media_linha(mat, i) e a média de
     cada AVALIAÇÃO com media_coluna(mat, j).
  e) Crie uma matriz 3 x 4 em que cada posição (i, j) vale i * j, primeiro
     com a função cria_matriz_ij(linhas, colunas), que usa dois laços for,
     e depois com compreensão de listas.
  f) Leia uma matriz 2 x 2 digitada pelo usuário com a função le_matriz().
  g) Guarde as notas de DUAS turmas em uma lista tridimensional e acesse
     uma nota com turmas[turma][aluno][nota].

Saída esperada (trecho):
    Matriz: 4 linhas x 3 colunas
    2ª nota de Ana: 7.0
    Última nota de Diego: 6.5
    ...
    Média por aluno:
      Ana: 7.5
      Bruno: 5.7
    ...
    Matriz i * j (com for): [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""


def main():
    # =================================================================
    # a) Criando a matriz: uma LISTA de LISTAS
    #    Cada lista interna é uma linha (um aluno).
    # =================================================================
    alunos = ["Ana", "Bruno", "Carla", "Diego"]
    avaliacoes = ("P1", "P2", "Trab")  # tupla: os nomes não mudam

    notas = [[8.0, 7.0, 7.5],   # linha 0 -> Ana
             [5.0, 4.0, 7.0],   # linha 1 -> Bruno
             [9.5, 9.0, 10.0],  # linha 2 -> Carla
             [6.0, 7.5, 6.5]]   # linha 3 -> Diego

    print(type(notas))  # <class 'list'>: em Python, matriz é lista de listas

    # len(notas) -> quantas linhas | len(notas[0]) -> quantas colunas
    linhas = len(notas)
    colunas = len(notas[0])
    print(f"Matriz: {linhas} linhas x {colunas} colunas")

    print("-" * 40)

    # =================================================================
    # b) Acesso: matriz[linha][coluna] — os índices começam em 0
    # =================================================================
    print("2ª nota de Ana:", notas[0][1])
    print("Última nota de Diego:", notas[-1][-1])  # negativos também valem
    print("Linha inteira da Carla:", notas[2])     # um índice só = uma linha
    # print(notas[4][0])   # descomente: IndexError (não existe a linha 4)

    # Uma posição se comporta como uma variável comum: revisão de nota
    notas[1][1] = 5.0
    print("Notas do Bruno após revisão:", notas[1])

    print("-" * 40)

    # =================================================================
    # c) Imprimindo em formato de tabela
    # =================================================================
    print("Boletim:")
    imprime_matriz(notas)

    print("-" * 40)

    # =================================================================
    # d) Percorrendo LINHAS e COLUNAS
    # =================================================================
    # As funções media_linha() e media_coluna() estão no fim do arquivo
    print("Média por aluno:")
    for i in range(linhas):
        print(f"  {alunos[i]}: {media_linha(notas, i):.1f}")

    print("Média por avaliação:")
    for j in range(colunas):
        print(f"  {avaliacoes[j]}: {media_coluna(notas, j):.1f}")

    print("-" * 40)

    # =================================================================
    # e) Construindo uma matriz 3 x 4 em que cada posição vale i * j
    # =================================================================
    # Forma 1: dois for, dentro da função cria_matriz_ij()
    mat = cria_matriz_ij(3, 4)
    print("Matriz i * j (com for):", mat)

    # Forma 2: compreensão de listas (uma compreensão dentro da outra)
    mat2 = [[i * j for j in range(4)] for i in range(3)]
    print("Matriz i * j (compreensão):", mat2)

    # Matriz 3 x 4 só de zeros, pronta para ser preenchida depois
    zeros = [[0 for j in range(4)] for i in range(3)]
    print("Matriz de zeros:", zeros)

    # CUIDADO: [[0] * 4] * 3 cria 3 referências para a MESMA linha!
    errada = [[0] * 4] * 3
    errada[0][0] = 99
    print("Armadilha [[0]*4]*3:", errada)  # o 99 aparece nas 3 linhas

    print("-" * 40)
 6 caracteres para cada número, alinhando-os perfeitamente em colunas (mesmo que alguns números tenham mais dígitos do que outros).

O
    # =================================================================
    # f) Lendo uma matriz digitada pelo usuário
    # =================================================================
    m = le_matriz(2, 2)
    print("Matriz digitada:")
    imprime_matriz(m)

    print("-" * 40)

    # =================================================================
    # g) Lista TRIDIMENSIONAL: turmas -> alunos -> notas
    # =================================================================
    turmas = [
        [[8.0, 7.0, 7.5], [5.0, 4.0, 7.0]],    # turma 0 (2 alunos)
        [[2.0, 8.0, 10.0], [8.6, 4.3, 7.0]],   # turma 1 (2 alunos)
    ]
    print("Quantidade de turmas:", len(turmas))
    print("Turma 1 inteira:", turmas[1])
    print("1º aluno da turma 1:", turmas[1][0])
    print("3ª nota do 1º aluno da turma 1:", turmas[1][0][2])


def media_linha(mat, i):
    # Fixa a LINHA i e varia a coluna j
    soma = 0
    for j in range(len(mat[i])):
        soma += mat[i][j]
    return soma / len(mat[i])


def media_coluna(mat, j):
    # Fixa a COLUNA j e varia a linha i (só trocamos o índice que anda)
    soma = 0
    for i in range(len(mat)):
        soma += mat[i][j]
    return soma / len(mat)


def cria_matriz_ij(num_linhas, num_colunas):
    mat = []
    for i in range(num_linhas):        # para cada linha
        linha = []                     # a linha começa vazia
        for j in range(num_colunas):   # para cada coluna
            linha.append(i * j)
        mat.append(linha)              # adiciona a linha pronta na matriz
    return mat


def imprime_matriz(mat):
    for linha in mat:
        for valor in linha:
            print(f"{valor:6}", end=" ")  # mesma linha, largura 6
        print()  # terminou a linha: pula para a próxima


def le_matriz(num_linhas, num_colunas):
    mat = [[] for i in range(num_linhas)]  # uma lista vazia para cada linha
    for i in range(num_linhas):
        for j in range(num_colunas):
            valor = float(input(f"({i + 1},{j + 1}): "))
            mat[i].append(valor)
    return mat


if __name__ == "__main__":
    main()
