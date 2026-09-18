"""
Exercício 4 — Positivo, Negativo, Zero, Par ou Ímpar
 
Peça um número inteiro.
Se o número for positivo, verifique se é par ou ímpar.
Se o número for negativo, mostre "Número negativo".
Se for zero, mostre "Zero não é positivo nem negativo".
"""
 
 
def main():
    # Solicita um número inteiro ao usuário
    numero = int(input("Digite um número inteiro: "))
 
    # Verifica se o número é positivo
    if numero > 0:
 
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print("Número positivo e par")
        else:
            print("Número positivo e ímpar")
 
    # Verifica se o número é negativo
    else:
        if numero < 0:
            print("Número negativo")
 
        # Caso o número seja zero
        else:
            print("Zero não é positivo nem negativo")
 
if __name__ == "__main__":
    main()
