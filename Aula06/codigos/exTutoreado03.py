"""
Exercício Tutoreado 3 — Boletim com funções

Reescreva o programa "leia n notas, mostre as notas e a média" dividindo-o
em funções, cada uma com uma tarefa:

  - le_quantidade(): sem parâmetros; lê e retorna quantas notas serão digitadas.
  - le_notas(n): lê n notas e retorna a lista.
  - calcula_media(notas): retorna a média da lista.
  - maior_e_menor(notas): retorna a maior e a menor nota (duas respostas!).
  - situacao(media, minimo=6.0): retorna "Aprovado", "Recuperação" ou
    "Reprovado". O mínimo vale 6.0 se não for informado.
  - imprime_caixa(texto): só mostra o texto dentro de uma moldura
    (não retorna nada).

Ao final, mostre também a situação do aluno se o mínimo fosse 7.0.

Saída esperada:
    Quantas notas? 3
    Nota 1: 8
    Nota 2: 5.5
    Nota 3: 6
    Notas: [8.0, 5.5, 6.0]
    Média: 6.5
    Maior: 8.0 | Menor: 5.5
    ++++++++++++++++++++++
    | Situação: Aprovado |
    ++++++++++++++++++++++
    Com mínimo 7.0: Recuperação
    ++++++++++++++++++
    | Fim do boletim |
    ++++++++++++++++++
    O que imprime_caixa() retornou? None
"""


# Repare: a main() está ANTES das outras funções e mesmo assim funciona.
# Isso acontece porque a main() só é CHAMADA na última linha do arquivo,
# quando todas as funções já foram definidas.
def main():
    n = le_quantidade()
    notas = le_notas(n)
    print("Notas:", notas)

    # O retorno de uma função pode ser guardado em uma variável...
    media = calcula_media(notas)
    # ...ou usado direto em qualquer expressão
    print("Média:", format(calcula_media(notas), ".1f"))

    # Uma função pode devolver dois valores (uma tupla): desempacotamos
    maior, menor = maior_e_menor(notas)
    print("Maior:", maior, "| Menor:", menor)

    # situacao() com o valor padrão (minimo = 6.0)
    imprime_caixa("Situação: " + situacao(media))

    # Argumentos nomeados: a ordem deixa de importar
    print("Com mínimo 7.0:", situacao(minimo=7.0, media=media))

    # Uma função sem return devolve None ("nada")
    resultado = imprime_caixa("Fim do boletim")
    print("O que imprime_caixa() retornou?", resultado)


# Função SEM parâmetros: os parênteses ficam vazios
def le_quantidade():
    quantidade = int(input("Quantas notas? "))
    return quantidade


# Função COM parâmetro: n recebe o valor passado na chamada
def le_notas(n):
    notas = []
    for i in range(n):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)
    return notas


def calcula_media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    return soma / len(notas)
    print("Esta linha NUNCA aparece: o return encerra a função.")


def maior_e_menor(notas):
    maior = notas[0]
    menor = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    return maior, menor  # empacotamento: devolve a tupla (maior, menor)


# 'minimo' tem valor PADRÃO: se a chamada não informar, vale 6.0.
# Cada caminho do if termina em um return diferente.
def situacao(media, minimo=6.0):
    if media >= minimo:
        return "Aprovado"
    elif media >= minimo - 2:
        return "Recuperação"
    else:
        return "Reprovado"


# Função que só mostra algo na tela: não precisa de return
def imprime_caixa(texto):
    print("+" * (len(texto) + 4))
    print("|", texto, "|")
    print("+" * (len(texto) + 4))


# Se esta chamada fosse a PRIMEIRA linha do arquivo, daria
# NameError: name 'main' is not defined (a função ainda não existiria).
if __name__ == "__main__":
    main()
