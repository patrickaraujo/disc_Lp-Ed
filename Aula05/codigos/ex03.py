"""
Exercício 4 — Classificação da Temperatura
 
Faça um programa que solicite uma temperatura em graus Celsius e classifique:
- Menor que 10°C: Muito frio
- Entre 10°C e 20°C: Frio
- Entre 21°C e 30°C: Agradável
- Acima de 30°C: Calor
 
Saída esperada:
    Classificação: Agradável
"""
 
 
def main():
    # Solicita a temperatura ao usuário
    temperatura = float(input("Digite a temperatura em °C: "))
 
    # Classifica a temperatura
    if temperatura < 10:
        classificacao = "Muito frio"
    elif temperatura <= 20:
        classificacao = "Frio"
    elif temperatura <= 30:
        classificacao = "Agradável"
    else:
        classificacao = "Calor"
 
    # Exibe o resultado
    print(f"Classificação: {classificacao}")
 
 
if __name__ == "__main__":
    main()
