"""
Exercício Tutoreado 1 — Diário de classe (listas e tuplas)

Faça um programa que organize o diário de uma turma:

Parte 1 — Listas
  a) Crie uma lista com 5 alunos, uma lista vazia e uma lista mista
     (com tipos diferentes e uma lista dentro dela).
  b) Mostre o primeiro e o último aluno (índice positivo e negativo)
     e os 3 primeiros (fatiamento).
  c) Atualize a turma: um aluno chegou (append), outro entrou na
     2ª posição (insert), um saiu pela posição (del) e outro pelo
     nome (remove).
  d) Leia a nota de cada aluno, guardando-as em uma lista. Dê 1 ponto
     extra ao primeiro aluno, mostre a média e quem ficou acima dela.
  e) Junte a turma com uma turma B (concatenação), crie a lista de
     faltas zerada (repetição) e uma lista de notas com bônus
     (compreensão de lista).

Parte 2 — Tuplas
  f) Guarde a data da prova em uma tupla, mostre um elemento, uma
     fatia e desempacote-a em três variáveis.
  g) Leia nome, sobrenome e turma em uma única linha usando split().

Saída esperada (trecho):
    Alunos: ['Ana', 'Bruno', 'Carla', 'Diego', 'Elisa'] (5 alunos)
    Primeiro: Ana | Último: Elisa
    3 primeiros: ['Ana', 'Bruno', 'Carla']
    Turma atualizada: ['Ana', 'Beatriz', 'Bruno', 'Elisa', 'Fábio']
    Nota de Ana: 7
    ...
    Notas: [8.0, 5.0, 9.0, 6.0, 7.5]
    Média da turma: 7.1
    ...
    Prova em 16 de outubro de 2026
"""


def main():
    # =================================================================
    # PARTE 1 — LISTAS
    # =================================================================

    # a) Criando listas: [dado1, dado2, ..., dadoN]
    alunos = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]
    vazia = []                                          # lista vazia
    mista = ["Fernando", 2026001, 8.5, ["LPED", "POO"]]  # tipos diferentes

    print(f"Alunos: {alunos} ({len(alunos)} alunos)")
    print("Lista vazia:", vazia, "| tamanho:", len(vazia))
    # Lista dentro de lista: 1º colchete -> lista principal; 2º -> sublista
    print("Disciplinas do Fernando:", mista[3], "| primeira:", mista[3][0])

    # b) Índices: vão de 0 até n - 1. Negativos contam da direita (-1 = último)
    print("Primeiro:", alunos[0], "| Último:", alunos[-1])
    print("Último pelo len:", alunos[len(alunos) - 1])
    # print(alunos[5])   # descomente: IndexError: list index out of range

    # Fatiamento: lista[início:fim] -> o índice 'fim' NÃO entra
    print("3 primeiros:", alunos[0:3])
    print("Do 2º ao 4º:", alunos[1:4])

    # c) Listas podem ser modificadas
    alunos.append("Fábio")       # acrescenta no final
    alunos.insert(1, "Beatriz")  # insere ANTES da posição 1
    del alunos[3]                # remove pela posição (sai a Carla)
    alunos.remove("Diego")       # remove pelo valor
    print("Turma atualizada:", alunos)

    print("-" * 40)

    # d) Lista vazia + append dentro de um laço = ler vários dados
    notas = []
    for i in range(len(alunos)):
        nota = float(input(f"Nota de {alunos[i]}: "))
        notas.append(nota)

    # Uma posição da lista se comporta como uma variável comum
    notas[0] = notas[0] + 1
    print("Notas:", notas)

    # Percorrendo pelo VALOR: a variável assume cada elemento
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)
    print("Média da turma:", format(media, ".1f"))

    # Percorrendo pelo ÍNDICE: o mesmo i serve para as duas listas
    print("Acima da média:")
    for i in range(len(notas)):
        if notas[i] > media:
            print(f"  {alunos[i]} ({notas[i]})")

    print("-" * 40)

    # e) Concatenação (+), repetição (*) e compreensão de lista
    turma_b = ["Gabi", "Hugo"]
    todos = alunos + turma_b          # "gruda" turma_b no final
    faltas = [0] * len(todos)         # mesma coisa que [0, 0, 0, ...]
    bonus = [nota + 0.5 for nota in notas]

    print("Todos os alunos:", todos)
    print("Faltas:", faltas)
    print("Notas com bônus:", bonus)

    print("-" * 40)

    # =================================================================
    # PARTE 2 — TUPLAS (parecidas com listas, mas IMUTÁVEIS)
    # =================================================================

    data_prova = (16, "outubro", 2026)  # com parênteses
    sala = "Bloco A", 204               # sem parênteses (empacotamento)
    so_uma = ("LPED",)                  # 1 elemento: a vírgula é obrigatória
    nao_e_tupla = ("LPED")              # sem vírgula é só uma string!
    tupla_vazia = ()

    print("Sala:", sala, "| Tupla vazia:", tupla_vazia)
    print(type(so_uma), type(nao_e_tupla))

    # Acesso e fatiamento funcionam igual às listas
    print("Mês da prova:", data_prova[1])
    print("Dia e mês:", data_prova[0:2])
    # data_prova[0] = 17   # descomente: TypeError (tupla não pode ser alterada)

    # Desempacotamento: cada elemento vai para uma variável
    dia, mes, ano = data_prova
    print(f"Prova em {dia} de {mes} de {ano}")

    # split() separa o texto nos espaços; o resultado é desempacotado.
    # Digite EXATAMENTE 3 palavras, ex.: Patrick Araujo LPED
    nome, sobrenome, turma = input("Nome, sobrenome e turma: ").split()
    print(f"Diário de {nome} {sobrenome} — turma {turma}")


if __name__ == "__main__":
    main()
