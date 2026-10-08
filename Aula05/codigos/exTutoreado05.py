# Exercício Tutoreado 5
# Escreva um programa que leia repetidamente a idade de nadadores e classifique
# cada um em uma das seguintes categorias:
#   Infantil A: 5-7 | Infantil B: 8-10 | Juvenil A: 11-13 | Juvenil B: 14-17 | Senior: >= 18
# A leitura deve continuar ate que o usuario digite 0, valor que encerra o
# programa sem ser classificado.
 
 
def main():
    idade = int(input("Idade do nadador (0 para sair): "))
 
    while idade != 0:
        if idade < 5:
            print("Sem categoria (abaixo de 5 anos)")
        elif idade <= 7:
            print("Infantil A")
        elif idade <= 10:
            print("Infantil B")
        elif idade <= 13:
            print("Juvenil A")
        elif idade <= 17:
            print("Juvenil B")
        else:
            print("Senior")
 
        idade = int(input("Idade do nadador (0 para sair): "))
 
    print("Programa encerrado.")
 
 
if __name__ == "__main__":
    main()
