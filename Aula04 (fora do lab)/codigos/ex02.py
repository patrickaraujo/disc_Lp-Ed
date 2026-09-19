# Programa que lê uma operação matemática (+, -, *, /) e dois
# números, realizando o cálculo correspondente com match/case.
# Exibe "Invalido" para qualquer operação não reconhecida.


def main(op: str, num1: float, num2: float) -> None:
    match op:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case _:
            print("Invalido")


if __name__ == "__main__":
    op = input("Digite a operacao: ")
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite um numero: "))
    main(op, num1, num2)
