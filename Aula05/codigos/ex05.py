def main():
    '''
        Crie um programa que solicite ao usuário um número inteiro e utilize 
        um laço de repetição do tipo while para calcular e exibir a sua tabuada 
        completa, multiplicando o número digitado por todos os valores de 1 a 10 
        de forma organizada.
    '''
    
    # Variável contadora iniciada em 1
    multiplicador = 1
    n = int(input("Digite um número para ver a tabuada: "))
 
    # Laço de repetição enquanto o contador for menor ou igual a 10
    while multiplicador <= 10:
        resultado = n * multiplicador
        # Uso de f-string para deixar a saída mais limpa e organizada
        print(f"{n} x {multiplicador} = {resultado}")
        
        # Incrementa o contador (também poderia ser escrito como c += 1)
        multiplicador = multiplicador + 1
 
 
if __name__ == "__main__":
    main()
