"""
Exercício 5 — Média ponderada com NumPy

Uma disciplina tem 4 avaliações com pesos diferentes:

    P1: 20% | P2: 20% | Trabalho: 30% | Projeto: 30%

Guarde os pesos em um array do NumPy (constante PESOS) e crie as funções:

- le_turma(n): lê o nome e as 4 notas (em uma única linha) de n alunos.
  Retorna a lista de nomes e um ARRAY do NumPy com as notas;
- medias_ponderadas(notas, pesos=PESOS): retorna o array de médias,
  calculado com np.dot;
- situacao(media, minimo=6.0): retorna "Aprovado" ou "Reprovado";
- aplica_acrescimo(notas, percentual=10): retorna um NOVO array com todas
  as notas aumentadas no percentual informado (sem laço; não é preciso
  limitar a 10);
- conta_novos_aprovados(antes, depois, minimo=6.0): recebe as médias antes
  e depois do acréscimo e retorna quantos alunos passaram de reprovado
  para aprovado.

Na main(), leia quantos alunos a turma tem e mostre o shape das notas, a
média e a situação de cada aluno, a média da turma em cada avaliação
(use mean(axis=0)), as médias com acréscimo de 10% e quantos alunos
passariam a ser aprovados.

Antes de rodar, instale o NumPy (uma única vez):
    pip install numpy

Saída esperada:
    Quantos alunos? 4
    Nome do aluno 1: Ana
    Notas de Ana (P1 P2 Trab Proj): 7 6 8 9
    Nome do aluno 2: Bruno
    Notas de Bruno (P1 P2 Trab Proj): 5 4 6 6.5
    Nome do aluno 3: Carla
    Notas de Carla (P1 P2 Trab Proj): 9 8.5 10 9.5
    Nome do aluno 4: Diego
    Notas de Diego (P1 P2 Trab Proj): 4 5 5.5 6
    Shape das notas: (4, 4)
    Ana: 7.70 (Aprovado)
    Bruno: 5.55 (Reprovado)
    Carla: 9.35 (Aprovado)
    Diego: 5.25 (Reprovado)
    Média por avaliação:
      P1: 6.25
      P2: 5.88
      Trab: 7.38
      Proj: 7.75
    Com acréscimo de 10%:
      Ana: 8.47
      Bruno: 6.11
      Carla: 10.29
      Diego: 5.78
    Novos aprovados: 1
"""

import numpy as np

AVALIACOES = ("P1", "P2", "Trab", "Proj")
PESOS = np.array([0.2, 0.2, 0.3, 0.3])


def main():
    n = int(input("Quantos alunos? "))
    nomes, notas = le_turma(n)
    print("Shape das notas:", notas.shape)

    medias = medias_ponderadas(notas)
    for i in range(n):
        print(f"{nomes[i]}: {medias[i]:.2f} ({situacao(medias[i])})")

    por_avaliacao = notas.mean(axis=0)
    print("Média por avaliação:")
    for j in range(len(AVALIACOES)):
        print(f"  {AVALIACOES[j]}: {por_avaliacao[j]:.2f}")

    novas_medias = medias_ponderadas(aplica_acrescimo(notas))
    print("Com acréscimo de 10%:")
    for i in range(n):
        print(f"  {nomes[i]}: {novas_medias[i]:.2f}")
    print("Novos aprovados:", conta_novos_aprovados(medias, novas_medias))


def le_turma(n):
    nomes = []
    lista_notas = []
    for i in range(n):
        nome = input(f"Nome do aluno {i + 1}: ").strip()
        valores = input(f"Notas de {nome} (P1 P2 Trab Proj): ").split()
        nomes.append(nome)
        lista_notas.append([float(v) for v in valores])
    return nomes, np.array(lista_notas)


def medias_ponderadas(notas, pesos=PESOS):
    # (n x 4) . (4) -> um valor por aluno
    return np.dot(notas, pesos)


def situacao(media, minimo=6.0):
    if media >= minimo:
        return "Aprovado"
    return "Reprovado"


def aplica_acrescimo(notas, percentual=10):
    # A operação vale para todas as posições de uma vez e cria um NOVO array
    return notas * (1 + percentual / 100)


def conta_novos_aprovados(antes, depois, minimo=6.0):
    quantidade = 0
    for i in range(len(antes)):
        if antes[i] < minimo and depois[i] >= minimo:
            quantidade += 1
    return quantidade


if __name__ == "__main__":
    main()
