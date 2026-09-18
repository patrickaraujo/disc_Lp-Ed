"""
Exercício 1 — Soma de dois números
 
Peça ao usuário dois números inteiros e calcule a soma entre eles.
Em seguida, verifique se o resultado da soma é maior que 20.
Saída esperada
 
A soma é maior que 20? True
 
ou
 
A soma é maior que 20? False
"""
 
def main():
    num1 = float(input("Digite o primeiro número:\t"))
    num2 = float(input("Digite o segundo número:\t"))
    limite = 20
    verificar = (num1+num2)>limite
    print(f"A soma de {num1} e {num2} é igual a {num1+num2}")
    print(f"{num1+num2} é maior que {limite}?:\t{verificar}")
    
if __name__ == "__main__":
    main()
