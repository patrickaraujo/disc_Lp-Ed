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

# Exercícios de Programação e Fluxograma

## Exercício 3 — Perímetro

Faça um algoritmo que leia o valor do lado de um quadrado e calcule o seu perímetro.

---

## Exercício 4 — Dobro de um número

Faça um algoritmo que leia um número e mostre o dobro dele.

---

## Exercício 5 — Retângulo

Faça um algoritmo que leia a base e a altura de um retângulo e calcule sua área.

---

## Exercício 6 — Conversão de temperaturas

Faça um algoritmo que leia uma temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = (C × 1,8) + 32

---

## Exercício 7 — Salário

Faça um algoritmo que leia a quantidade de horas trabalhadas e o valor pago por hora, e calcule o salário final.

---

## Exercício 8 — Conversão de moedas

Faça um algoritmo que leia um valor em reais (R$) e a cotação do dólar, e calcule quantos dólares a pessoa poderá comprar.
