"""
Exercício 3 — Conversão de Nota para Conceito
 
Faça um programa que receba uma nota de 0 a 100 e converta para:
- 0 a 49: Conceito D
- 50 a 69: Conceito C
- 70 a 89: Conceito B
- 90 a 100: Conceito A
 
Saída esperada:
    Conceito: B
"""
 
 
def main():
    # Solicita a nota ao usuário
    nota = float(input("Digite uma nota de 0 a 100: "))
 
    # Verifica se a nota é válida e define o conceito
    if nota < 0 or nota > 100:
        print("Nota inválida.")
        return
    elif nota < 50:
        conceito = "D"
    elif nota < 70:
        conceito = "C"
    elif nota < 90:
        conceito = "B"
    else:
        conceito = "A"
 
    # Exibe o resultado
    print(f"Conceito: {conceito}")
 
 
if __name__ == "__main__":
    main()
