"""
Crie um programa que demonstre o uso do laço de repetição while através de
dois exemplos práticos. O primeiro deve exibir uma frase na tela dez vezes
utilizando uma variável contadora. O segundo deve implementar um jogo interativo
onde o programa solicita uma palavra secreta e continua pedindo novas tentativas
em looping até que o usuário acerte a palavra estipulada, aplicando métodos de
normalização de texto como lower() e strip().
"""
 
 
def main():
    """
    Exemplos práticos de laços de repetição (while) e manipulação de strings.
    """
 
    print("--- Exemplo 1: Laço while com contador ---")
    # Exemplo 1: Laço de repetição com contador
    contador = 1
    while contador <= 10:
        print("Estou aprendendo python!")
        contador = contador + 1
 
    print("\n--- Exemplo 2: Jogo da Palavra Secreta ---")
    # Exemplo 2: Manipulação de strings, while com break/continue
    # e comparação de strings com operadores relacionais
 
    # quando quiser transformar uma string TODA em letras MAIUSCULAS
    # usamos o .upper() e quando quiser transformar tudo para
    # MINUSCULO, usamos o .lower()
 
    # quando quiser remover possiveis espaços do inicio ou do fim
    # da string, usamos o .strip()
 
    palavra_secreta = "unisa"
 
    while True:
        tentativa = input("Digite a palavra secreta (ou 'sair'): ").lower().strip()
 
        # continue: entrada vazia volta ao início do laço
        if tentativa == "":
            print("Entrada vazia! Tente novamente.")
            continue
 
        # break: sai do laço com o comando 'sair'
        if tentativa == "sair":
            print("Encerrando o jogo...")
            break
 
        # break: sai do laço ao acertar a palavra
        if tentativa == palavra_secreta:
            print("Acertô miseravi!")
            break
 
        # comparação de strings com operadores relacionais:
        # o Python compara lexicograficamente (ordem do dicionário)
        if tentativa < palavra_secreta:
            print("Dica: sua palavra vem antes da palavra secreta na ordem alfabética.")
        else:
            print("Dica: sua palavra vem depois da palavra secreta na ordem alfabética.")
 
        print("Palavra incorreta!\n")
 
    print("Fim do programa.")
 
 
if __name__ == "__main__":
    main()
