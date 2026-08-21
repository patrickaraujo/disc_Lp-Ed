# 🐍 Entrada, Saída e Operações em Python

## Objetivos

Nesta aula vamos aprender a:

* Mostrar informações na tela com `print()`;
* Ler dados do usuário com `input()`;
* Realizar operações matemáticas;
* Entender a ordem das operações;
* Converter valores entre diferentes tipos.

---

# 1. Escrevendo na tela — `print()`

A função `print()` é utilizada para mostrar informações na tela.

```python
print("Olá, mundo!")
```

Saída:

```text
Olá, mundo!
```

Também podemos mostrar o conteúdo de variáveis:

```python
idade = 20

print("Idade:", idade)
```

Saída:

```text
Idade: 20
```

Podemos passar vários valores separados por vírgula. 

---

## Quebra de linha

O caractere `\n` cria uma nova linha.

```python
print("Olá!\nBem-vindo à aula.")
```

Saída:

```text
Olá!
Bem-vindo à aula.
```

Por padrão, cada `print()` termina com uma quebra de linha. É possível alterar isso usando `end`. 

```python
print("Python", end=" ")
print("é legal!")
```

Saída:

```text
Python é legal!
```

---

# 2. Lendo dados — `input()`

A função `input()` permite receber informações digitadas pelo usuário.

```python
nome = input("Digite seu nome: ")

print("Olá,", nome)
```

⚠️ **Importante:** o valor recebido por `input()` é sempre uma `string`. 

Exemplo:

```python
idade = input("Digite sua idade: ")

print(idade)
```

Mesmo digitando:

```text
20
```

o Python considera `"20"` como texto.

---

# 3. Conversão de tipos

Podemos converter valores utilizando:

| Função    | Converte para  |
| --------- | -------------- |
| `int()`   | Número inteiro |
| `float()` | Número decimal |
| `str()`   | Texto          |

Essas três funções são apresentadas nos slides como as principais formas de conversão de dados. 

### Inteiro

```python
idade = int(input("Digite sua idade: "))
```

### Decimal

```python
altura = float(input("Digite sua altura: "))
```

### Texto

```python
numero = 10

texto = str(numero)
```

---

## Exemplo

```python
numero = int(input("Digite um número: "))

resultado = numero * 10

print("Resultado:", resultado)
```

Se o usuário digitar `5`:

```text
Resultado: 50
```

---

## ⚠️ Cuidado com conversões

Nem todo valor pode ser convertido.

```python
numero = int("abc")
```

Isso gera um erro porque `"abc"` não representa um número. 

Também é importante observar:

```python
int(2.99)
```

Resultado:

```text
2
```

A parte decimal é descartada.

---

# 4. Expressões

Uma **expressão** é uma combinação de valores, variáveis e operadores que produz um resultado.

Exemplo:

```python
a = 10
b = 5

resultado = a + b
```

A expressão é:

```python
a + b
```

Expressões podem envolver operações aritméticas, lógicas ou relacionais. 

---

# 5. ➕ Operadores aritméticos

Os principais operadores matemáticos em Python são: 

| Operador | Operação         | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `+`      | Adição           | `10 + 5` | `15`      |
| `-`      | Subtração        | `10 - 5` | `5`       |
| `*`      | Multiplicação    | `10 * 5` | `50`      |
| `/`      | Divisão          | `5 / 2`  | `2.5`     |
| `//`     | Divisão inteira  | `5 // 2` | `2`       |
| `%`      | Resto da divisão | `5 % 2`  | `1`       |
| `**`     | Potenciação      | `2 ** 3` | `8`       |

---

## Divisão `/`

A divisão comum retorna um número decimal.

```python
5 / 2
```

Resultado:

```text
2.5
```

---

## Divisão inteira `//`

Retorna apenas a parte inteira da divisão.

```python
5 // 2
```

Resultado:

```text
2
```

A diferença entre `/` e `//` é destacada nos exemplos dos slides. 

---

## Resto da divisão `%`

O operador `%` retorna o **resto da divisão**.

```python
5 % 2
```

Resultado:

```text
1
```

Outro exemplo:

```python
4 % 2
```

Resultado:

```text
0
```

Isso é muito útil para descobrir, por exemplo, se um número é par.

---

## Potenciação `**`

```python
2 ** 4
```

Resultado:

```text
16
```

Ou seja:

```text
2 × 2 × 2 × 2 = 16
```



---

# 6. Ordem das operações

Python segue uma ordem para resolver expressões.

Por exemplo:

```python
8 + 10 * 6
```

Primeiro ocorre a multiplicação:

```text
10 * 6 = 60
```

Depois:

```text
8 + 60 = 68
```

Resultado:

```text
68
```

Os slides chamam essa ordem de **precedência dos operadores**. 

---

## Parênteses

Podemos usar parênteses para deixar explícita a ordem desejada.

```python
(8 + 10) * 6
```

Primeiro:

```text
8 + 10 = 18
```

Depois:

```text
18 * 6 = 108
```

✅ Quando houver expressões maiores, use parênteses para deixar o código mais fácil de entender. 

---

# 7. Exemplo completo 💻

Vamos criar um programa que recebe dois números e calcula algumas operações:

```python
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

Se o usuário digitar:

```text
10
2
```

Teremos:

```text
Soma: 12.0
Subtração: 8.0
Multiplicação: 20.0
Divisão: 5.0
```

---

# 📌 Resumo

```python
# Mostrar informação
print("Olá")

# Ler texto
nome = input("Nome: ")

# Ler inteiro
idade = int(input("Idade: "))

# Ler decimal
altura = float(input("Altura: "))

# Operações
a + b
a - b
a * b
a / b
a // b
a % b
a ** b
```

### Lembre-se

* `print()` → mostra informações;
* `input()` → recebe informações;
* `input()` retorna uma `string`;
* `int()` → inteiro;
* `float()` → decimal;
* `str()` → texto;
* Parênteses ajudam a controlar e deixar clara a ordem das operações.
