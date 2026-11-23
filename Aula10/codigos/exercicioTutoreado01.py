"""
Exercício Tutoreado 1 — Pedidos da lanchonete (dicionários + tuplas + funções)

Uma lanchonete guarda o cardápio e o estoque em dois dicionários:

    cardapio = {código: (nome, preço)}     <- o valor é uma TUPLA
    estoque  = {código: quantidade}

Um pedido é uma lista de tuplas (código, quantidade). Faça um programa que:

  a) Crie a função atender(pedido, cardapio, estoque), que percorre o
     pedido e, para cada item:
       - se o código não existir no cardápio: "código inexistente";
       - se não houver estoque suficiente: "estoque insuficiente";
       - senão: dá baixa no estoque e soma o valor ao total.
     A função devolve o total do pedido.
  b) Crie a função estoque_baixo(estoque, cardapio, limite=2), que devolve
     uma lista com os nomes dos produtos com quantidade <= limite.
  c) Mostre o total e os produtos com estoque baixo.

Saída esperada:
    101 x2 -> X-salada: R$ 36.00
    104 x1 -> Açaí: estoque insuficiente (há 0)
    102 x3 -> Pastel: estoque insuficiente (há 2)
    999 x1 -> código inexistente
    103 x2 -> Suco: R$ 14.00
    Total do pedido: R$ 50.00
    Estoque baixo: ['Pastel', 'Açaí']
"""


def atender(pedido, cardapio, estoque):
    total = 0
    # Cada item do pedido é uma tupla (código, quantidade):
    # o for já DESEMPACOTA a tupla em duas variáveis.
    for codigo, qtd in pedido:
        # Operador in em dicionário: verifica se a CHAVE existe.
        if codigo not in cardapio:
            print(f"{codigo} x{qtd} -> código inexistente")
            continue                      # passa para o próximo item

        nome, preco = cardapio[codigo]    # desempacota a tupla (nome, preço)

        # get(chave, padrão): devolve o padrão se a chave não existir
        disponivel = estoque.get(codigo, 0)
        if qtd > disponivel:
            print(f"{codigo} x{qtd} -> {nome}: estoque insuficiente (há {disponivel})")
        else:
            estoque[codigo] = disponivel - qtd    # atualiza o valor da chave
            valor = preco * qtd
            total = total + valor
            print(f"{codigo} x{qtd} -> {nome}: R$ {valor:.2f}")
    return total


def estoque_baixo(estoque, cardapio, limite=2):
    baixos = []
    # items() devolve os pares (chave, valor) do dicionário
    for codigo, qtd in estoque.items():
        if qtd <= limite:
            nome = cardapio[codigo][0]    # [0] = 1º elemento da tupla (nome)
            baixos.append(nome)
    return baixos


def main():
    cardapio = {
        101: ("X-salada", 18.0),
        102: ("Pastel", 9.5),
        103: ("Suco", 7.0),
        104: ("Açaí", 15.0),
    }
    estoque = {101: 5, 102: 2, 103: 10, 104: 0}
    pedido = [(101, 2), (104, 1), (102, 3), (999, 1), (103, 2)]

    total = atender(pedido, cardapio, estoque)
    print(f"Total do pedido: R$ {total:.2f}")
    print("Estoque baixo:", estoque_baixo(estoque, cardapio))

    # Para pensar: por que o preço está numa TUPLA e o estoque num
    # dicionário separado? A tupla (nome, preço) não muda durante o
    # atendimento; o estoque muda a cada venda.
    # Tente fazer cardapio[101][1] = 20.0 e veja o erro: tuplas são imutáveis.
    # Para mudar o preço, troque a tupla inteira:
    #     cardapio[101] = ("X-salada", 20.0)


if __name__ == "__main__":
    main()
