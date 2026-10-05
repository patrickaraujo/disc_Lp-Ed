# Exercicio Tutoreado 1
# Faca um programa que leia a altura e o peso de uma pessoa. De acordo com a
# tabela a seguir, verifique e mostre qual a classificacao dessa pessoa:
#                 Peso
#            Ate 60   Entre 60-90 (inclusive)   Acima de 90
# Altura < 1,20    A            D                    G
# 1,20 - 1,70      B            E                    H
# Maior que 1,70   C            F                    I
 
 
def main():
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
 
    if altura < 1.20:
        if peso <= 60:
            classe = "A"
        elif peso <= 90:
            classe = "D"
        else:
            classe = "G"
    elif altura <= 1.70:
        if peso <= 60:
            classe = "B"
        elif peso <= 90:
            classe = "E"
        else:
            classe = "H"
    else:
        if peso <= 60:
            classe = "C"
        elif peso <= 90:
            classe = "F"
        else:
            classe = "I"
 
    print("Classificacao:", classe)
 
 
if __name__ == "__main__":
    main()
