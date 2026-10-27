"""
Exercício 3 — Corrida de Kart

Uma bateria de kart tem 4 pilotos, e cada um dá 5 voltas. Os nomes ficam
em uma lista e os tempos (em segundos) em uma MATRIZ: cada linha é um
piloto e cada coluna é uma volta. Use as constantes PILOTOS = 4 e
VOLTAS = 5 no início do programa. Crie as funções:

- le_corrida(): lê o nome de cada piloto e seus 5 tempos, digitados em
  uma única linha. Retorna a lista de nomes e a matriz de tempos;
- melhor_volta(tempos): retorna a linha e a coluna do menor tempo da matriz;
- tempo_total(voltas): recebe UMA linha da matriz e retorna a soma dos tempos;
- classificacao(nomes, tempos): retorna uma lista de tuplas
  (tempo_total, nome) ordenada do menor para o maior tempo total;
- volta_mais_rapida(tempos): retorna o índice da volta (coluna) com a menor
  média entre os pilotos e o valor dessa média.

Na main(), mostre a melhor volta da prova (piloto, volta e tempo), a
classificação final e a volta com a menor média.

Dica: o método sort() ordena uma lista de tuplas pelo primeiro elemento.

Saída esperada:
    Nome do piloto 1: Ana
    Tempos de Ana (5 voltas): 62.1 60.5 59.8 61.0 60.2
    Nome do piloto 2: Bruno
    Tempos de Bruno (5 voltas): 63.0 61.2 60.9 60.1 59.5
    Nome do piloto 3: Carla
    Tempos de Carla (5 voltas): 61.5 59.9 60.0 59.4 60.8
    Nome do piloto 4: Diego
    Tempos de Diego (5 voltas): 64.2 62.0 61.5 61.1 60.9
    Melhor volta: Carla, volta 4 (59.4 s)
    Classificação final:
      1º Carla - 301.6 s
      2º Ana - 303.6 s
      3º Bruno - 304.7 s
      4º Diego - 309.7 s
    Volta com a menor média: volta 5 (60.35 s)
"""

PILOTOS = 4
VOLTAS = 5


def main():
    nomes, tempos = le_corrida()

    i, j = melhor_volta(tempos)
    print(f"Melhor volta: {nomes[i]}, volta {j + 1} ({tempos[i][j]} s)")

    print("Classificação final:")
    posicao = 1
    for total, nome in classificacao(nomes, tempos):
        print(f"  {posicao}º {nome} - {total:.1f} s")
        posicao += 1

    volta, media = volta_mais_rapida(tempos)
    print(f"Volta com a menor média: volta {volta + 1} ({media:.2f} s)")


def le_corrida():
    nomes = []
    tempos = []
    for i in range(PILOTOS):
        nome = input(f"Nome do piloto {i + 1}: ").strip()
        valores = input(f"Tempos de {nome} ({VOLTAS} voltas): ").split()
        nomes.append(nome)
        tempos.append([float(v) for v in valores])
    return nomes, tempos


def melhor_volta(tempos):
    i_melhor = 0
    j_melhor = 0
    for i in range(len(tempos)):
        for j in range(len(tempos[i])):
            if tempos[i][j] < tempos[i_melhor][j_melhor]:
                i_melhor = i
                j_melhor = j
    return i_melhor, j_melhor


def tempo_total(voltas):
    total = 0
    for tempo in voltas:
        total += tempo
    return total


def classificacao(nomes, tempos):
    resultado = []
    for i in range(len(nomes)):
        resultado.append((tempo_total(tempos[i]), nomes[i]))
    resultado.sort()
    return resultado


def volta_mais_rapida(tempos):
    j_rapida = 0
    menor_media = 0
    for j in range(len(tempos[0])):
        soma = 0
        for i in range(len(tempos)):
            soma += tempos[i][j]
        media = soma / len(tempos)
        if j == 0 or media < menor_media:
            menor_media = media
            j_rapida = j
    return j_rapida, menor_media


if __name__ == "__main__":
    main()
