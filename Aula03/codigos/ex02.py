"""
Exercício 2 — Número Positivo ou Negativo
 
Leia um número inteiro e informe se ele é positivo ou negativo.
Considere zero como um valor positivo.
Utilize uma estrutura if/else para realizar a verificação.
"""
 
 
def main():
    n = int(input("Digite um número inteiro: "))
 
    if n >= 0:
        print("O valor é positivo")
    else:
        print("O valor é negativo")
 
 
if __name__ == "__main__":
    main()
