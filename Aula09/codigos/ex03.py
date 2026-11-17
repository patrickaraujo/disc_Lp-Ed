"""
Exercício 3 — Cofre com senha

A senha de um cofre é "lped2026". O usuário tem no máximo 3 tentativas.

  - Se digitar a senha certa, mostre "Cofre aberto!" e encerre o laço (break).
  - Se apertar Enter sem digitar nada (senha vazia), mostre "Senha vazia,
    tente de novo." — essa tentativa NÃO conta (continue).
  - Se errar, mostre quantas tentativas restam.
  - Se as 3 tentativas acabarem, mostre "Cofre bloqueado!".

Saída esperada (exemplo 1):
    Senha: abc
    Senha incorreta. Restam 2 tentativa(s).
    Senha:
    Senha vazia, tente de novo.
    Senha: lped2026
    Cofre aberto!

Saída esperada (exemplo 2):
    Senha: 1234
    Senha incorreta. Restam 2 tentativa(s).
    Senha: senha
    Senha incorreta. Restam 1 tentativa(s).
    Senha: lped
    Senha incorreta. Restam 0 tentativa(s).
    Cofre bloqueado!
"""

SENHA = "lped2026"
MAX_TENTATIVAS = 3


def main():
    tentativas = 0
    aberto = False

    # while: não sabemos quantas vezes o laço vai rodar
    # (a senha vazia não conta como tentativa)
    while tentativas < MAX_TENTATIVAS:
        senha = input("Senha: ")

        if senha == "":
            print("Senha vazia, tente de novo.")
            continue          # volta ao teste do while SEM contar a tentativa

        tentativas = tentativas + 1

        if senha == SENHA:
            aberto = True
            print("Cofre aberto!")
            break             # sai do laço imediatamente

        print(f"Senha incorreta. Restam {MAX_TENTATIVAS - tentativas} tentativa(s).")

    if not aberto:
        print("Cofre bloqueado!")


if __name__ == "__main__":
    main()
