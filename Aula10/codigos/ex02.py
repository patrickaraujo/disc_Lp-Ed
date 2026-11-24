"""
Exercício 2 — Agenda de contatos

Guarde os contatos em um dicionário {nome: (telefone, email)}, em que o
valor é uma TUPLA. Faça um menu (use match-case) que se repete até a
opção 0:

    1 - Adicionar contato   (avise se o nome já existir)
    2 - Buscar contato      (avise se não existir)
    3 - Atualizar telefone  (o e-mail continua o mesmo)
    4 - Listar contatos
    0 - Sair

Atenção: tuplas são imutáveis. Para atualizar o telefone, monte uma
NOVA tupla com o telefone novo e o e-mail antigo.

Saída esperada (trecho):
    Opção: 1
    Nome: Ana
    Telefone: 99999-1111
    E-mail: ana@email.com
    Contato adicionado.
    Opção: 3
    Nome: Ana
    Novo telefone: 98888-2222
    Telefone atualizado.
    Opção: 2
    Nome: Ana
    Ana | 98888-2222 | ana@email.com
    Opção: 2
    Nome: Bruno
    Contato não encontrado.
    Opção: 0
    Agenda encerrada.
"""


def main():
    agenda = {}
    print("1-Adicionar 2-Buscar 3-Atualizar telefone 4-Listar 0-Sair")

    while True:
        opcao = int(input("Opção: "))

        match opcao:
            case 1:
                nome = input("Nome: ")
                if nome in agenda:
                    print("Esse contato já existe.")
                else:
                    telefone = input("Telefone: ")
                    email = input("E-mail: ")
                    agenda[nome] = (telefone, email)     # valor = tupla
                    print("Contato adicionado.")
            case 2:
                nome = input("Nome: ")
                if nome in agenda:
                    telefone, email = agenda[nome]       # desempacota
                    print(f"{nome} | {telefone} | {email}")
                else:
                    print("Contato não encontrado.")
            case 3:
                nome = input("Nome: ")
                if nome in agenda:
                    novo = input("Novo telefone: ")
                    email = agenda[nome][1]              # mantém o e-mail
                    # agenda[nome][0] = novo  -> TypeError (tupla imutável)
                    agenda[nome] = (novo, email)         # troca a tupla inteira
                    print("Telefone atualizado.")
                else:
                    print("Contato não encontrado.")
            case 4:
                if len(agenda) == 0:
                    print("Agenda vazia.")
                for nome, (telefone, email) in agenda.items():
                    print(f"{nome} | {telefone} | {email}")
            case 0:
                print("Agenda encerrada.")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
