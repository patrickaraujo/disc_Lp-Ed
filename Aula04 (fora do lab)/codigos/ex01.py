# Programa que lê um mês informado pelo usuário e exibe
# a sua abreviação (Jan, Fev, Mar, ...). Usa match/case para
# tratar cada número de 1 a 12 e exibe "Invalido" para
# qualquer outra entrada.


def mostrar_mes(mes: str) -> None:
    match mes:
        case "1":
            print("Jan")
        case "2":
            print("Fev")
        case "3":
            print("Mar")
        case "4":
            print("Abr")
        case "5":
            print("Mai")
        case "6":
            print("Jun")
        case "7":
            print("Jul")
        case "8":
            print("Ago")
        case "9":
            print("Set")
        case "10":
            print("Out")
        case "11":
            print("Nov")
        case "12":
            print("Dez")
        case _:
            print("Invalido")


if __name__ == "__main__":
    mes = input("Digite um mês: ")
    mostrar_mes(mes)
