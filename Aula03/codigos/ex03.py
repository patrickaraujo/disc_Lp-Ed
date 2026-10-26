"""
Exercício 3 — Carteira de Motorista

Peça a idade de uma pessoa.
Se for maior ou igual a 18 anos, verifique se possui carteira de motorista (CNH):
    - Se sim, mostre "Pode dirigir".
    - Se não, mostre "Precisa tirar a carteira".

Se for menor de 18 anos, mostre "Não pode dirigir".
"""


def main():
    # Solicita a idade ao usuário
    idade = int(input("Digite sua idade: "))

    # Verifica se a pessoa é maior de idade
    if idade >= 18:

        # Só faz sentido perguntar sobre a CNH para quem tem 18 anos ou mais.
        # lower() e strip() aceitam respostas como "Sim" ou " sim "
        cnh = input("Você possui carteira de motorista? (sim/não): ").strip().lower()

        # if aninhado: verifica se possui CNH
        if cnh == "sim":
            print("Pode dirigir")
        else:
            print("Precisa tirar a carteira")

    # Menor de 18 anos
    else:
        print("Não pode dirigir")


if __name__ == "__main__":
    main()
