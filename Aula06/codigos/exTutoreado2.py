"""
Exercício Tutoreado 2 — Cantina da UNISA (dicionários)

>>> VERSÃO GUIA: siga os passos e escreva o código logo abaixo de cada
>>> comentário. Rode o programa ao final de cada passo para conferir.

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
"""


def main():
    # -----------------------------------------------------------------
    # PASSO 1 — Criando e acessando um dicionário
    # Sintaxe: nome = {chave1: valor1, chave2: valor2, ...}
    # -----------------------------------------------------------------

    # 1.1 Crie o dicionário 'cardapio' com:
    #     "café" custa 4.5 | "pão de queijo" custa 6.0 | "suco" custa 7.0

    # 1.2 Mostre o cardápio inteiro e o type() dele.

    # 1.3 Mostre o preço do café com 2 casas decimais.
    #     Dica: no dicionário, acessamos pela CHAVE -> cardapio["..."]

    # 1.4 Tente mostrar cardapio["pizza"]. Rode e leia o erro.
    #     Qual é o nome dele? Depois, transforme a linha em comentário.

    # Saída esperada do Passo 1:
    #   Cardápio: {'café': 4.5, 'pão de queijo': 6.0, 'suco': 7.0}
    #   <class 'dict'>
    #   Preço do café: R$ 4.50

    # -----------------------------------------------------------------
    # PASSO 2 — Alterando e incluindo itens
    # -----------------------------------------------------------------

    # 2.1 O café aumentou: mude o preço dele para 5.0.

    # 2.2 Inclua o item "coxinha" custando 8.0.
    #     Pergunta: qual a diferença entre o código do 2.1 e o do 2.2?

    # 2.3 Mostre o cardápio atualizado.

    # Saída esperada do Passo 2:
    #   Cardápio atualizado: {'café': 5.0, 'pão de queijo': 6.0, 'suco': 7.0, 'coxinha': 8.0}

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 3 — keys(), values(), items() e o laço for
    # -----------------------------------------------------------------

    # 3.1 Mostre, convertidos em lista com list():
    #     - as chaves (keys);
    #     - os valores (values);
    #     - os pares (items). De que tipo é cada par?

    # 3.2 Faça um for direto no dicionário (for item in cardapio)
    #     e mostre cada elemento. O for percorre as chaves ou os valores?

    # 3.3 Agora faça um for com items(), pegando a chave E o valor ao
    #     mesmo tempo, e mostre cada item no formato "café: R$ 5.00".
    #     Dica: for item, preco in cardapio.items():

    # Saída esperada do Passo 3:
    #   Itens: ['café', 'pão de queijo', 'suco', 'coxinha']
    #   Preços: [5.0, 6.0, 7.0, 8.0]
    #   Pares: [('café', 5.0), ('pão de queijo', 6.0), ('suco', 7.0), ('coxinha', 8.0)]
    #   Só os nomes:
    #     café
    #     ...
    #   Cardápio completo:
    #     café: R$ 5.00
    #     ...

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 4 — Consultando um item que talvez não exista
    # -----------------------------------------------------------------

    # 4.1 Leia em 'escolha' o item que o cliente deseja
    #     (use .strip().lower() para limpar o texto).

    # 4.2 FORMA 1: use o operador 'in' para verificar se a escolha está
    #     no cardápio. Se estiver, mostre o preço; se não, mostre
    #     "Não temos '<escolha>'."

    # 4.3 FORMA 2: mostre o preço usando get(), com o valor padrão
    #     "item indisponível" para quando o item não existir.

    # 4.4 Mostre cardapio.get("pizza"), sem valor padrão. O que aparece?

    # Saída esperada do Passo 4 (digitando "suco"):
    #   suco: R$ 7.00
    #   Usando get(): 7.0
    #   get() sem padrão: None

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 5 — Contando os pedidos com um dicionário
    # Ideia: a CHAVE é o item; o VALOR é quantas vezes ele foi pedido.
    # -----------------------------------------------------------------

    # 5.1 Crie o dicionário 'contagem' vazio.

    # 5.2 Leia o primeiro 'pedido' (com .strip().lower()).

    # 5.3 Enquanto o pedido for diferente de "fim":
    #     - se o pedido NÃO estiver no cardápio: "Item não existe no cardápio."
    #     - senão, se o pedido JÁ estiver em 'contagem': some 1 no valor;
    #     - senão (primeira vez): crie a chave com valor 1.
    #     - no final do laço, leia o próximo pedido.

    # 5.4 Mostre o dicionário 'contagem'.

    # 5.5 Se 'contagem' não estiver vazio (len > 0), percorra
    #     contagem.items() para descobrir:
    #     - o item mais vendido (comece com mais_vendido = "" e troque
    #       sempre que achar uma quantidade maior);
    #     - o faturamento: some quantidade * preço do item no cardápio.
    #     Mostre os dois.

    # Saída esperada do Passo 5 (pedidos: café, suco, café, pizza, fim):
    #   Item não existe no cardápio.
    #   Contagem: {'café': 2, 'suco': 1}
    #   Mais vendido: café (2 pedidos)
    #   Faturamento: R$ 17.00

    print("-" * 40)

    # -----------------------------------------------------------------
    # PASSO 6 — Tupla como chave
    # As chaves precisam ser IMUTÁVEIS: string, número ou tupla.
    # -----------------------------------------------------------------

    # 6.1 Crie o dicionário 'combos' com a chave ("café", "pão de queijo")
    #     valendo 9.0.

    # 6.2 Tente incluir um combo usando uma LISTA como chave:
    #     combos[["suco", "coxinha"]] = 12.0
    #     Rode e leia o erro. Depois, transforme a linha em comentário.

    # 6.3 Inclua o combo ("suco", "coxinha") valendo 13.0, agora com tupla.

    # 6.4 Percorra combos.items() e mostre cada combo no formato
    #     "Combo café + pão de queijo: R$ 9.00".
    #     Dica: a chave é uma tupla, então combo[0] e combo[1].

    # Saída esperada do Passo 6:
    #   Combo café + pão de queijo: R$ 9.00
    #   Combo suco + coxinha: R$ 13.00


if __name__ == "__main__":
    main()
