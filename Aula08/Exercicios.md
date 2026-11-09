# Lista de Exercícios — Ordenação e Busca

> **Exercícios 1 a 3:** ordenação (Selection, Insertion e Bubble Sort).  
> **Exercícios 4 a 6:** busca sequencial e binária.

## Exercício 1 — Notas em ordem decrescente

Leia 5 notas digitadas pelo usuário e guarde-as em uma lista. Crie a função
`ordena_decrescente(lista)`, que ordena a lista da MAIOR para a MENOR nota
usando o Selection Sort (não use `sort()` nem `sorted()`).

Na `main()`, mostre a lista antes e depois da ordenação.

> 💡 Dica: no Selection Sort crescente procuramos o MENOR elemento. Para a ordem
decrescente, basta procurar o MAIOR, invertendo a comparação.

### Exemplo de execução

```text
Nota 1: 7.5
Nota 2: 9
Nota 3: 6
Nota 4: 10
Nota 5: 8.5
Antes: [7.5, 9.0, 6.0, 10.0, 8.5]
Depois: [10.0, 9.0, 8.5, 7.5, 6.0]
```

---

## Exercício 2 — Lista de nomes em ordem alfabética

Leia 5 nomes digitados pelo usuário e guarde-os em uma lista. Crie a função
`ordena_nomes(lista)`, que coloca os nomes em ordem alfabética usando o
Insertion Sort.

Na `main()`, mostre os nomes ordenados, um por linha, numerados.

> 💡 Dica: os operadores < e > também funcionam com strings. O Python compara as
palavras letra por letra, como no dicionário: "Ana" < "Bruno" é True. Atenção:
letras maiúsculas vêm antes das minúsculas ("Zeca" < "ana" é True), então
digite todos os nomes com a inicial maiúscula.

### Exemplo de execução

```text
Nome 1: Rafael
Nome 2: Beatriz
Nome 3: Carlos
Nome 4: Ana
Nome 5: Mariana
Em ordem alfabética:
  1. Ana
  2. Beatriz
  3. Carlos
  4. Mariana
  5. Rafael
```

---

## Exercício 3 — Menor e maior idade

Leia a quantidade de pessoas de um grupo e, em seguida, a idade de cada uma.
Crie a função `bubble_sort(lista)`, que ordena as idades em ordem crescente
usando o Bubble Sort.

Na `main()`, mostre as idades ordenadas, a menor idade e a maior idade.

> 💡 Dica: depois de ordenar, a menor idade está na primeira posição (lista[0]) e
a maior está na última (lista[-1]).

### Exemplo de execução

```text
Quantas pessoas? 5
Idade da pessoa 1: 34
Idade da pessoa 2: 19
Idade da pessoa 3: 52
Idade da pessoa 4: 27
Idade da pessoa 5: 8
Idades ordenadas: [8, 19, 27, 34, 52]
Menor idade: 8
Maior idade: 52
```

---

## Exercício 4 — Lista de convidados

A lista de convidados de uma festa é:

```python
convidados = ["Marcos", "Júlia", "Pedro", "Larissa", "Tiago", "Camila"]
```

Crie a função `busca_sequencial(lista, chave)`, que retorna a posição do nome
na lista ou -1 se o nome não estiver nela.

Na `main()`, leia o nome de uma pessoa e mostre se ela foi convidada e em qual
posição da lista ela está.

### Exemplos de execução

```text
Nome: Larissa
Larissa foi convidado(a)! Posição na lista: 3
```

```text
Nome: Fernanda
Fernanda não está na lista de convidados.
```

---

## Exercício 5 — Busca binária em uma lista ordenada

Considere a lista ordenada:

```python
numeros = [3, 8, 12, 17, 25, 31, 40, 52, 66, 79]
```

Crie a função `busca_binaria(lista, chave)`, que retorna a posição da chave na
lista ou -1 se ela não estiver na lista.

Na `main()`, leia um número e mostre a posição dele ou a mensagem
"Número não encontrado".

### Exemplos de execução

```text
Número procurado: 40
Número encontrado na posição 6
```

```text
Número procurado: 20
Número não encontrado
```

---

## Exercício 6 — Ordenar e depois buscar

A busca binária só funciona em listas ordenadas. Leia 6 números inteiros
digitados pelo usuário (sem nenhuma ordem) e:

1. ordene a lista com o Insertion Sort;
2. mostre a lista ordenada;
3. leia um número e use a busca binária para dizer se ele está na lista.

Reaproveite as funções dos exercícios anteriores: `insertion_sort(lista)` e
`busca_binaria(lista, chave)`.

### Exemplo de execução

```text
Número 1: 15
Número 2: 4
Número 3: 23
Número 4: 8
Número 5: 42
Número 6: 16
Lista ordenada: [4, 8, 15, 16, 23, 42]
Número procurado: 23
23 está na posição 4 da lista ordenada
```
