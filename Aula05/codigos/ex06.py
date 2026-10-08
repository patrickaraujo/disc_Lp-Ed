"""
Exercício — Soma dos 50 primeiros números pares
 
Faça um programa que calcule e mostre a soma dos 50 primeiros
números pares (2, 4, 6, ..., 100).
 
Resolva o problema de duas formas: usando while e usando for.
 
Saída esperada:
    Soma com while: 2550
    Soma com for: 2550
"""
 
 
def main():
    soma = 0
 
    # range(2, 101, 2) gera 2, 4, 6, ..., 100
    for par in range(2, 101, 2):
        soma += par
    
    print(f"Soma com while: {soma}")
    
    
    soma = 0
    contador = 1  # Quantos pares já foram somados
 
    while contador <= 50:
        par = contador * 2
        soma += par
        contador += 1
 
    print(f"Soma com for: {soma}")
 
if __name__ == "__main__":
    main()
