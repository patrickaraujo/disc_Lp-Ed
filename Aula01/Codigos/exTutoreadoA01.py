    '''
        Crie um programa que utilize comandos de saída (print) para exibir 
        diferentes tipos de dados e realize operações aritméticas básicas 
        (soma, subtração, divisão, multiplicação, potência, divisão inteira e 
        resto) além de manipulação de strings. Em seguida, utilize o comando de 
        entrada (input) para perguntar o nome do usuário e a disciplina que ele 
        estuda, exibindo uma mensagem personalizada de boas-vindas ao final.
    '''
def main():
    # Para fazer comentários em uma linha, usamos -> #

    # print() --> usamos para fazer uma saída de dados
    print('Olá, mundo!')      # exibe o texto "Olá, mundo!" no console
    print(10)                 # exibe o número inteiro 10
    print(5.87)               # exibe o número real 5.87
    print(True)               # exibe o booleano True
    # obs: para booleanos, sempre usamos letras maiúsculas no início (True/False)

    ###################################################
    # Operações aritméticas: 
    
    # Soma --> +
    print("5 + 5")            # exibe o TEXTO "5 + 5"
    print(5 + 5)              # exibe o resultado de 5 + 5, ou seja, 10

    # Subtração --> -
    print("9 - 3")
    print(9 - 3)

    # Divisão --> /
    print("12 / 4")
    print(12 / 4)

    # Multiplicação --> *
    print("3 * 2")
    print(3 * 2)

    # Potência --> **
    print('3 ** 2')           # exibe o TEXTO '3 ** 2'
    # exibe o resultado de 3 elevado a 2, ou seja, 3*3 
    print(3 ** 2)

    # Divisão inteira --> //
    print('20 // 3')
    # exibe a parte inteira da divisão
    print(20 // 3)

    # Módulo (resto da divisão) --> %
    print("5 % 2")
    print(5 % 2)              # exibe o resto INTEIRO da divisão entre 5 e 2

    # Multiplicação de string
    print("python" * 10)      # repete o texto 10 vezes

    # Soma (concatenação) de string
    print('Uni' + 'sa')       # exibe o resultado da "soma" (junção) do texto

    #########################################################
    # Entrada de dados: usamos o input()
    nome = input("Qual o seu nome? ")             # pergunta ao usuário um nome
    disciplina = input("O que você estuda? ")     # pergunta ao usuário o que ele estuda

    # Exibe as informações capturadas de forma organizada e amigável
    print(f"Seja bem-vindo(a), {nome}!")
    print(f"Que legal que você estuda {disciplina}!")


if __name__ == "__main__":
    main()
