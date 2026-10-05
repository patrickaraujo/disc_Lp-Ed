# Exercicio 15 (Aula 4) - DIFICIL
# Faca um programa que leia os coeficientes de uma equacao do segundo grau.
# Em seguida, calcule e mostre as raizes dessa equacao, lembrando que as raizes
# sao calculadas como: x = (-b +/- raiz(delta)) / (2 * a), em que delta = b^2 - 4*a*c
# A variavel a tem de ser diferente de zero. Caso seja igual, imprima a mensagem
# "Nao e equacao de segundo grau". Do contrario, imprima:
#   Se delta < 0, nao existe raiz real. Imprima: "Nao existe raiz"
#   Se delta = 0, existe uma raiz real. Imprima a raiz e: "Raiz unica"
#   Se delta > 0, existem duas raizes reais. Imprima as raizes
 
 
def main():
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
 
    if a == 0:
        print("Nao e equacao de segundo grau.")
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print("Nao existe raiz")
        elif delta == 0:
            raiz = -b / (2 * a)
            print("Raiz unica:", raiz)
        else:
            r1 = (-b + delta**0.5) / (2 * a)
            r2 = (-b - delta**0.5) / (2 * a)
            print("Duas raizes reais:", r1, "e", r2)
 
 
if __name__ == "__main__":
    main()
