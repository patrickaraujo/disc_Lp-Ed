# Lista de Exercícios — Revisão 2 (prática)

> Revisão para as provas: dicionários, tuplas, matrizes (listas de listas), NumPy, ordenação e busca.  
> Os exercícios tutoreados (`exTutoreado01.py` e `exTutoreado02.py`) estão na pasta `codigos`.
>
> 🧠 **Dica de prova:** antes de rodar, faça o **teste de mesa**. Em matrizes, anote `[linha][coluna]`; em ordenação, anote a lista depois de cada passada; na busca binária, anote `inicio`, `fim` e `meio` a cada passo.

## Exercício 1 — Contador de palavras

Leia uma frase e conte quantas vezes cada palavra aparece, usando um dicionário `{palavra: quantidade}`. Ignore maiúsculas/minúsculas e os sinais `. , ! ?` no fim das palavras.

Mostre:

* cada palavra com sua contagem, na ordem em que apareceu;
* a palavra mais frequente (em caso de empate, a que apareceu primeiro);
* quantas palavras aparecem uma única vez.

> ⚠️ Não use `Counter`, `max()` nem `sorted()`.  
> 💡 Dica: `contagem.get(palavra, 0)` devolve 0 quando a palavra ainda não é chave do dicionário.

### Exemplo de execução

```text
Frase: O rato roeu a roupa do rei de Roma, e o rei roeu a rolha!
o: 2
rato: 1
roeu: 2
a: 2
roupa: 1
do: 1
rei: 2
de: 1
roma: 1
e: 1
rolha: 1
Mais frequente: "o" (2 vezes)
Palavras que aparecem uma única vez: 7
```

---

## Exercício 2 — Agenda de contatos

Guarde os contatos em um dicionário `{nome: (telefone, email)}`, em que o valor é uma **tupla**. Faça um menu com `match-case` que se repete até a opção 0:

| Opção | Ação                                              |
|-------|---------------------------------------------------|
| 1     | Adicionar contato (avise se o nome já existir)    |
| 2     | Buscar contato (avise se não existir)             |
| 3     | Atualizar telefone (o e-mail continua o mesmo)    |
| 4     | Listar contatos                                   |
| 0     | Sair                                              |

> ⚠️ Tuplas são imutáveis: para atualizar o telefone, monte uma **nova** tupla com o telefone novo e o e-mail antigo.

### Exemplo de execução (trecho)

```text
Opção: 1
Nome: Ana
Telefone: 99999-1111
E-mail: ana@email.com
Contato adicionado.
Opção: 3
Nome: Ana
Novo telefone: 98888-2222
Telefone atualizado.
Opção: 2
Nome: Ana
Ana | 98888-2222 | ana@email.com
Opção: 2
Nome: Bruno
Contato não encontrado.
Opção: 0
Agenda encerrada.
```

---

## Exercício 3 — Mapa de assentos do cinema

Uma sala tem 5 fileiras (A a E) com 8 poltronas cada. Represente a sala como uma **matriz** (lista de listas), em que `0` = livre e `1` = ocupada.

Crie as funções:

| Função                            | O que faz                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------|
| `criar_sala(fileiras, poltronas)` | devolve a matriz toda com 0, montada com laços                                              |
| `reservar(sala, fileira, numero)` | devolve `"Reservada"`, `"Poltrona já ocupada"` ou `"Fileira ou poltrona inválida"`          |
| `mostrar(sala)`                   | imprime o mapa (`L` = livre, `X` = ocupada)                                                 |
| `livres_por_fileira(sala)`        | devolve uma lista com a quantidade de lugares livres de cada fileira                        |

Faça as reservas abaixo, mostre o mapa, os livres por fileira e a fileira com mais lugares livres.

```python
pedidos = [("A", 3), ("A", 4), ("C", 1), ("C", 8), ("E", 5),
           ("A", 3), ("F", 2), ("B", 9), ("B", 2), ("B", 3), ("B", 4)]
```

> 💡 A fileira é uma letra e a poltrona vai de 1 a 8, mas a matriz começa no índice 0: converta antes de acessar `sala[i][j]`.  
> ⚠️ Cuidado com `[[0] * 8] * 5`: as 5 linhas seriam a **mesma** lista.

### Exemplo de execução

```text
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
```

---

## Exercício 4 — Conta de energia com NumPy

Uma vila tem 3 casas. O consumo (kWh) de cada casa em 4 meses foi lido em sequência, casa por casa:

```python
leituras = [210, 185, 230, 250,   150, 140, 160, 175,   320, 300, 290, 335]
```

1. Transforme as leituras em um array NumPy 3 × 4 (casas × meses) com `reshape`.
2. Calcule a matriz de custos: R$ 0,85 por kWh mais uma taxa fixa de R$ 12,00 por mês, **com o array inteiro, sem laço**.
3. Crie com `np.zeros` um array para o total de cada casa e preencha-o com laços aninhados.
4. Mostre a casa com o maior total e quantos meses, somando todas as casas, passaram de 250 kWh.
5. Simule uma meta de economia de 10% (`consumo * 0.9`) e mostre a nova matriz.

### Exemplo de execução

```text
Consumo (kWh):
[[210 185 230 250]
 [150 140 160 175]
 [320 300 290 335]]
Custos (R$):
[[190.5  169.25 207.5  224.5 ]
 [139.5  131.   148.   160.75]
 [284.   267.   258.5  296.75]]
Total por casa: [ 791.75  579.25 1106.25]
Casa com maior conta: 3 (R$ 1106.25)
Meses acima de 250 kWh: 4
Consumo com 10% de economia:
[[189.  166.5 207.  225. ]
 [135.  126.  144.  157.5]
 [288.  270.  261.  301.5]]
```

---

## Exercício 5 — Bubble Sort com parada antecipada

Implemente `bubbleSort(lista)`, que ordena a lista em ordem crescente e devolve uma **tupla** `(passadas, comparacoes, trocas)`.

Use uma variável `trocou`: se uma passada inteira terminar **sem nenhuma troca**, a lista já está ordenada e o algoritmo deve parar.

Teste com as três listas e responda em um comentário: por que a lista quase ordenada termina tão mais rápido que a invertida?

```python
quase_ordenada = [1, 2, 3, 5, 4, 6]
embaralhada    = [5, 1, 4, 2, 8, 3]
invertida      = [6, 5, 4, 3, 2, 1]
```

### Exemplo de execução

```text
quase ordenada: [1, 2, 3, 4, 5, 6] | passadas=2 comparações=9 trocas=1
embaralhada: [1, 2, 3, 4, 5, 8] | passadas=4 comparações=14 trocas=7
invertida: [1, 2, 3, 4, 5, 6] | passadas=5 comparações=15 trocas=15
```
