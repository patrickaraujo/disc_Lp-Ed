'''
Faça um algoritmo que leia a base e a altura de um retângulo e calcule sua área.
'''

def main():
    base = int(input("Digite o valor da base do retângulo: "))
    altura = int(input("Digite o valor da altura do retângulo: "))
    area_retangulo = base * altura
    print(f"Esta é a área do retângulo: {area_retangulo}")

if __name__ == "__main__":
    main()
