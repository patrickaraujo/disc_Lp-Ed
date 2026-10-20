"""
Exercício 4 — Contador de palavras

Leia uma frase e conte quantas vezes cada palavra aparece, usando um
dicionário em que a PALAVRA é a chave e a QUANTIDADE é o valor.
Considere maiúsculas e minúsculas como iguais ("Python" = "python").

Ao final:
- mostre cada palavra e sua quantidade (use items());
- mostre quantas palavras DIFERENTES a frase tem;
- mostre a palavra mais frequente (em caso de empate, qualquer uma);
- peça uma palavra ao usuário e informe quantas vezes ela aparece,
  usando get() (se não aparecer, deve mostrar 0).

Dica: frase.split() devolve uma lista com as palavras da frase.

Saída esperada:
    Digite uma frase: o rato roeu a roupa do rei e o rei riu
    o: 2
    rato: 1
    roeu: 1
    a: 1
    roupa: 1
    do: 1
    rei: 2
    e: 1
    riu: 1
    Palavras diferentes: 9
    Mais frequente: o (2 vezes)
    Qual palavra deseja consultar? rato
    'rato' aparece 1 vez(es)
"""


def main():
    frase = input("Digite uma frase: ").lower()
    palavras = frase.split()

    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")

    print("Palavras diferentes:", len(contagem))

    mais_frequente = ""
    for palavra in contagem:
        if mais_frequente == "" or contagem[palavra] > contagem[mais_frequente]:
            mais_frequente = palavra

    if mais_frequente != "":
        print(f"Mais frequente: {mais_frequente} "
              f"({contagem[mais_frequente]} vezes)")

    busca = input("Qual palavra deseja consultar? ").strip().lower()
    print(f"'{busca}' aparece {contagem.get(busca, 0)} vez(es)")


if __name__ == "__main__":
    main()
