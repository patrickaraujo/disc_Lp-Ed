# Lista de Exercícios — Listas, Tuplas, Dicionários e Funções

# Parte 1 — Listas e Tuplas

## Exercício 1 — Explorando uma lista

Peça ao usuário **números inteiros**, um por vez, até que ele digite **0** (o zero não entra na lista). O usuário deve digitar pelo menos 3 números.

Depois, mostre:

* a) a lista completa e quantos números ela tem;
* b) os 3 primeiros e os 3 últimos números, usando **fatiamento**;
* c) a lista de trás para frente, usando um `for` com `range` decrescente;
* d) uma nova lista com o quadrado de cada número, criada com **compreensão de lista**.

### Exemplo de execução

```text
Digite um número (0 para parar): 3
Digite um número (0 para parar): 8
Digite um número (0 para parar): 1
Digite um número (0 para parar): 5
Digite um número (0 para parar): 2
Digite um número (0 para parar): 0
Lista: [3, 8, 1, 5, 2] (5 números)
3 primeiros: [3, 8, 1]
3 últimos: [1, 5, 2]
De trás para frente:
2
5
1
8
3
Quadrados: [9, 64, 1, 25, 4]
```

---

## Exercício 2 — Temperaturas da semana

Os dias da semana nunca mudam, então guarde-os em uma **tupla**:

```python
dias = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")
```

Leia a temperatura (em °C) de cada dia, guardando-as em uma **lista**. Em seguida, mostre:

* a lista de temperaturas;
* a temperatura média da semana;
* a maior e a menor temperatura, e **em que dia** cada uma ocorreu;
* quantos dias tiveram temperatura acima de 30°C.

> ⚠️ Não use as funções prontas `sum()`, `max()` e `min()`: percorra a lista com um laço.

### Exemplo de execução

```text
Temperatura de Dom: 28
Temperatura de Seg: 31
Temperatura de Ter: 33
Temperatura de Qua: 22
Temperatura de Qui: 19
Temperatura de Sex: 30
Temperatura de Sáb: 25
Temperaturas: [28.0, 31.0, 33.0, 22.0, 19.0, 30.0, 25.0]
Média: 26.9°C
Maior: 33.0°C (Ter)
Menor: 19.0°C (Qui)
Dias acima de 30°C: 2
```

---

## Exercício 3 — Pontos no plano

Pergunte quantos pontos serão digitados. Depois, leia cada ponto em **uma linha**, no formato `x y`, e guarde-o como uma **tupla** `(x, y)` dentro de uma lista.

Ao final, mostre:

* a lista de pontos;
* o quadrante de cada ponto (**desempacote** a tupla em `x` e `y`):

| Condição                 | Resultado       |
| ------------------------ | --------------- |
| `x > 0` e `y > 0`        | 1º quadrante    |
| `x < 0` e `y > 0`        | 2º quadrante    |
| `x < 0` e `y < 0`        | 3º quadrante    |
| `x > 0` e `y < 0`        | 4º quadrante    |
| `x` ou `y` igual a zero  | Sobre um eixo   |

* o ponto mais distante da origem, sabendo que `distância = (x² + y²) ** 0.5`.

### Exemplo de execução

```text
Quantos pontos? 3
Ponto 1 (x y): 2 3
Ponto 2 (x y): -4 1
Ponto 3 (x y): 0 -2
Pontos: [(2.0, 3.0), (-4.0, 1.0), (0.0, -2.0)]
(2.0, 3.0) -> 1º quadrante
(-4.0, 1.0) -> 2º quadrante
(0.0, -2.0) -> Sobre um eixo
Mais distante da origem: (-4.0, 1.0) (distância 4.12)
```

---

# Parte 2 — Dicionários

## Exercício 4 — Contador de palavras

Leia uma frase e conte quantas vezes cada palavra aparece, usando um **dicionário** em que a palavra é a chave e a quantidade é o valor. Considere maiúsculas e minúsculas como iguais.

Ao final:

* mostre cada palavra e sua quantidade (use `items()`);
* mostre quantas palavras **diferentes** a frase tem;
* mostre a palavra mais frequente (em caso de empate, qualquer uma);
* peça uma palavra ao usuário e informe quantas vezes ela aparece, usando `get()` (se não aparecer, deve mostrar 0).

> 💡 Dica: `frase.split()` devolve uma lista com as palavras da frase.

### Exemplo de execução

```text
Digite uma frase: o rato roeu a roupa do rei e o rei riu
o: 2
rato: 1
roeu: 1
a: 1
roupa: 1
do: 1
rei: 2
e: 1
riu: 1
Palavras diferentes: 9
Mais frequente: o (2 vezes)
Qual palavra deseja consultar? rato
'rato' aparece 1 vez(es)
```

---

## Exercício 5 — Estoque da farmácia

Uma farmácia controla o estoque em um dicionário:

```python
estoque = {"dipirona": 100, "paracetamol": 50, "vitamina c": 30}
```

Leia movimentações até o usuário digitar `fim` no nome do produto. Para cada movimentação, leia o produto e a quantidade: quantidade **positiva** é entrada e quantidade **negativa** é saída.

Regras:

* produto que não existe com quantidade positiva: cadastre-o no estoque;
* produto que não existe com quantidade negativa: mostre `Produto não cadastrado`;
* saída maior que o estoque disponível: mostre `Estoque insuficiente` e não altere o estoque.

Ao final, mostre:

* o estoque de cada produto;
* o total de unidades na farmácia (percorra `values()`);
* uma **lista** com os produtos com estoque baixo (menos de 20 unidades).

### Exemplo de execução

```text
Produto (ou 'fim'): dipirona
Quantidade (+ entrada / - saída): -90
Produto (ou 'fim'): amoxicilina
Quantidade (+ entrada / - saída): 15
Produto (ou 'fim'): vitamina c
Quantidade (+ entrada / - saída): -40
Estoque insuficiente: há apenas 30 unidade(s).
Produto (ou 'fim'): fim
--- Estoque ---
dipirona: 10
paracetamol: 50
vitamina c: 30
amoxicilina: 15
Total de unidades: 105
Estoque baixo: ['dipirona', 'amoxicilina']
```

---

# Parte 3 — Funções

## Exercício 6 — Funções numéricas

Crie as funções abaixo. Todas devem **retornar** o resultado (nada de `print` dentro delas). Considere apenas inteiros positivos.

| Função                  | O que retorna                                                    |
| ----------------------- | ---------------------------------------------------------------- |
| `reverso(n)`            | O número ao contrário. Ex.: `127 -> 721`                         |
| `quantidade_digitos(n)` | Quantos dígitos o número tem. Ex.: `2026 -> 4`                   |
| `potencia(a, b=2)`      | `a` elevado a `b` **sem usar `**`**. Sem `b`, calcula o quadrado |

Na `main()`, leia `n` e mostre o reverso e a quantidade de dígitos. Depois, leia `a` e `b` e mostre `potencia(a, b)` e `potencia(a)`.

> 💡 Dica: `n % 10` devolve o último dígito de `n`, e `n // 10` remove o último dígito.

### Exemplo de execução

```text
Digite um número inteiro positivo: 127
Reverso: 721
Quantidade de dígitos: 3
Base: 3
Expoente: 4
3 elevado a 4 = 81
3 ao quadrado = 9
```

---

## Exercício 7 — Caixa eletrônico

Um caixa eletrônico entrega cédulas de R$ 100, 50, 20 e 10, sempre usando a **menor quantidade** de cédulas possível. Crie as funções:

* `valor_valido(valor)`: retorna `True` se o valor for positivo e múltiplo de 10; senão, `False`;
* `calcula_cedulas(valor, cedulas=(100, 50, 20, 10))`: retorna um **dicionário** `{cédula: quantidade}` só com as cédulas usadas;
* `mostra_cedulas(resultado)`: mostra o dicionário de forma organizada (não retorna nada).

Na `main()`, leia valores de saque até o usuário digitar `0`. Para cada valor válido, mostre as cédulas do caixa normal e as de um caixa que só tem notas de 50 e 10, chamando `calcula_cedulas` com **argumento nomeado**.

> 💡 Dica: `valor // cedula` diz quantas cédulas cabem; `valor % cedula` é o que sobra.

### Exemplo de execução

```text
Valor do saque (0 para sair): 380
Caixa completo:
  3 x R$ 100
  1 x R$ 50
  1 x R$ 20
  1 x R$ 10
Caixa só com 50 e 10:
  7 x R$ 50
  3 x R$ 10
Valor do saque (0 para sair): 75
Valor inválido: use múltiplos de 10.
Valor do saque (0 para sair): 0
```

---

## Exercício 8 — Lista de tarefas

Crie um gerenciador de tarefas com um menu que se repete até o usuário sair:

```text
1 - Adicionar tarefa
2 - Concluir tarefa
3 - Mostrar tarefas
0 - Sair
```

Regras:

* A lista de tarefas deve ser criada **dentro da `main()`** e passada como parâmetro para as funções.
* Use uma variável **global** `concluidas` para contar quantas tarefas foram concluídas.
* Funções obrigatórias:
  * `adicionar(tarefas, texto)`: acrescenta a tarefa (sem `return`);
  * `concluir(tarefas, numero)`: remove a tarefa pela posição mostrada ao usuário (começando em 1) e soma 1 em `concluidas`. Retorna `True` se conseguiu e `False` se a posição for inválida;
  * `mostrar(tarefas)`: mostra as tarefas numeradas a partir de 1.
* Ao sair, mostre quantas tarefas foram concluídas e quantas ficaram pendentes.

**Responda também, em comentários no seu código:**

* a) Por que `adicionar()` altera a lista da `main()` mesmo sem `return`?
* b) Por que `concluir()` precisa da palavra `global` e `adicionar()` não?
* c) O que aconteceria se `adicionar()` fizesse `tarefas = tarefas + [texto]` em vez de `tarefas.append(texto)`?

### Exemplo de execução (trecho)

```text
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
```
