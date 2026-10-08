"""
Exercício 1 — Classificação Etária e Preço do Ingresso
 
Em um cinema, o preço do ingresso varia de acordo com a faixa etária do cliente.
Faça um programa que leia a idade de uma pessoa e exiba sua classificação
e o preço do ingresso correspondente:
 
- 0 a 12 anos:     Criança      — R$ 10,00
- 13 a 17 anos:    Adolescente  — R$ 15,00
- 18 a 59 anos:    Adulto       — R$ 20,00
- 60 anos ou mais: Idoso        — R$ 12,00
 
Caso a idade informada seja negativa, exiba a mensagem "Idade inválida."
 
Saída esperada:
    Classificação: Adulto
    Preço do ingresso: R$ 20,00
"""
 
 
def main():
    # Solicita a idade ao usuário
    idade = int(input("Digite sua idade: "))
 
    # Valida a entrada
    if idade < 0:
        print("Idade inválida.")
        return
 
    # Define a classificação e o preço de acordo com a idade
    if idade <= 12:
        classificacao = "Criança"
        preco = 10.00
    elif idade <= 17:
        classificacao = "Adolescente"
        preco = 15.00
    elif idade <= 59:
        classificacao = "Adulto"
        preco = 20.00
    else:
        classificacao = "Idoso"
        preco = 12.00
 
    # Formata o preço no padrão brasileiro (vírgula como separador decimal)
    preco_formatado = f"{preco:.2f}".replace(".", ",")
 
    # Exibe o resultado
    print(f"Classificação: {classificacao}")
    print(f"Preço do ingresso: R$ {preco_formatado}")
 
 
if __name__ == "__main__":
    main()
