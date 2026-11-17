"""
Exercício 4 — Leituras de um sensor de umidade

Um sensor registra a umidade do ar (%) a cada hora. Quando ele falha,
grava o valor -1. As leituras do dia foram:

    leituras = [62, 65, -1, 71, 80, -1, 77, 68]

Crie as funções abaixo (sem usar sum(), max(), min() nem remove()):

  limpar(leituras)              -> devolve uma NOVA lista sem os -1
                                   (a lista original não pode mudar)
  media(lista)                  -> devolve a média dos valores
  posicao_pico(lista)           -> devolve o ÍNDICE do maior valor
  contar_acima(lista, limite=70)-> devolve quantos valores são maiores
                                   que o limite (valor padrão: 70)

Na main(), mostre as leituras originais, as válidas, quantas falhas
ocorreram, a média, o pico e sua posição, e quantas leituras ficaram
acima de 70 (limite padrão) e acima de 75 (argumento nomeado).

Saída esperada:
    Originais: [62, 65, -1, 71, 80, -1, 77, 68]
    Válidas: [62, 65, 71, 80, 77, 68]
    Falhas do sensor: 2
    Média: 70.5%
    Pico: 80% (posição 3 da lista de válidas)
    Acima de 70%: 3
    Acima de 75%: 2
"""


def limpar(leituras):
    validas = []                 # lista NOVA: não mexemos na original
    for valor in leituras:
        if valor != -1:
            validas.append(valor)
    return validas


def media(lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma / len(lista)


def posicao_pico(lista):
    # Começamos com a posição 0 (um valor DA PRÓPRIA lista), e não com
    # um número qualquer: assim funciona para qualquer lista.
    pos = 0
    for i in range(1, len(lista)):   # aqui pode começar em 1: o índice 0 já é o candidato
        if lista[i] > lista[pos]:
            pos = i
    return pos


def contar_acima(lista, limite=70):
    quantidade = 0
    for valor in lista:
        if valor > limite:
            quantidade = quantidade + 1
    return quantidade


def main():
    leituras = [62, 65, -1, 71, 80, -1, 77, 68]
    validas = limpar(leituras)
    pico = posicao_pico(validas)

    print("Originais:", leituras)                       # continua igual
    print("Válidas:", validas)
    print("Falhas do sensor:", len(leituras) - len(validas))
    print(f"Média: {media(validas):.1f}%")
    print(f"Pico: {validas[pico]}% (posição {pico} da lista de válidas)")
    print("Acima de 70%:", contar_acima(validas))             # usa o padrão
    print("Acima de 75%:", contar_acima(validas, limite=75))  # argumento nomeado


if __name__ == "__main__":
    main()
