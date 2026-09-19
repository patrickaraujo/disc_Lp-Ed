# Programa que lê uma letra e classifica como "Vogal" ou "Consoante".
# As vogais (a, e, i, o, u) são verificadas individualmente com match/case;
# qualquer outra letra é classificada como consoante.


def classificar_letra(letra: str) -> None:
    match letra:
        case "a":
            print("Vogal")
        case "e":
            print("Vogal")
        case "i":
            print("Vogal")
        case "o":
            print("Vogal")
        case "u":
            print("Vogal")
        case _:
            print("Consoante")


if __name__ == "__main__":
    letra = input("Digite uma letra: ")
    classificar_letra(letra)
