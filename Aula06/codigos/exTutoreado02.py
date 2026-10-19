"""
Exercício Tutoreado 2 — Cantina da UNISA (dicionários)

A cantina guarda o cardápio em um dicionário: o NOME do item é a chave
e o PREÇO é o valor. Faça um programa que:

  a) Crie o cardápio, mostre-o e mostre o preço do café.
  b) Altere o preço do café e acrescente um novo item.
  c) Mostre as chaves, os valores e os pares (keys, values e items),
     e o cardápio formatado item a item.
  d) Pergunte um item ao cliente e informe o preço, verificando antes
     se ele existe (operador in) e depois usando get().
  e) Registre os pedidos do dia (até o usuário digitar "fim"), conte
     quantas vezes cada item foi pedido e mostre o mais vendido e o
     faturamento total.
  f) Use uma tupla como chave para guardar o preço de um combo.

Saída esperada (trecho):
    Cardápio: {'café': 4.5, 'pão de queijo': 6.0, 'suco': 7.0}
    Preço do café: R$ 4.50
    ...
    Pedido (ou 'fim'): café
    Pedido (ou 'fim'): suco
    Pedido (ou 'fim'): café
    Pedido (ou 'fim'): fim
    Contagem: {'café': 2, 'suco': 1}
    Mais vendido: café (2 pedidos)
    Faturamento: R$ 17.00
"""


def main():
    # a) Dicionário: {chave1: valor1, ..., chaveN: valorN}
    cardapio = {"café": 4.5, "pão de queijo": 6.0, "suco": 7.0}
    print("Cardápio:", cardapio)
    print(type(cardapio))

    # Acesso pela CHAVE (e não por posição, como nas listas)
    print("Preço do café: R$", format(cardapio["café"], ".2f"))
    # print(cardapio["pizza"])   # descomente: KeyError: 'pizza'

    # b) Atribuir a uma chave que EXISTE altera o valor;
    #    a uma chave que NÃO existe cria um novo par.
    cardapio["café"] = 5.0
    cardapio["coxinha"] = 8.0
    print("Cardápio atualizado:", cardapio)

    print("-" * 40)

    # c) Métodos keys(), values() e items()
    print("Itens:", list(cardapio.keys()))
    print("Preços:", list(cardapio.values()))
    print("Pares:", list(cardapio.items()))  # cada par é uma TUPLA

    # O for em um dicionário percorre as CHAVES...
    print("Só os nomes:")
    for item in cardapio:
        print(" ", item)

    # ...e com items() pegamos chave e valor ao mesmo tempo (desempacotamento)
    print("Cardápio completo:")
    for item, preco in cardapio.items():
        print(f"  {item}: R$ {preco:.2f}")

    print("-" * 40)

    # d) Consultando um item que talvez não exista
    escolha = input("Qual item você deseja? ").strip().lower()

    # Forma 1: verificar com 'in' antes de acessar (evita o KeyError)
    if escolha in cardapio:
        print(f"{escolha}: R$ {cardapio[escolha]:.2f}")
    else:
        print(f"Não temos '{escolha}'.")

    # Forma 2: get(chave, padrão) devolve o padrão se a chave não existir
    print("Usando get():", cardapio.get(escolha, "item indisponível"))
    print("get() sem padrão:", cardapio.get("pizza"))  # None

    print("-" * 40)

    # e) Contando com dicionário: a chave é o item, o valor é quantas
    #    vezes ele apareceu (mesma ideia do "Contando Letras" do slide)
    contagem = {}  # dicionário vazio
    pedido = input("Pedido (ou 'fim'): ").strip().lower()
    while pedido != "fim":
        if pedido not in cardapio:
            print("Item não existe no cardápio.")
        elif pedido in contagem:
            contagem[pedido] += 1
        else:
            contagem[pedido] = 1  # primeira vez: cria a chave
        pedido = input("Pedido (ou 'fim'): ").strip().lower()

    print("Contagem:", contagem)

    if len(contagem) > 0:
        # Procurando a chave com o maior valor
        mais_vendido = ""
        faturamento = 0
        for item, quantidade in contagem.items():
            if mais_vendido == "" or quantidade > contagem[mais_vendido]:
                mais_vendido = item
            faturamento += quantidade * cardapio[item]

        print(f"Mais vendido: {mais_vendido} ({contagem[mais_vendido]} pedidos)")
        print(f"Faturamento: R$ {faturamento:.2f}")

    print("-" * 40)

    # f) As chaves precisam ser IMUTÁVEIS: string, número ou TUPLA.
    #    Uma lista não pode ser chave, mas uma tupla pode.
    combos = {("café", "pão de queijo"): 9.0}
    # combos[["suco", "coxinha"]] = 12.0   # descomente: TypeError (lista)
    combos[("suco", "coxinha")] = 13.0
    for combo, preco in combos.items():
        # combo é uma tupla: acessamos seus elementos por índice
        print(f"Combo {combo[0]} + {combo[1]}: R$ {preco:.2f}")


if __name__ == "__main__":
    main()
