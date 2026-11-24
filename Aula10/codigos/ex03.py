"""
Exercício 3 — Mapa de assentos do cinema

Uma sala tem 5 fileiras (A a E) com 8 poltronas cada. Represente a sala
como uma MATRIZ (lista de listas) em que 0 = livre e 1 = ocupada.

Crie as funções:
  criar_sala(fileiras, poltronas) -> matriz toda com 0 (use laços)
  reservar(sala, fileira, numero) -> devolve uma mensagem:
        "Fileira ou poltrona inválida", "Poltrona já ocupada" ou "Reservada"
        (fileira é uma letra; numero vai de 1 a 8)
  mostrar(sala)                    -> imprime o mapa (L = livre, X = ocupada)
  livres_por_fileira(sala)         -> lista com a quantidade de livres de cada fileira

Faça as reservas da lista abaixo, mostre o mapa, os lugares livres por
fileira e a fileira com mais lugares livres.

    pedidos = [("A", 3), ("A", 4), ("C", 1), ("C", 8), ("E", 5),
               ("A", 3), ("F", 2), ("B", 9), ("B", 2), ("B", 3), ("B", 4)]

Saída esperada:
    A3: Reservada
    A4: Reservada
    C1: Reservada
    C8: Reservada
    E5: Reservada
    A3: Poltrona já ocupada
    F2: Fileira ou poltrona inválida
    B9: Fileira ou poltrona inválida
    B2: Reservada
    B3: Reservada
    B4: Reservada
        1 2 3 4 5 6 7 8
    A   L L X X L L L L
    B   L X X X L L L L
    C   X L L L L L L X
    D   L L L L L L L L
    E   L L L L X L L L
    Livres por fileira: [6, 5, 6, 8, 7]
    Fileira com mais lugares livres: D
"""

LETRAS = "ABCDE"


def criar_sala(fileiras, poltronas):
    sala = []
    for i in range(fileiras):
        linha = []                    # uma lista NOVA para cada fileira
        for j in range(poltronas):
            linha.append(0)
        sala.append(linha)
    # Cuidado: [[0] * 8] * 5 parece igual, mas cria 5 referências para a
    # MESMA linha. Reservar A3 marcaria a poltrona 3 de todas as fileiras.
    return sala


def reservar(sala, fileira, numero):
    if fileira not in LETRAS or numero < 1 or numero > len(sala[0]):
        return "Fileira ou poltrona inválida"
    i = LETRAS.index(fileira)         # "A" -> 0, "B" -> 1, ...
    j = numero - 1                    # poltrona 1 fica na coluna 0
    if sala[i][j] == 1:
        return "Poltrona já ocupada"
    sala[i][j] = 1
    return "Reservada"


def mostrar(sala):
    cabecalho = "   "
    for j in range(len(sala[0])):
        cabecalho = cabecalho + " " + str(j + 1)
    print(cabecalho)
    for i in range(len(sala)):
        linha = LETRAS[i] + "  "
        for j in range(len(sala[i])):
            if sala[i][j] == 1:
                linha = linha + " X"
            else:
                linha = linha + " L"
        print(linha)


def livres_por_fileira(sala):
    livres = []
    for linha in sala:
        cont = 0
        for poltrona in linha:
            if poltrona == 0:
                cont = cont + 1
        livres.append(cont)
    return livres


def main():
    sala = criar_sala(5, 8)
    pedidos = [("A", 3), ("A", 4), ("C", 1), ("C", 8), ("E", 5),
               ("A", 3), ("F", 2), ("B", 9), ("B", 2), ("B", 3), ("B", 4)]

    for fileira, numero in pedidos:
        print(f"{fileira}{numero}: {reservar(sala, fileira, numero)}")

    mostrar(sala)
    livres = livres_por_fileira(sala)
    print("Livres por fileira:", livres)

    melhor = 0
    for i in range(1, len(livres)):
        if livres[i] > livres[melhor]:
            melhor = i
    print("Fileira com mais lugares livres:", LETRAS[melhor])


if __name__ == "__main__":
    main()
