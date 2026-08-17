# Exercícios de Lógica e Programação

## Exercício 1 — O lobo, o cordeiro e as alfaces — Tutoreado

Um homem precisa atravessar um rio utilizando um barco. Com ele estão:

* um **lobo**;
* um **cordeiro**;
* uma **caixa de alfaces**.

O barco possui espaço apenas para o homem e **mais um item por vez**.

Durante a travessia, algumas regras precisam ser respeitadas:

* O **lobo não pode ficar sozinho com o cordeiro**, pois o lobo atacará o cordeiro.
* O **cordeiro não pode ficar sozinho com as alfaces**, pois ele comerá as alfaces.

**Desafio:** determine uma sequência de travessias que permita levar o homem, o lobo, o cordeiro e as alfaces para a outra margem sem violar nenhuma das restrições.

### Resolução

1. Levar o **cordeiro** para a outra margem.
2. Voltar **sozinho**.
3. Levar o **lobo** para a outra margem.
4. Voltar trazendo o **cordeiro**.
5. Levar as **alfaces** para a outra margem.
6. Voltar **sozinho**.
7. Levar o **cordeiro** para a outra margem.

> **Ponto-chave:** a dificuldade não está apenas em realizar as travessias, mas em garantir que **nenhuma das restrições seja violada em nenhum momento**.

---

## Exercício 2 — Torre de Hanói

Na **Torre de Hanói**, três discos de tamanhos diferentes estão inicialmente empilhados em um dos pinos, em ordem decrescente de tamanho, com o maior disco embaixo e o menor em cima.

O objetivo é transferir todos os discos para outro pino, utilizando um terceiro pino como auxiliar.

Durante os movimentos, as seguintes regras devem ser respeitadas:

* Apenas **um disco pode ser movimentado por vez**.
* Somente o disco que está no **topo de uma pilha** pode ser movimentado.
* Um disco **maior nunca pode ser colocado sobre um disco menor**.

**Desafio:** transfira os três discos da torre inicial para a torre de destino respeitando todas as regras.

Você pode utilizar o simulador abaixo para praticar:

https://www.hypatiamat.com/jogos/torreHanoi/torreHanoi_HTML.html

---

# Exercícios de Programação

## Exercício 3 — Soma de dois números

Peça ao usuário **dois números inteiros** e calcule a soma entre eles.

Em seguida, verifique se o resultado da soma é **maior que 20**.

### Saída esperada

```text
A soma é maior que 20? True
```

ou

```text
A soma é maior que 20? False
```

---

## Exercício 4 — Limite de peso de uma caixa

Uma caixa suporta no máximo **50 kg**.

Peça ao usuário:

* o peso atual da caixa;
* o peso do objeto que ele deseja adicionar.

Calcule o peso total e verifique se o novo objeto pode ser colocado na caixa sem ultrapassar o limite de **50 kg**.

### Saída esperada

```text
Cabe dentro da caixa? True
```

ou

```text
Cabe dentro da caixa? False
```

---

## Exercício 5 — Temperatura agradável

Peça ao usuário a **temperatura atual**.

Considere que uma temperatura é agradável quando está **entre 20 °C e 25 °C**, incluindo os valores 20 e 25.

Verifique se a temperatura informada está dentro desse intervalo.

### Saída esperada

```text
A temperatura está agradável? True
```

ou

```text
A temperatura está agradável? False
```

---

## Exercício 6 — Estoque da farmácia

Uma farmácia possui inicialmente **100 unidades** de determinado remédio.

Peça ao usuário a quantidade de unidades que foram vendidas.

Calcule o **estoque final** e verifique se ele ficou com menos de **20 unidades**.

### Saída esperada

```text
Estoque baixo? True
```

ou

```text
Estoque baixo? False
```

---

## Exercício 7 — Controle de velocidade

A velocidade máxima permitida em uma via é de **80 km/h**.

Peça ao usuário a velocidade do carro e verifique se ela está **acima de 80 km/h**.

Caso esteja acima do limite, considere que o carro foi multado.

### Saída esperada

```text
O carro foi multado? True
```

ou

```text
O carro foi multado? False
```

---

## Exercício 8 — Aprovação do aluno

Peça ao usuário:

* a **nota da prova**;
* a **frequência do aluno**, em porcentagem.

O aluno será aprovado somente se:

* sua nota for **maior ou igual a 6**; **e**
* sua frequência for **maior ou igual a 75%**.

Verifique se o aluno atende aos dois critérios.

### Saída esperada

```text
Aluno aprovado? True
```

ou

```text
Aluno aprovado? False
```
