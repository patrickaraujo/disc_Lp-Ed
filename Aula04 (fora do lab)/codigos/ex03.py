# Programa que lê um número inteiro e classifica a dificuldade
# correspondente: 1 = Fácil, 2 = Médio, 3 = Difícil.
# Exibe "Inválido" para qualquer valor fora de 1 a 3.


def main(num: int) -> None:
    match num:
        case 1:
            print("Fácil")
        case 2:
            print("Médio")
        case 3:
            print("Difícil")
        case _:
            print("Inválido")


if __name__ == "__main__":
    num = int(input("Digite um número: "))
    main(num)
