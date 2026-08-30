# Exercícios de Programação — Estruturas Condicionais

## Bloco 1 — `if/else` simples

### Exercício 1 — Elegibilidade para Votação
Leia a idade de uma pessoa e informe se ela já pode votar ou não.
Considere que o voto é permitido a partir dos 16 anos.
Utilize uma estrutura `if/else` para realizar a verificação.

---

### Exercício 2 — Número Positivo ou Negativo
Leia um número inteiro e informe se ele é positivo ou negativo.
Considere zero como um valor positivo.
Utilize uma estrutura `if/else` para realizar a verificação.

---

## Bloco 2 — `if/else` aninhado

### Exercício 3 — Carteira de Motorista
Peça a idade de uma pessoa.
Se for maior ou igual a 18 anos, verifique se possui carteira de motorista (CNH):
- Se sim, mostre "Pode dirigir".
- Se não, mostre "Precisa tirar a carteira".

Se for menor de 18 anos, mostre "Não pode dirigir".

---

### Exercício 4 — Positivo, Negativo, Zero, Par ou Ímpar
Peça um número inteiro.
Se o número for positivo, verifique se é par ou ímpar.
Se o número for negativo, mostre "Número negativo".
Se for zero, mostre "Zero não é positivo nem negativo".

---

### Exercício 5 — Par/Ímpar e Comparação de Dois Números
Peça ao usuário um número inteiro, verifique se ele é par ou ímpar e exiba o resultado na tela.
Em seguida, solicite dois novos números inteiros, compare-os e informe qual deles é o maior, ou se ambos são iguais.

---

## Bloco 3 — Operadores relacionais e lógicos

### Exercício 6 — Validação de Usuário e Senha
Peça um usuário e uma senha.
- Se usuário `unisa` e senha `1234`: pergunte se deseja acessar como administrador — "sim" mostra "Acesso total!", caso contrário "Acesso restrito".
- Se usuário `usuario` e senha `5678`: mostre "Acesso externo".
- Caso contrário: mostre "Usuário ou senha inválidos".

---

### Exercício 7 — Situação do Aluno
Peça a média final do aluno e o percentual de faltas.

Se a média for maior ou igual a 7:
- Se tiver menos de 25% de faltas, mostre "Aprovado".
- Caso contrário, mostre "Reprovado por falta".

Se a média for menor que 7, mostre "Reprovado por nota".

Valide também as entradas: médias fora do intervalo de 0 a 10 e percentuais de faltas fora de 0 a 100 devem ser rejeitados com uma mensagem de erro.

**Saída esperada:**
```
Situação: Aprovado
```
