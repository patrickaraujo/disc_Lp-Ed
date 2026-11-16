"""
Exercício Tutoreado 1 — Fechamento do diário (revisão integrada)

Um professor quer fechar o diário de um aluno. Faça um programa que:

  a) Leia quantas avaliações o aluno fez (int).
  b) Leia cada nota (float). Notas fora do intervalo [0, 10] devem ser
     pedidas de novo até que o usuário digite uma nota válida (while).
  c) Guarde as notas válidas em uma lista (append).
  d) Calcule a média com uma variável acumuladora (sem usar sum()).
  e) Crie a função situacao(media), que devolve:
       "Aprovado"     se media >= 7
       "Recuperação"  se media >= 5
       "Reprovado"    caso contrário
  f) Mostre as notas, a média com 1 casa decimal, a situação e quantas
     notas ficaram abaixo de 5.

Depois, faça o TESTE DE MESA do item d) com as notas [8.0, 4.5, 7.0]
(tabela no final do arquivo).

Saída esperada:
    Quantas avaliações? 3
    Nota 1: 8
    Nota 2: 11
    Nota inválida! Digite um valor entre 0 e 10.
    Nota 2: 4.5
    Nota 3: 7
    Notas: [8.0, 4.5, 7.0]
    Média: 6.5
    Situação: Recuperação
    Notas abaixo de 5: 1
"""


def situacao(media):
    # A ORDEM dos testes importa: começamos pela condição mais restritiva.
    # Se o teste "media >= 5" viesse primeiro, uma média 9 cairia nele
    # e o aluno nunca seria "Aprovado" (o if-elif para no 1º verdadeiro).
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def main():
    # a) input() SEMPRE devolve str -> convertemos com int()
    quantidade = int(input("Quantas avaliações? "))

    # b) e c) Lista vazia + append dentro de um laço
    notas = []
    for i in range(quantidade):
        nota = float(input(f"Nota {i + 1}: "))
        # while de VALIDAÇÃO: repete enquanto a nota for inválida.
        # Não sabemos quantas vezes o usuário vai errar -> while, e não for.
        while nota < 0 or nota > 10:
            print("Nota inválida! Digite um valor entre 0 e 10.")
            nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)

    # d) Variável acumuladora: inicializada UMA vez, ANTES do laço.
    #    (Se o "soma = 0" ficasse dentro do for, a soma seria zerada
    #     a cada volta e só a última nota sobraria.)
    soma = 0
    abaixo_de_5 = 0          # contador: também começa antes do laço
    for nota in notas:
        soma = soma + nota
        if nota < 5:
            abaixo_de_5 = abaixo_de_5 + 1

    media = soma / len(notas)   # divide pelo TAMANHO da lista, não por um número fixo

    # f) Saída
    print("Notas:", notas)
    print(f"Média: {media:.1f}")
    print("Situação:", situacao(media))
    print("Notas abaixo de 5:", abaixo_de_5)


# ---------------------------------------------------------------------
# TESTE DE MESA do laço de soma com notas = [8.0, 4.5, 7.0]
#
#   volta | nota | soma (antes) | soma (depois) | nota < 5? | abaixo_de_5
#   ------+------+--------------+---------------+-----------+------------
#   início|  -   |      -       |      0        |     -     |     0
#     1   | 8.0  |      0       |     8.0       |   False   |     0
#     2   | 4.5  |     8.0      |    12.5       |   True    |     1
#     3   | 7.0  |    12.5      |    19.5       |   False   |     1
#
#   media = 19.5 / 3 = 6.5  ->  6.5 >= 7? Não.  6.5 >= 5? Sim.  -> "Recuperação"
# ---------------------------------------------------------------------

if __name__ == "__main__":
    main()
