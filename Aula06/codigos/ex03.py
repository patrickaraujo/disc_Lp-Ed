"""
Exercício 3 — Pontos no plano

Pergunte quantos pontos serão digitados. Depois, leia cada ponto em UMA
linha, no formato "x y" (separados por espaço), e guarde-o como uma
TUPLA (x, y) dentro de uma lista.

Ao final, mostre:
- a lista de pontos;
- o quadrante de cada ponto (desempacote a tupla em x e y):
      x > 0 e y > 0 -> 1º quadrante     x < 0 e y > 0 -> 2º quadrante
      x < 0 e y < 0 -> 3º quadrante     x > 0 e y < 0 -> 4º quadrante
      se x ou y for zero -> "Sobre um eixo"
- o ponto mais distante da origem, sabendo que
      distância = (x² + y²) ** 0.5

Saída esperada:
    Quantos pontos? 3
    Ponto 1 (x y): 2 3
    Ponto 2 (x y): -4 1
    Ponto 3 (x y): 0 -2
    Pontos: [(2.0, 3.0), (-4.0, 1.0), (0.0, -2.0)]
    (2.0, 3.0) -> 1º quadrante
    (-4.0, 1.0) -> 2º quadrante
    (0.0, -2.0) -> Sobre um eixo
    Mais distante da origem: (-4.0, 1.0) (distância 4.12)
"""


def main():
    n = int(input("Quantos pontos? "))

    pontos = []
    for i in range(n):
        # split() devolve as duas partes digitadas; desempacotamos em x e y
        x, y = input(f"Ponto {i + 1} (x y): ").split()
        ponto = (float(x), float(y))  # empacotando em uma tupla
        pontos.append(ponto)

    print("Pontos:", pontos)

    mais_distante = pontos[0]
    maior_distancia = 0

    for ponto in pontos:
        x, y = ponto  # desempacotamento

        if x > 0 and y > 0:
            quadrante = "1º quadrante"
        elif x < 0 and y > 0:
            quadrante = "2º quadrante"
        elif x < 0 and y < 0:
            quadrante = "3º quadrante"
        elif x > 0 and y < 0:
            quadrante = "4º quadrante"
        else:
            quadrante = "Sobre um eixo"
        print(ponto, "->", quadrante)

        distancia = (x ** 2 + y ** 2) ** 0.5
        if distancia > maior_distancia:
            maior_distancia = distancia
            mais_distante = ponto

    print(f"Mais distante da origem: {mais_distante} "
          f"(distância {maior_distancia:.2f})")


if __name__ == "__main__":
    main()
