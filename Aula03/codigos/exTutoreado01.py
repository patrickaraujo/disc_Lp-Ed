"""
Exercício Tutoreado 1 — Aprovação por Média e Faltas
 
Peça a média final do aluno e a porcentagem de faltas.
Se a média for maior ou igual a 7, verifique as faltas:
    - Se tiver menos de 25% de faltas, mostre "Aprovado".
    - Caso contrário, mostre "Reprovado por falta".
Se a média for menor que 7, mostre "Reprovado por nota".
"""
 
 
def main():
    media = float(input("Digite a sua média: "))
    percentFaltas = int(input("Digite a porcentagem de faltas: "))
 
    if media >= 7:
        if percentFaltas < 25:
            print("Aprovado!")
        else:
            print("Reprovado por falta!")
    else:
        print("Reprovado por nota!")
 
 
if __name__ == "__main__":
    main()
