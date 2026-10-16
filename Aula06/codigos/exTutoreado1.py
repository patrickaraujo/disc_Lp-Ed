"""
Exercício Tutoreado 1 — Diário de classe (listas e tuplas)

>>> VERSÃO GUIA: siga os passos e escreva o código logo abaixo de cada
>>> comentário. Rode o programa ao final de cada passo para conferir.

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
"""


def main():
    # =================================================================
    # PARTE 1 — LISTAS
    # =================================================================

    # -----------------------------------------------------------------
    # PASSO 1 — Criando listas
    # Sintaxe: nome = [dado1, dado2, ..., dadoN]
    # -----------------------------------------------------------------

    # 1.1 Crie a lista 'alunos' com: Ana, Bruno, Carla, Diego e Elisa.

    # 1.2 Crie a lista 'vazia', sem nenhum elemento.

    # 1.3 Crie a lista 'mista' com: o nome "Fernando", o RA 2026001,
    #     a nota 8.5 e, por último, uma LISTA com "LPED" e "POO".

    # 1.4 Mostre a lista 'alunos' e quantos alunos ela tem (len).

    # 1.5 Mostre a lista 'vazia' e o tamanho dela.

    # 1.6 Mostre a lista de disciplinas do Fernando (posição 3 de 'mista')
    #     e, depois, só a primeira disciplina.
    #     Dica: lista dentro de lista usa dois colchetes -> mista[?][?]

    # Saída esperada do Passo 1:
    #   Alunos: ['Ana', 'Bruno', 'Carla', 'Diego', 'Elisa'] (5 alunos)
    #   Lista vazia: [] | tamanho: 0
    #   Disciplinas do Fernando: ['LPED', 'POO'] | primeira: LPED

    # -----------------------------------------------------------------
    # PASSO 2 — Índices e fatiamento
    # Índices vão de 0 até n - 1. Índices negativos contam da direita.
    # -----------------------------------------------------------------

    # 2.1 Mostre o primeiro aluno (índice positivo) e o último
    #     (índice NEGATIVO).

    # 2.2 Mostre o último aluno de novo, agora usando len().
    #     Pergunta: por que o índice é len(alunos) - 1, e não len(alunos)?

    # 2.3 Escreva print(alunos[5]), rode e leia o erro. Qual é o nome dele?
    #     Depois, transforme a linha em comentário para seguir em frente.

    # 2.4 Usando fatiamento (lista[início:fim]), mostre:
    #     - os 3 primeiros alunos;
    #     - do 2º ao 4º aluno.
    #     Lembre-se: o índice 'fim' NÃO entra no resultado.

    # Saída esperada do Passo 2:
    #   Primeiro: Ana | Último: Elisa
    #   Último pelo len: Elisa
    #   3 primeiros: ['Ana', 'Bruno', 'Carla']
    #   Do 2º ao 4º: ['Bruno', 'Carla', 'Diego']

    # -----------------------------------------------------------------
    # PASSO 3 — Modificando a lista
    # -----------------------------------------------------------------

    # 3.1 O aluno "Fábio" chegou: acrescente-o no FINAL da lista.

    # 3.2 A aluna "Beatriz" deve entrar na 2ª posição (índice 1).
    #     Dica: lista.insert(índice, valor)

    # 3.3 Remova o aluno que está no índice 3 usando del.
    #     Antes de rodar: quem você acha que vai sair?

    # 3.4 Remova o aluno "Diego" pelo NOME.

    # 3.5 Mostre a turma atualizada.

    # Saída esperada do Passo 3:
    #   Turma atualizada: ['Ana', 'Beatriz', 'Bruno', 'Elisa', 'Fábio']

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 4 — Lendo dados para uma lista
    # Padrão: lista vazia + laço + append
    # -----------------------------------------------------------------

    # 4.1 Crie a lista 'notas' vazia.

    # 4.2 Faça um for com i indo de 0 até len(alunos) - 1. Dentro dele:
    #     - leia a nota do aluno alunos[i] (float), mostrando o nome
    #       na pergunta: "Nota de Ana: ";
    #     - acrescente a nota em 'notas'.

    # 4.3 O primeiro aluno ganhou 1 ponto extra: some 1 na nota da
    #     posição 0. (Uma posição da lista funciona como uma variável.)

    # 4.4 Mostre a lista de notas.

    # 4.5 Calcule a média percorrendo a lista PELO VALOR:
    #     for nota in notas  ->  some cada nota em 'soma'.
    #     Depois divida pela quantidade de notas e mostre com 1 casa
    #     decimal: format(media, ".1f")

    # 4.6 Mostre quem ficou acima da média percorrendo PELO ÍNDICE:
    #     for i in range(len(notas)). Mostre alunos[i] e notas[i].
    #     Pergunta: por que aqui precisamos do índice e não só do valor?

    # Saída esperada do Passo 4 (notas digitadas: 7, 5, 9, 6, 7.5):
    #   Notas: [8.0, 5.0, 9.0, 6.0, 7.5]
    #   Média da turma: 7.1
    #   Acima da média:
    #     Ana (8.0)
    #     Bruno (9.0)
    #     Fábio (7.5)

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 5 — Concatenação, repetição e compreensão de lista
    # -----------------------------------------------------------------

    # 5.1 Crie a lista 'turma_b' com "Gabi" e "Hugo".

    # 5.2 Crie a lista 'todos' juntando 'alunos' e 'turma_b' com o operador +.

    # 5.3 Crie a lista 'faltas' com um 0 para cada aluno de 'todos'.
    #     Dica: [0] * quantidade

    # 5.4 Crie a lista 'bonus' com cada nota + 0.5, em UMA linha.
    #     Dica: [expressão for variável in lista]

    # 5.5 Mostre 'todos', 'faltas' e 'bonus'.

    # Saída esperada do Passo 5:
    #   Todos os alunos: ['Ana', 'Beatriz', 'Bruno', 'Elisa', 'Fábio', 'Gabi', 'Hugo']
    #   Faltas: [0, 0, 0, 0, 0, 0, 0]
    #   Notas com bônus: [8.5, 5.5, 9.5, 6.5, 8.0]

    print("-" * 40)

    # =================================================================
    # PARTE 2 — TUPLAS (parecidas com listas, mas IMUTÁVEIS)
    # =================================================================

    # -----------------------------------------------------------------
    # PASSO 6 — Criando tuplas
    # -----------------------------------------------------------------

    # 6.1 Crie a tupla 'data_prova' COM parênteses: dia 16, "outubro", 2026.

    # 6.2 Crie a tupla 'sala' SEM parênteses: "Bloco A" e 204.

    # 6.3 Crie 'so_uma' com apenas "LPED" e 'nao_e_tupla' = ("LPED").
    #     Mostre type() das duas. Por que os tipos são diferentes?

    # 6.4 Crie 'tupla_vazia' e mostre-a junto com 'sala'.

    # Saída esperada do Passo 6:
    #   Sala: ('Bloco A', 204) | Tupla vazia: ()
    #   <class 'tuple'> <class 'str'>

    # -----------------------------------------------------------------
    # PASSO 7 — Acessando e desempacotando
    # -----------------------------------------------------------------

    # 7.1 Mostre o mês da prova (índice) e o dia e o mês juntos (fatiamento).

    # 7.2 Tente mudar o dia: data_prova[0] = 17. Rode e leia o erro.
    #     Depois, transforme a linha em comentário.

    # 7.3 Desempacote 'data_prova' em três variáveis (dia, mes, ano)
    #     em UMA linha e mostre: "Prova em 16 de outubro de 2026".

    # 7.4 Leia nome, sobrenome e turma em UMA linha e desempacote:
    #     nome, sobrenome, turma = input("...").split()
    #     Mostre: "Diário de <nome> <sobrenome> — turma <turma>".
    #     Teste: o que acontece se você digitar só 2 palavras?

    # Saída esperada do Passo 7:
    #   Mês da prova: outubro
    #   Dia e mês: (16, 'outubro')
    #   Prova em 16 de outubro de 2026
    #   Diário de Patrick Araujo — turma LPED


if __name__ == "__main__":
    main()
