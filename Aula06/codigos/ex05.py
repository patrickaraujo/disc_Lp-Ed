"""
Exercício 5 — Estoque da farmácia

Uma farmácia controla o estoque em um dicionário (produto: quantidade):

    estoque = {"dipirona": 100, "paracetamol": 50, "vitamina c": 30}

Leia movimentações até o usuário digitar "fim" no nome do produto.
Para cada movimentação, leia o produto e a quantidade:
- quantidade POSITIVA é entrada (compra);
- quantidade NEGATIVA é saída (venda).

Regras:
- produto que não existe e quantidade positiva: cadastre-o no estoque;
- produto que não existe e quantidade negativa: "Produto não cadastrado";
- saída maior que o estoque disponível: "Estoque insuficiente" (não altere).

Ao final, mostre:
- o estoque de cada produto;
- o total de unidades na farmácia (percorra values());
- uma LISTA com os produtos com estoque baixo (menos de 20 unidades).

Saída esperada:
    Produto (ou 'fim'): dipirona
    Quantidade (+ entrada / - saída): -90
    Produto (ou 'fim'): amoxicilina
    Quantidade (+ entrada / - saída): 15
    Produto (ou 'fim'): vitamina c
    Quantidade (+ entrada / - saída): -40
    Estoque insuficiente: há apenas 30 unidade(s).
    Produto (ou 'fim'): fim
    --- Estoque ---
    dipirona: 10
    paracetamol: 50
    vitamina c: 30
    amoxicilina: 15
    Total de unidades: 105
    Estoque baixo: ['dipirona', 'amoxicilina']
"""


def main():
    estoque = {"dipirona": 100, "paracetamol": 50, "vitamina c": 30}

    produto = input("Produto (ou 'fim'): ").strip().lower()
    while produto != "fim":
        quantidade = int(input("Quantidade (+ entrada / - saída): "))

        if produto not in estoque:
            if quantidade > 0:
                estoque[produto] = quantidade  # nova chave
            else:
                print("Produto não cadastrado.")
        elif estoque[produto] + quantidade < 0:
            print(f"Estoque insuficiente: há apenas "
                  f"{estoque[produto]} unidade(s).")
        else:
            estoque[produto] += quantidade

        produto = input("Produto (ou 'fim'): ").strip().lower()

    print("--- Estoque ---")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

    total = 0
    for quantidade in estoque.values():
        total += quantidade
    print("Total de unidades:", total)

    baixo = []
    for produto in estoque:
        if estoque[produto] < 20:
            baixo.append(produto)
    print("Estoque baixo:", baixo)


if __name__ == "__main__":
    main()
