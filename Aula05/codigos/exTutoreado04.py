"""
Exercício 5 (Exercício Tutoreado 4) — Contagem simples
 
Crie um programa que mostre na tela:
 - os números de 0 até 9, um por linha.
 - os números de 1 até 10, um por linha.
 - os números de 9 até 0, um por linha.
 - os números pares de 2 até 12, um por linha.
 
Use um laço de repetição for.
"""
 
 
def main():
 
    # Números de 0 até 9
    for numero in range(10):
        print(numero)
 
    # Números de 1 até 10
    for numero in range(1, 11):
        print(numero)
 
    # Números de 9 até 0
    for numero in range(9, -1, -1):
        print(numero)
 
    # Números pares de 2 até 12
    for numero in range(2, 13, 2):
        print(numero)
 
 
if __name__ == "__main__":
    main()
