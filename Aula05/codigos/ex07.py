"""
Exercício 6 — Soma acumulada
 
Peça ao usuário números inteiros, um por vez.
 
Continue pedindo números até que o usuário
digite 0.
 
Ao final, mostre a soma de todos os números
digitados, exceto o zero.
"""
 
 
def main():
    soma = 0
 
    numero = int(input("Digite um número: "))
 
    while numero != 0:
        soma += numero
 
        numero = int(input("Digite um número: "))
 
    print(f"Soma total = {soma}")
 
 
if __name__ == "__main__":
    main()
