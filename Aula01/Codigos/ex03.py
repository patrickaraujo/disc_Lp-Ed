'''
Faça um algoritmo que leia o valor do lado de um quadrado e calcule o seu perímetro.
'''

def main():
    lado = int(input("Digite o valor do lado do quadrado: "))
    perimetro = lado * 4
    print(f"O perímetro do quadrado é: {perimetro}")

if __name__ == "__main__":
    main()
