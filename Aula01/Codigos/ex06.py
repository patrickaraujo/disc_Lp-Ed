'''
Faça um algoritmo que leia uma temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = (C × 1,8) + 32
'''

def main():
    # Alterado para float para aceitar temperaturas com casas decimais
    graus = float(input("Qual a temperatura em Celsius? "))
    conversao = (graus * 1.8) + 32
    print(f"A temperatura em Fahrenheit é: {conversao}")

if __name__ == "__main__":
    main()
