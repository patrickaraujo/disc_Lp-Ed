"""
Exercício Tutoreado 4 — Cadastro da turma (escopo e listas em funções)

Faça um cadastro de alunos e notas usando listas paralelas, em que as
listas são criadas na main() e passadas para as funções:

  - cadastrar(alunos, notas): lê nomes e notas até o usuário digitar "sair".
  - listar(alunos, notas): mostra cada aluno, sua nota e se está aprovado
    (nota mínima guardada em uma variável global).
  - dar_bonus(notas, valor=0.5): soma o bônus em todas as notas.
  - trocar_turma(alunos): tenta trocar a lista por uma nova (e não consegue!).

Mantenha também um histórico global com as ações realizadas.

Saída esperada:
    Bem-vindo ao cadastro!
    Nome (ou 'sair'): Ana
    Nota de Ana: 7
    Nome (ou 'sair'): Bruno
    Nota de Bruno: 5.8
    Nome (ou 'sair'): sair
    1. Ana - 7.0 (aprovado)
    2. Bruno - 5.8 (reprovado)
    Depois do bônus:
    1. Ana - 7.5 (aprovado)
    2. Bruno - 6.3 (aprovado)
    Depois de trocar_turma(): ['Ana', 'Bruno']
    Até a próxima aula!
    Mensagem global continua: Bem-vindo ao cadastro!
    Histórico: ['cadastro: Ana', 'cadastro: Bruno', 'bônus de 0.5']
    Histórico depois de limpar: []
"""

# ---------------------------------------------------------------------
# VARIÁVEIS GLOBAIS: criadas fora de qualquer função, visíveis em todas.
# Use com moderação: qualquer função pode alterá-las, o que dificulta
# descobrir quem mudou o quê.
# ---------------------------------------------------------------------
NOTA_MINIMA = 6.0
mensagem = "Bem-vindo ao cadastro!"
historico = []


def main():
    print(mensagem)  # a main() LÊ uma global sem problema

    # Variáveis LOCAIS da main(): só existem aqui dentro.
    # Para outras funções usarem, passamos como parâmetro.
    alunos = []
    notas = []

    cadastrar(alunos, notas)
    listar(alunos, notas)
    # print(linha)   # descomente: NameError ('linha' é local de listar)

    dar_bonus(notas)
    print("Depois do bônus:")
    listar(alunos, notas)

    trocar_turma(alunos)
    print("Depois de trocar_turma():", alunos)

    despedida()
    print("Mensagem global continua:", mensagem)

    print("Histórico:", historico)
    limpar_historico()
    print("Histórico depois de limpar:", historico)


def cadastrar(alunos, notas):
    # 'alunos' e 'notas' aqui apontam para as MESMAS listas da main().
    # Como listas são mutáveis, o append altera as listas da main().
    nome = input("Nome (ou 'sair'): ").strip().capitalize()
    while nome != "Sair":
        nota = float(input(f"Nota de {nome}: "))
        alunos.append(nome)
        notas.append(nota)
        registrar("cadastro: " + nome)
        nome = input("Nome (ou 'sair'): ").strip().capitalize()


def listar(alunos, notas):
    for i in range(len(alunos)):
        # NOTA_MINIMA não foi criada aqui: a função enxerga a global
        if notas[i] >= NOTA_MINIMA:
            linha = f"{i + 1}. {alunos[i]} - {notas[i]:.1f} (aprovado)"
        else:
            linha = f"{i + 1}. {alunos[i]} - {notas[i]:.1f} (reprovado)"
        print(linha)


def dar_bonus(notas, valor=0.5):
    # Alterar uma POSIÇÃO da lista altera a lista original
    for i in range(len(notas)):
        notas[i] = notas[i] + valor
    registrar(f"bônus de {valor}")


def trocar_turma(alunos):
    # Atribuir uma NOVA lista cria uma variável local com outro conteúdo.
    # A lista da main() NÃO é afetada.
    alunos = ["Turma", "Nova"]


def despedida():
    # Local com o MESMO nome de uma global: a global não muda
    mensagem = "Até a próxima aula!"
    print(mensagem)


def registrar(texto):
    # append ALTERA a lista global sem precisar de 'global'
    historico.append(texto)


def registrar_errado(texto):
    # Esta função dá UnboundLocalError se for chamada: ao ver
    # "historico = ...", o Python trata historico como LOCAL, e ela
    # está sendo usada antes de existir.
    historico = historico + [texto]


def limpar_historico():
    # Para ATRIBUIR um novo valor à global, precisamos do 'global'
    global historico
    historico = []


if __name__ == "__main__":
    main()
