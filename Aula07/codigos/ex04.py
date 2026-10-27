"""
Exercício 4 — Jogo da Velha

Leia um tabuleiro de jogo da velha 3 x 3, linha por linha. Cada linha é
digitada de uma vez, com 3 símbolos separados por espaço: X, O ou - (casa
vazia). Aceite letras minúsculas também. Guarde o tabuleiro em uma matriz.

Crie as funções:
- le_tabuleiro(): lê e retorna a matriz 3 x 3. Se a linha não tiver 3
  símbolos válidos, mostre "Linha inválida" e peça a linha novamente;
- mostra_tabuleiro(tab): mostra o tabuleiro;
- vencedor(tab): retorna "X" ou "O" se algum jogador completou uma linha,
  uma coluna ou uma diagonal; caso contrário, retorna "";
- tem_casa_vazia(tab): retorna True se ainda existe alguma casa com "-".

Na main(), informe o resultado:
- "X venceu!" ou "O venceu!";
- "Deu velha!" (ninguém venceu e não há casas vazias);
- "Jogo em andamento" (ninguém venceu e ainda há casas vazias).

Saída esperada:
    Linha 1: x o x
    Linha 2: o x o
    Linha 3: o - y
    Linha inválida: use 3 símbolos entre X, O e -.
    Linha 3: o - x
     X | O | X
    ---+---+---
     O | X | O
    ---+---+---
     O | - | X
    X venceu!
"""


def main():
    tabuleiro = le_tabuleiro()
    mostra_tabuleiro(tabuleiro)

    ganhador = vencedor(tabuleiro)
    if ganhador != "":
        print(f"{ganhador} venceu!")
    elif tem_casa_vazia(tabuleiro):
        print("Jogo em andamento")
    else:
        print("Deu velha!")


def le_tabuleiro():
    tab = []
    while len(tab) < 3:
        simbolos = input(f"Linha {len(tab) + 1}: ").upper().split()
        valida = len(simbolos) == 3
        for s in simbolos:
            if s not in ("X", "O", "-"):
                valida = False
        if valida:
            tab.append(simbolos)
        else:
            print("Linha inválida: use 3 símbolos entre X, O e -.")
    return tab


def mostra_tabuleiro(tab):
    for i in range(3):
        print(f" {tab[i][0]} | {tab[i][1]} | {tab[i][2]}")
        if i < 2:
            print("---+---+---")


def vencedor(tab):
    for jogador in ("X", "O"):
        # Linhas e colunas: o mesmo i serve para a linha i e a coluna i
        for i in range(3):
            if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
                return jogador
            if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
                return jogador
        # Diagonal principal: [0][0], [1][1], [2][2]
        if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
            return jogador
        # Diagonal secundária: [0][2], [1][1], [2][0]
        if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
            return jogador
    return ""


def tem_casa_vazia(tab):
    for linha in tab:
        if "-" in linha:
            return True
    return False


if __name__ == "__main__":
    main()
