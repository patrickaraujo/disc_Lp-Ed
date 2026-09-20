"""
Exercício 7 — Situação do Aluno
 
Peça a média final do aluno e o percentual de faltas.
 
Se a média for maior ou igual a 7:
- Se tiver menos de 25% de faltas, mostre "Aprovado".
- Caso contrário, mostre "Reprovado por falta".
 
Se a média for menor que 7, mostre:
"Reprovado por nota".
 
Saída esperada:
    Situação: Aprovado
"""
 
def main():
    # Solicita a média final do aluno
    media = float(input("Digite a média final do aluno: "))
 
    # Solicita o percentual de faltas
    faltas = float(input("Digite o percentual de faltas: "))
 
    # Verifica se os valores são válidos
    if media < 0 or media > 10:
        print("Média inválida.")
        return
 
    if faltas < 0 or faltas > 100:
        print("Percentual de faltas inválido.")
        return
 
    # Verifica primeiro a média do aluno
    if media >= 7:
 
        # Se a média for suficiente, verifica as faltas
        if faltas < 25:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado por falta"
 
    else:
        situacao = "Reprovado por nota"
 
    # Exibe o resultado
    print(f"Situação: {situacao}")
 
if __name__ == "__main__":
    main()
