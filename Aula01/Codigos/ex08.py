'''
Faça um algoritmo que leia um valor em reais (R$) e a cotação do dólar, e calcule quantos dólares a pessoa poderá comprar.
'''

def main():
    reais = float(input("Digite o valor em reais (R$): "))
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    dolares = reais / cotacao_dolar
    print(f"Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f}")

if __name__ == "__main__":
    main()
