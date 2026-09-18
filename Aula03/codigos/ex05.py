"""
Exercício 5 — Par/Ímpar e Comparação de Dois Números
 
Peça ao usuário um número inteiro, verifique se ele é par ou ímpar
e exiba o resultado na tela.
Em seguida, solicite dois novos números inteiros, compare-os e informe
qual deles é o maior, ou se ambos são iguais.
"""
 
def main():
    # Parte 1: Verificar se um número é par ou ímpar
    n = int(input("Digite um número: "))
 
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
 
    print("-" * 30)  # Separador visual para organizar a saída no console
 
    # Parte 2: Comparar dois números
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))
 
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    else:
        if n2 > n1:
            print(f"{n2} é maior que {n1}")
        else:
            print("Os dois números são iguais")
 
if __name__ == "__main__":
    main()
