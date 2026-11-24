"""
Exercício 5 — Bubble Sort com parada antecipada

Implemente bubbleSort(lista), que ordena a lista em ordem crescente e
devolve uma tupla (passadas, comparacoes, trocas).

Use uma variável trocou: se uma passada inteira terminar SEM nenhuma
troca, a lista já está ordenada e o algoritmo deve parar.

Teste com as três listas abaixo e responda em comentário: por que a
lista "quase ordenada" termina tão mais rápido que a "invertida"?

    quase ordenada: [1, 2, 3, 5, 4, 6]
    embaralhada:    [5, 1, 4, 2, 8, 3]
    invertida:      [6, 5, 4, 3, 2, 1]

Saída esperada:
    quase ordenada: [1, 2, 3, 4, 5, 6] | passadas=2 comparações=9 trocas=1
    embaralhada: [1, 2, 3, 4, 5, 8] | passadas=4 comparações=14 trocas=7
    invertida: [1, 2, 3, 4, 5, 6] | passadas=5 comparações=15 trocas=15
"""


def bubbleSort(lista):
    n = len(lista)
    passadas = 0
    comparacoes = 0
    trocas = 0

    for fim in range(n - 1, 0, -1):     # a cada passada, o maior "sobe" para o fim
        passadas = passadas + 1
        trocou = False
        for j in range(fim):            # compara vizinhos até a parte já ordenada
            comparacoes = comparacoes + 1
            if lista[j] > lista[j + 1]:
                # troca usando uma variável auxiliar
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                trocas = trocas + 1
                trocou = True
        if not trocou:                  # passada sem troca: já está ordenada
            break

    return passadas, comparacoes, trocas


def main():
    testes = [
        ("quase ordenada", [1, 2, 3, 5, 4, 6]),
        ("embaralhada", [5, 1, 4, 2, 8, 3]),
        ("invertida", [6, 5, 4, 3, 2, 1]),
    ]
    for nome, lista in testes:
        passadas, comparacoes, trocas = bubbleSort(lista)
        print(f"{nome}: {lista} | passadas={passadas} "
              f"comparações={comparacoes} trocas={trocas}")

    # Resposta: na lista quase ordenada, a 1ª passada já resolve a única
    # inversão (5, 4); a 2ª passada não faz trocas e o laço para. Na lista
    # invertida, todo par está fora de ordem: são necessárias todas as
    # passadas, e cada comparação gera uma troca.


if __name__ == "__main__":
    main()
