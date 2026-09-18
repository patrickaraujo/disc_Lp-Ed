"""
Exercício 1 — Elegibilidade para Votação
 
Leia a idade de uma pessoa e informe se ela já pode votar ou não.
Considere que o voto é permitido a partir dos 16 anos.
Utilize uma estrutura if/else para realizar a verificação.
"""
 
 
def main():
    idade = int(input("Digite sua idade: "))
 
    if idade >= 16:
        print("Já tem 16 anos ou mais! Você já pode votar e participar das decisões políticas.")
    else:
        print("Ainda não tem a idade mínima. Espere completar 16 anos para poder votar.")
 
 
if __name__ == "__main__":
    main()
