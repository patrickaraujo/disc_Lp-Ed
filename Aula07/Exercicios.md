# Lista de Exercícios — Matrizes e NumPy

## Exercício 1 — Posições não nulas

Peça ao usuário o número de **linhas** e de **colunas** de uma matriz e leia a matriz **linha por linha**: cada linha é digitada de uma vez, com os valores separados por espaço. Crie as funções:

* `le_matriz(linhas, colunas)`: lê e retorna a matriz. Se a quantidade de valores digitados em uma linha for diferente de `colunas`, mostra uma mensagem e pede a linha novamente;
* `imprime_matriz(mat)`: mostra a matriz em formato de tabela (não retorna nada);
* `posicoes_nao_nulas(mat)`: retorna uma **lista de tuplas** `(linha, coluna)` com as posições diferentes de zero, contando a partir de 1.

Na `main()`, mostre a matriz, quantas posições são não nulas, a lista de posições e o percentual de posições não nulas.

> 💡 Dica: `input().split()` devolve uma lista de textos; converta cada um com `int()`.

### Exemplo de execução

```text
Linhas: 3
Colunas: 4
Linha 1: 0 5 0 2
Linha 2: 0 0 0
Digite exatamente 4 valores.
Linha 2: 0 0 0 0
Linha 3: 7 0 1 0
Matriz:
   0   5   0   2
   0   0   0   0
   7   0   1   0
Posições não nulas: 4
Posições: [(1, 2), (1, 4), (3, 1), (3, 3)]
Percentual não nulo: 33.3%
```

---

## Exercício 2 — Operações com matrizes quadradas

Crie as funções abaixo para matrizes quadradas `n x n`. As funções de cálculo devem **retornar uma nova matriz**, sem alterar as matrizes recebidas.

| Função                | O que faz                                                  |
| --------------------- | ---------------------------------------------------------- |
| `le_matriz(n, nome)`  | Lê a matriz linha por linha (valores separados por espaço) |
| `imprime_matriz(mat)` | Mostra a matriz em formato de tabela                       |
| `soma(m1, m2)`        | Retorna `m1 + m2`                                          |
| `subtracao(m1, m2)`   | Retorna `m1 - m2`                                          |
| `transposta(mat)`     | Retorna a transposta (a linha `i` vira a coluna `i`)       |
| `eh_simetrica(mat)`   | Retorna `True` se a matriz for igual à sua transposta      |

Na `main()`, leia `n`, as matrizes A e B, e mostre `A + B`, `A - B`, a transposta de A e se A e B são simétricas.

> 💡 Dica: na transposta, a posição `[i][j]` do resultado recebe `mat[j][i]`.

### Exemplo de execução

```text
Dimensão n: 3
Matriz A, linha 1: 1 2 3
Matriz A, linha 2: 4 5 6
Matriz A, linha 3: 7 8 9
Matriz B, linha 1: 1 0 2
Matriz B, linha 2: 0 3 4
Matriz B, linha 3: 2 4 5
A + B:
   2   2   5
   4   8  10
   9  12  14
A - B:
   0   2   1
   4   2   2
   5   4   4
Transposta de A:
   1   4   7
   2   5   8
   3   6   9
A é simétrica? False
B é simétrica? True
```

---

## Exercício 3 — Corrida de Kart

Uma bateria de kart tem **4 pilotos**, e cada um dá **5 voltas**. Os nomes ficam em uma lista e os tempos (em segundos) em uma **matriz**: cada linha é um piloto e cada coluna é uma volta. Use as constantes `PILOTOS = 4` e `VOLTAS = 5` no início do programa. Crie as funções:

| Função                          | O que retorna                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------ |
| `le_corrida()`                  | A lista de nomes e a matriz de tempos (os 5 tempos são digitados em uma linha) |
| `melhor_volta(tempos)`          | A linha e a coluna do menor tempo da matriz                                    |
| `tempo_total(voltas)`           | A soma dos tempos de **uma linha** da matriz                                   |
| `classificacao(nomes, tempos)`  | Uma lista de tuplas `(tempo_total, nome)`, do menor para o maior tempo         |
| `volta_mais_rapida(tempos)`     | O índice da volta (coluna) com a menor média e o valor dessa média             |

Na `main()`, mostre a melhor volta da prova (piloto, volta e tempo), a classificação final e a volta com a menor média.

> 💡 Dica: o método `sort()` ordena uma lista de tuplas pelo primeiro elemento.

### Exemplo de execução

```text
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
```

---

## Exercício 4 — Jogo da Velha

Leia um tabuleiro de jogo da velha 3 x 3, **linha por linha**. Cada linha tem 3 símbolos separados por espaço: `X`, `O` ou `-` (casa vazia). Aceite letras minúsculas também. Crie as funções:

* `le_tabuleiro()`: lê e retorna a matriz 3 x 3. Se a linha não tiver 3 símbolos válidos, mostre `Linha inválida` e peça a linha novamente;
* `mostra_tabuleiro(tab)`: mostra o tabuleiro;
* `vencedor(tab)`: retorna `"X"` ou `"O"` se algum jogador completou uma **linha**, uma **coluna** ou uma **diagonal**; caso contrário, retorna `""`;
* `tem_casa_vazia(tab)`: retorna `True` se ainda existe alguma casa com `-`.

Na `main()`, informe o resultado:

| Situação                                       | Mensagem                   |
| ---------------------------------------------- | -------------------------- |
| Um jogador completou linha, coluna ou diagonal | `X venceu!` ou `O venceu!` |
| Ninguém venceu e não há casas vazias           | `Deu velha!`               |
| Ninguém venceu e ainda há casas vazias         | `Jogo em andamento`        |

> 💡 Dica: na diagonal principal, linha e coluna são iguais (`[0][0]`, `[1][1]`, `[2][2]`); na secundária, somam 2 (`[0][2]`, `[1][1]`, `[2][0]`).

### Exemplo de execução

```text
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
```

---

## Exercício 5 — Média ponderada com NumPy

> ⚠️ Este exercício precisa do NumPy. Instale uma única vez, no terminal ou no console do Spyder: `pip install numpy`

Uma disciplina tem 4 avaliações com pesos diferentes:

| Avaliação | P1  | P2  | Trabalho | Projeto |
| --------- | --- | --- | -------- | ------- |
| Peso      | 20% | 20% | 30%      | 30%     |

Guarde os pesos em um array do NumPy (constante `PESOS`) e crie as funções:

* `le_turma(n)`: lê o nome e as 4 notas (em uma única linha) de `n` alunos. Retorna a lista de nomes e um **array do NumPy** com as notas;
* `medias_ponderadas(notas, pesos=PESOS)`: retorna o array de médias, calculado com `np.dot`;
* `situacao(media, minimo=6.0)`: retorna `"Aprovado"` ou `"Reprovado"`;
* `aplica_acrescimo(notas, percentual=10)`: retorna um **novo array** com todas as notas aumentadas no percentual informado (sem laço; não é preciso limitar a 10);
* `conta_novos_aprovados(antes, depois, minimo=6.0)`: recebe as médias antes e depois do acréscimo e retorna quantos alunos passaram de reprovado para aprovado.

Na `main()`, leia quantos alunos a turma tem e mostre o `shape` das notas, a média e a situação de cada aluno, a média da turma em cada avaliação (use `mean(axis=0)`), as médias com acréscimo de 10% e quantos alunos passariam a ser aprovados.

### Exemplo de execução

```text
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
```
