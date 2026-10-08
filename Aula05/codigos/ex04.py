"""
Exercício 5 — Classificação da Velocidade da Internet
 
Faça um programa que solicite a velocidade da internet em Mbps e classifique:
- Até 10 Mbps: Lenta
- De 11 a 50 Mbps: Média
- De 51 a 200 Mbps: Rápida
- Acima de 200 Mbps: Ultra Rápida
 
Saída esperada:
    Classificação: Rápida
"""
 
 
def main():
    # Solicita a velocidade da internet ao usuário
    velocidade = float(input("Digite a velocidade da internet em Mbps: "))
 
    # Verifica se a velocidade é válida
    if velocidade < 0:
        print("Velocidade inválida.")
        return
 
    # Classifica a velocidade da internet
    if velocidade <= 10:
        classificacao = "Lenta"
    elif velocidade <= 50:
        classificacao = "Média"
    elif velocidade <= 200:
        classificacao = "Rápida"
    else:
        classificacao = "Ultra Rápida"
 
    # Exibe o resultado
    print(f"Classificação: {classificacao}")
 
 
if __name__ == "__main__":
    main()
