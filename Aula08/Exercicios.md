# Lista de Exercícios — Ordenação e Busca

> **Exercícios 1 a 3:** ordenação (Selection, Insertion e Bubble Sort).  
> **Exercícios 4 a 6:** busca sequencial e binária.

## Exercício 1 — Ranking de um campeonato

Leia quantos jogadores participaram de um campeonato e, para cada um, o nome
e a pontuação. Guarde cada jogador como uma tupla (nome, pontos) em uma lista.
Crie as funções:

- `le_jogadores(n)`: lê e retorna a lista de tuplas;
- `ordena_ranking(jogadores)`: ordena a lista pela pontuação, da MAIOR para a
  MENOR, usando o Selection Sort (não use `sort()` nem `sorted()`);
- `mostra_ranking(jogadores)`: mostra a posição, o nome e os pontos de cada um.

Na `main()`, mostre o ranking completo e o pódio (os 3 primeiros). Se houver
menos de 3 jogadores, o pódio mostra apenas os que existem.

> 💡 Dica: a pontuação é a posição 1 da tupla: jogadores[j][1].

### Exemplo de execução

```text
Quantos jogadores? 5
Nome do jogador 1: Lia
Pontos de Lia: 340
Nome do jogador 2: Rafa
Pontos de Rafa: 510
Nome do jogador 3: Téo
Pontos de Téo: 275
Nome do jogador 4: Bia
Pontos de Bia: 510
Nome do jogador 5: Caio
Pontos de Caio: 420
Ranking final:
  1º Rafa      510 pts
  2º Bia       510 pts
  3º Caio      420 pts
  4º Lia       340 pts
  5º Téo       275 pts
Pódio:
  Ouro: Rafa
  Prata: Bia
  Bronze: Caio
```

---

## Exercício 2 — Boletim em ordem de nota

Leia o nome e as duas notas (P1 e P2, digitadas na mesma linha) de n alunos.
Para cada aluno, guarde uma tupla (nome, media). Crie as funções:

- `le_boletim(n)`: lê os alunos e retorna a lista de tuplas (nome, media),
  em que media é a média aritmética das duas notas;
- `ordena_por_media(boletim)`: ordena a lista pela média, da MAIOR para a
  MENOR, usando o Insertion Sort;
- `situacao(media)`: retorna "Aprovado" (media >= 6), "Exame" (4 <= media < 6)
  ou "Reprovado" (media < 4).

Na `main()`, mostre o boletim ordenado, com a situação de cada aluno, e
quantos alunos ficaram em cada situação. Use um dicionário para contar.

> ⚠️ Atenção: alunos com a mesma média devem aparecer na ordem em que foram
digitados. Use a comparação estrita (<) no while do Insertion Sort.

### Exemplo de execução

```text
Quantos alunos? 5
Nome do aluno 1: Ana
Notas de Ana (P1 P2): 7 8
Nome do aluno 2: Bruno
Notas de Bruno (P1 P2): 5 4
Nome do aluno 3: Carla
Notas de Carla (P1 P2): 9.5 9
Nome do aluno 4: Diego
Notas de Diego (P1 P2): 3 4
Nome do aluno 5: Elisa
Notas de Elisa (P1 P2): 8 7
Boletim (da maior para a menor média):
  Carla     9.25  Aprovado
  Ana       7.50  Aprovado
  Elisa     7.50  Aprovado
  Bruno     4.50  Exame
  Diego     3.50  Reprovado
Resumo:
  Aprovado: 3
  Exame: 1
  Reprovado: 1
```

---

## Exercício 3 — Fila de atendimento por prioridade

Em um pronto atendimento, cada paciente recebe uma classificação de risco:

| Prioridade | Classificação |
| ---------- | ------------- |
| 3          | Emergência    |
| 2          | Urgente       |
| 1          | Pouco urgente |

Leia os pacientes até que o nome digitado seja FIM. Para cada paciente, leia
a prioridade (aceite apenas 1, 2 ou 3; se for outro valor, mostre
"Prioridade inválida" e peça de novo). Guarde cada paciente como uma tupla
(nome, prioridade), na ordem de chegada. Crie as funções:

- `le_prioridade(nome)`: lê e retorna uma prioridade válida;
- `ordena_fila(fila)`: ordena a fila pela prioridade, da MAIOR para a MENOR,
  usando o Bubble Sort;
- `mostra_fila(fila, classificacao)`: mostra a ordem de atendimento.

Use um dicionário para traduzir a prioridade na classificação:
{3: "Emergência", 2: "Urgente", 1: "Pouco urgente"}.

> ⚠️ Atenção: entre pacientes com a MESMA prioridade, quem chegou primeiro deve ser
atendido primeiro. Por isso, só troque dois vizinhos quando a prioridade do
da direita for ESTRITAMENTE maior.

### Exemplo de execução

```text
Nome do paciente (FIM para encerrar): Marta
Prioridade de Marta (1 a 3): 1
Nome do paciente (FIM para encerrar): João
Prioridade de João (1 a 3): 3
Nome do paciente (FIM para encerrar): Pedro
Prioridade de Pedro (1 a 3): 2
Nome do paciente (FIM para encerrar): Rita
Prioridade de Rita (1 a 3): 5
Prioridade inválida
Prioridade de Rita (1 a 3): 3
Nome do paciente (FIM para encerrar): Lucas
Prioridade de Lucas (1 a 3): 2
Nome do paciente (FIM para encerrar): Sônia
Prioridade de Sônia (1 a 3): 1
Nome do paciente (FIM para encerrar): fim
Ordem de atendimento:
  1. João     (Emergência)
  2. Rita     (Emergência)
  3. Pedro    (Urgente)
  4. Lucas    (Urgente)
  5. Marta    (Pouco urgente)
  6. Sônia    (Pouco urgente)
```

---

## Exercício 4 — Consulta de alunos por RA

A secretaria guarda o cadastro dos alunos em uma lista de tuplas
(ra, nome, curso), na ordem em que foram matriculados (sem ordenação):

```python
cadastro = [(20261045, "Ana Souza", "ADS"),
            (20258812, "Bruno Lima", "Ciência da Computação"),
            (20263390, "Carla Dias", "Engenharia de Software"),
            (20250127, "Diego Rocha", "ADS"),
            (20262274, "Elisa Melo", "Sistemas de Informação")]
```

Crie a função `busca_ra(cadastro, ra)`, que usa a busca sequencial e retorna o
ÍNDICE do aluno com aquele RA, ou -1 se o RA não existir.

Na `main()`, peça RAs ao usuário até que ele digite 0. Para cada RA, mostre o
nome e o curso do aluno ou a mensagem "RA não encontrado". Ao final, mostre
quantas consultas foram feitas e quantas encontraram um aluno.

Por que usar a busca sequencial aqui, e não a binária? (Responda em um
comentário no código.)

### Exemplo de execução

```text
RA (0 para sair): 20263390
  Carla Dias - Engenharia de Software
RA (0 para sair): 20250000
  RA não encontrado
RA (0 para sair): 20250127
  Diego Rocha - ADS
RA (0 para sair): 0
Consultas: 3 | Encontrados: 2
```

---

## Exercício 5 — Consulta de preços no caixa

O caixa de um mercado tem a lista de produtos ORDENADA pelo código de barras
(curto, para facilitar). Cada produto é uma tupla (codigo, nome, preco):

```python
produtos = [(102, "Arroz 5kg", 27.90), (215, "Feijão 1kg", 8.49),
            (330, "Café 500g", 18.75), (418, "Leite 1L", 5.29),
            (527, "Açúcar 1kg", 4.99), (640, "Óleo 900ml", 7.80),
            (755, "Macarrão 500g", 4.35), (861, "Sabão em pó", 15.90)]
```

Crie a função `busca_produto(produtos, codigo)`, que usa a BUSCA BINÁRIA para
retornar o índice do produto ou -1.

Na `main()`, registre uma compra: leia códigos até o usuário digitar 0. Para
cada código, leia a quantidade, mostre o subtotal do item e acumule o total.
Se o código não existir, mostre "Produto não cadastrado" e não peça a
quantidade. Ao final, mostre a quantidade de itens e o valor total da compra.

> 💡 Dica: compare a chave com produtos[meio][0], o código do produto do meio.

### Exemplo de execução

```text
Código (0 para finalizar): 330
  Café 500g (R$ 18.75) - quantidade: 2
  Subtotal: R$ 37.50
Código (0 para finalizar): 999
  Produto não cadastrado
Código (0 para finalizar): 102
  Arroz 5kg (R$ 27.90) - quantidade: 1
  Subtotal: R$ 27.90
Código (0 para finalizar): 755
  Macarrão 500g (R$ 4.35) - quantidade: 3
  Subtotal: R$ 13.05
Código (0 para finalizar): 0
Itens: 6 | Total da compra: R$ 78.45
```

---

## Exercício 6 — O computador adivinha o seu número

Agora quem adivinha é o computador! O usuário pensa em um número de 1 a 100
e o programa tenta descobri-lo usando a ideia da busca binária: o chute é
sempre o MEIO do intervalo que ainda é possível. A cada chute, o usuário
responde:

| Resposta | Significado                            |
| -------- | -------------------------------------- |
| +        | O número pensado é MAIOR que o chute   |
| -        | O número pensado é MENOR que o chute   |
| =        | O computador acertou                   |

Crie as funções:

- `le_resposta(chute)`: mostra o chute e lê a resposta. Se não for +, - ou =,
  mostra "Responda com +, - ou =" e pergunta de novo;
- `adivinha(inicio, fim)`: conduz o jogo e retorna o número de tentativas, ou
  -1 se as respostas forem contraditórias (o intervalo ficou vazio, ou seja,
  inicio > fim).

Na `main()`, mostre em quantas tentativas o computador acertou ou a mensagem
"Respostas contraditórias! Você mudou de número?".

Pergunta para pensar: qual é o número MÁXIMO de tentativas para um número de
1 a 100? E de 1 a 1000?

### Exemplos de execução

```text
Pense em um número de 1 a 100.
É 50? (+ / - / =): +
É 75? (+ / - / =): -
É 62? (+ / - / =): x
Responda com +, - ou =
É 62? (+ / - / =): +
É 68? (+ / - / =): -
É 65? (+ / - / =): =
Acertei em 5 tentativa(s)!
```

```text
Pense em um número de 1 a 100.
É 50? (+ / - / =): +
É 75? (+ / - / =): +
É 88? (+ / - / =): +
É 94? (+ / - / =): +
É 97? (+ / - / =): +
É 99? (+ / - / =): +
É 100? (+ / - / =): +
Respostas contraditórias! Você mudou de número?
```
