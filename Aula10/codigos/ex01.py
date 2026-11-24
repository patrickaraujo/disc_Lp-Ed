"""
Exercício 1 — Contador de palavras

Leia uma frase e conte quantas vezes cada palavra aparece, usando um
dicionário {palavra: quantidade}. Ignore maiúsculas/minúsculas e os
sinais de pontuação . , ! ? no fim das palavras.

Mostre:
  - cada palavra com sua contagem, na ordem em que apareceu;
  - a palavra mais frequente (em caso de empate, a que apareceu primeiro);
  - quantas palavras aparecem uma única vez.

Não use a classe Counter nem as funções max() e sorted().

Saída esperada:
    Frase: O rato roeu a roupa do rei de Roma, e o rei roeu a rolha!
    o: 2
    rato: 1
    roeu: 2
    a: 2
    roupa: 1
    do: 1
    rei: 2
    de: 1
    roma: 1
    e: 1
    rolha: 1
    Mais frequente: "o" (2 vezes)
    Palavras que aparecem uma única vez: 7
"""


def contar_palavras(frase):
    contagem = {}
    # lower() -> tudo minúsculo; split() -> lista de palavras
    for palavra in frase.lower().split():
        palavra = palavra.strip(".,!?")   # tira a pontuação das pontas
        # get(palavra, 0): se a palavra ainda não é chave, começa do 0
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem


def mais_frequente(contagem):
    melhor = ""
    maior = 0
    for palavra, qtd in contagem.items():
        if qtd > maior:          # > (e não >=): no empate, fica a primeira
            maior = qtd
            melhor = palavra
    return melhor, maior          # devolve uma tupla


def main():
    frase = input("Frase: ")
    contagem = contar_palavras(frase)

    for palavra, qtd in contagem.items():
        print(f"{palavra}: {qtd}")

    palavra, vezes = mais_frequente(contagem)   # desempacota a tupla
    print(f'Mais frequente: "{palavra}" ({vezes} vezes)')

    unicas = 0
    for qtd in contagem.values():
        if qtd == 1:
            unicas = unicas + 1
    print("Palavras que aparecem uma única vez:", unicas)


if __name__ == "__main__":
    main()
