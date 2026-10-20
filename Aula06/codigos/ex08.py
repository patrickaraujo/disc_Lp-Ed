"""
Exercício 8 — Lista de tarefas (escopo e listas em funções)

Crie um gerenciador de tarefas com menu que se repete até o usuário sair:

    1 - Adicionar tarefa
    2 - Concluir tarefa
    3 - Mostrar tarefas
    0 - Sair

Regras:
- A lista de tarefas deve ser criada DENTRO da main() (variável local)
  e passada como parâmetro para as funções.
- Use uma variável GLOBAL "concluidas" para contar quantas tarefas
  foram concluídas.
- Funções obrigatórias:
    adicionar(tarefas, texto)  -> acrescenta a tarefa (sem return)
    concluir(tarefas, numero)  -> remove a tarefa pela posição mostrada
                                  ao usuário (começando em 1) e soma 1
                                  em "concluidas". Retorna True se
                                  conseguiu e False se a posição for inválida.
    mostrar(tarefas)           -> mostra as tarefas numeradas a partir de 1
- Ao sair, mostre quantas tarefas foram concluídas e quantas ficaram pendentes.

Responda também, em comentários no seu código:
  a) Por que adicionar() altera a lista da main() mesmo sem return?
  b) Por que concluir() precisa da palavra global e adicionar() não?
  c) O que aconteceria se adicionar() fizesse  tarefas = tarefas + [texto]
     em vez de  tarefas.append(texto)?

Saída esperada (trecho):
    Opção: 1
    Tarefa: estudar listas
    Opção: 1
    Tarefa: fazer a lista de exercícios
    Opção: 2
    Número da tarefa: 1
    Tarefa concluída!
    Opção: 3
    1. fazer a lista de exercícios
    Opção: 0
    Concluídas: 1 | Pendentes: 1
"""

concluidas = 0  # variável GLOBAL


def main():
    tarefas = []  # variável LOCAL da main()

    while True:
        print("\n1 - Adicionar | 2 - Concluir | 3 - Mostrar | 0 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            texto = input("Tarefa: ").strip()
            adicionar(tarefas, texto)
        elif opcao == "2":
            numero = int(input("Número da tarefa: "))
            if concluir(tarefas, numero):
                print("Tarefa concluída!")
            else:
                print("Número inválido.")
        elif opcao == "3":
            mostrar(tarefas)
        elif opcao == "0":
            print(f"Concluídas: {concluidas} | Pendentes: {len(tarefas)}")
            break
        else:
            print("Opção inválida.")


def adicionar(tarefas, texto):
    # a) 'tarefas' recebe a MESMA lista da main(). Como listas são
    #    mutáveis, o append altera o conteúdo dessa lista.
    tarefas.append(texto)
    # c) Com  tarefas = tarefas + [texto]  seria criada uma NOVA lista,
    #    guardada só na variável local 'tarefas'. A lista da main()
    #    continuaria igual e a tarefa "sumiria" ao final da função.


def concluir(tarefas, numero):
    # b) Aqui fazemos uma ATRIBUIÇÃO (concluidas = concluidas + 1).
    #    Sem 'global', o Python trataria 'concluidas' como local e daria
    #    UnboundLocalError. Em adicionar() não há atribuição à variável
    #    'tarefas', só uma alteração do conteúdo da lista (append).
    global concluidas
    if numero < 1 or numero > len(tarefas):
        return False
    del tarefas[numero - 1]
    concluidas = concluidas + 1
    return True


def mostrar(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa pendente.")
    for i in range(len(tarefas)):
        print(f"{i + 1}. {tarefas[i]}")


if __name__ == "__main__":
    main()
