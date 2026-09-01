'''
Faça um algoritmo que leia a quantidade de horas trabalhadas e o valor pago por hora, e calcule o salário final.
'''

def main():
    horas = float(input("Digite suas horas trabalhadas: "))
    valor = float(input("Digite o valor pago por hora: "))
    salario = horas * valor
    # Formatação com 2 casas decimais para valores monetários
    print(f"O valor do salário é: R$ {salario:.2f}")

if __name__ == "__main__":
    main()
