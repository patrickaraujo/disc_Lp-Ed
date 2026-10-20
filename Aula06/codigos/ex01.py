"""
Exercício 1 — Explorando uma lista

Peça ao usuário números inteiros, um por vez, até que ele digite 0
(o zero não entra na lista). O usuário deve digitar pelo menos 3 números.

Depois, mostre:
a) a lista completa e quantos números ela tem;
b) os 3 primeiros e os 3 últimos números, usando fatiamento (slicing);
c) a lista de trás para frente, usando um for com range decrescente;
d) uma nova lista com o quadrado de cada número, criada com
   compreensão de lista.

Saída esperada:
    Digite um número (0 para parar): 3
    Digite um número (0 para parar): 8
    Digite um número (0 para parar): 1
    Digite um número (0 para parar): 5
    Digite um número (0 para parar): 2
    Digite um número (0 para parar): 0
    Lista: [3, 8, 1, 5, 2] (5 números)
    3 primeiros: [3, 8, 1]
    3 últimos: [1, 5, 2]
    De trás para frente:
    2
    5
    1
    8
    3
    Quadrados: [9, 64, 1, 25, 4]
"""


def main():
    # ------------------------------------------------------------------
    # Leitura: não sabemos quantos números o usuário vai digitar,
    # então usamos while até que ele digite 0 (o zero não entra na lista).
    # ------------------------------------------------------------------
    numeros = []
    numero = int(input("Digite um número (0 para parar): "))
    while numero != 0:
        numeros.append(numero)
        numero = int(input("Digite um número (0 para parar): "))

    # Validação: o enunciado pede pelo menos 3 números
    if len(numeros) < 3:
        print("Digite pelo menos 3 números.")
        return

    # ------------------------------------------------------------------
    # a) Lista completa e quantidade de elementos
    # ------------------------------------------------------------------
    print(f"Lista: {numeros} ({len(numeros)} números)")

    # ------------------------------------------------------------------
    # b) Fatiamento (slicing)
    #    lista[início:fim] -> o índice 'fim' NÃO entra no resultado
    #    numeros[0:3]  -> posições 0, 1 e 2 (os 3 primeiros)
    #    numeros[-3:]  -> as 3 últimas posições (atalho elegante)
    # ------------------------------------------------------------------
    print("3 primeiros:", numeros[0:3])
    print("3 últimos:", numeros[-3:])

    # ------------------------------------------------------------------
    # c) De trás para frente com range decrescente
    #    range(início, fim, passo)
    #    - início: len(numeros) - 1  (último índice válido)
    #    - fim:    -1               (para ANTES do 0, pois o 0 também deve entrar)
    #    - passo:  -1               (decrementa de 1 em 1)
    # ------------------------------------------------------------------
    print("De trás para frente:")
    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i])

    # ------------------------------------------------------------------
    # d) Compreensão de lista: cria uma nova lista aplicando n * n
    #    para cada elemento 'n' da lista original.
    # ------------------------------------------------------------------
    quadrados = [n * n for n in numeros]
    print("Quadrados:", quadrados)


if __name__ == "__main__":
    main()
