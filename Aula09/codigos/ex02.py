"""
Exercício 2 — Desconto progressivo

Uma loja dá desconto de acordo com o valor da compra:
    a partir de R$ 1000,00 -> 15%
    a partir de R$ 500,00  -> 10%
    a partir de R$ 200,00  -> 5%
    abaixo de R$ 200,00    -> sem desconto

Clientes com cartão fidelidade ganham mais 5 pontos percentuais, mas
SOMENTE se a compra for de pelo menos R$ 200,00.

Leia o valor da compra e se o cliente tem cartão (s/n). Mostre o
percentual de desconto, o valor do desconto e o valor final.

Pergunta (responda em comentário no código): o que aconteceria se o
teste "valor >= 200" fosse o PRIMEIRO do if-elif? Teste com R$ 1500,00.

Saída esperada:
    Valor da compra: 650
    Tem cartão fidelidade (s/n)? s
    Desconto: 15%
    Valor do desconto: R$ 97.50
    Valor final: R$ 552.50
"""


def main():
    valor = float(input("Valor da compra: "))
    cartao = input("Tem cartão fidelidade (s/n)? ")

    # A ordem vai da faixa MAIOR para a menor: o if-elif para no primeiro
    # teste verdadeiro. Se "valor >= 200" viesse primeiro, uma compra de
    # R$ 1500,00 entraria nele (1500 >= 200 é True) e ganharia só 5%.
    if valor >= 1000:
        percentual = 15
    elif valor >= 500:
        percentual = 10
    elif valor >= 200:
        percentual = 5
    else:
        percentual = 0

    # and: as DUAS condições precisam ser verdadeiras
    if cartao == "s" and valor >= 200:
        percentual = percentual + 5

    desconto = valor * percentual / 100
    print(f"Desconto: {percentual}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor - desconto:.2f}")


if __name__ == "__main__":
    main()
