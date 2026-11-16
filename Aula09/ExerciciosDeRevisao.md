# Lista de Exercícios — Revisão 1 (prática)

> Revisão para as provas: tipos e conversão, operadores `//` e `%`, `if-elif-else`, `while`, `for`, `break`/`continue`, listas, funções e escopo.  
> Os exercícios tutoreados (`exTutoreado01.py` e `exTutoreado02.py`) estão na pasta `codigos`.
>
> 🧠 **Dica de prova:** antes de rodar qualquer código, faça o **teste de mesa**: anote, volta a volta, o valor de cada variável. É assim que se encontram os erros de lógica que o Python **não** mostra.

## Exercício 1 — Tempo de viagem

Leia a distância de uma viagem (em km) e a velocidade média do ônibus (em km/h). Calcule o tempo total de viagem em **minutos** (número inteiro) e mostre-o no formato `X h Y min`, usando os operadores `//` e `%`.

Mostre também o **tipo** do dado lido antes e depois da conversão com `float()`. Se a viagem durar mais de 4 horas, avise que haverá uma parada obrigatória.

> 💡 Dica: `type(x)` mostra o tipo de um objeto. Lembre que `input()` sempre devolve uma `str`.

### Exemplo de execução

```text
Distância (km): 245
Velocidade média (km/h): 70
Tipo lido: <class 'str'> | tipo convertido: <class 'float'>
Tempo total: 210 minutos
Duração: 3 h 30 min
Viagem sem parada obrigatória.
```

---

## Exercício 2 — Desconto progressivo

Uma loja dá desconto de acordo com o valor da compra:

| Valor da compra        | Desconto |
|------------------------|----------|
| a partir de R$ 1000,00 | 15%      |
| a partir de R$ 500,00  | 10%      |
| a partir de R$ 200,00  | 5%       |
| abaixo de R$ 200,00    | 0%       |

Clientes com cartão fidelidade ganham **mais 5 pontos percentuais**, mas **somente** se a compra for de pelo menos R$ 200,00.

Leia o valor da compra e se o cliente tem cartão (`s`/`n`). Mostre o percentual de desconto, o valor do desconto e o valor final.

> ❓ Responda em um comentário no código: o que aconteceria se o teste `valor >= 200` fosse o **primeiro** do `if-elif`? Teste com R$ 1500,00.

### Exemplo de execução

```text
Valor da compra: 650
Tem cartão fidelidade (s/n)? s
Desconto: 15%
Valor do desconto: R$ 97.50
Valor final: R$ 552.50
```

---

## Exercício 3 — Cofre com senha

A senha de um cofre é `"lped2026"`. O usuário tem no máximo **3 tentativas**.

* Se digitar a senha certa, mostre `Cofre aberto!` e encerre o laço com `break`.
* Se apertar Enter sem digitar nada, mostre `Senha vazia, tente de novo.`. Essa tentativa **não conta** (use `continue`).
* Se errar, mostre quantas tentativas restam.
* Se as 3 tentativas acabarem, mostre `Cofre bloqueado!`.

### Exemplos de execução

```text
Senha: abc
Senha incorreta. Restam 2 tentativa(s).
Senha:
Senha vazia, tente de novo.
Senha: lped2026
Cofre aberto!
```

```text
Senha: 1234
Senha incorreta. Restam 2 tentativa(s).
Senha: senha
Senha incorreta. Restam 1 tentativa(s).
Senha: lped
Senha incorreta. Restam 0 tentativa(s).
Cofre bloqueado!
```

---

## Exercício 4 — Leituras de um sensor de umidade

Um sensor registra a umidade do ar (%) a cada hora. Quando ele falha, grava o valor `-1`. As leituras do dia foram:

```python
leituras = [62, 65, -1, 71, 80, -1, 77, 68]
```

Crie as funções:

| Função                          | O que devolve                                                          |
|---------------------------------|------------------------------------------------------------------------|
| `limpar(leituras)`              | uma **nova** lista sem os `-1` (a lista original não pode mudar)        |
| `media(lista)`                  | a média dos valores                                                     |
| `posicao_pico(lista)`           | o **índice** do maior valor                                             |
| `contar_acima(lista, limite=70)`| quantos valores são maiores que o limite (valor padrão: 70)             |

Na `main()`, mostre as leituras originais e as válidas, quantas falhas ocorreram, a média, o pico e sua posição, e quantas leituras ficaram acima de 70 (limite padrão) e acima de 75 (argumento nomeado).

> ⚠️ Não use `sum()`, `max()`, `min()` nem `remove()`: percorra a lista com um laço.

### Exemplo de execução

```text
Originais: [62, 65, -1, 71, 80, -1, 77, 68]
Válidas: [62, 65, 71, 80, 77, 68]
Falhas do sensor: 2
Média: 70.5%
Pico: 80% (posição 3 da lista de válidas)
Acima de 70%: 3
Acima de 75%: 2
```

---

## Exercício 5 — Preveja antes de rodar

Para cada trecho, **escreva a saída antes de executar**. Depois, copie o código, rode e confira. Para cada previsão errada, explique o que você não tinha considerado.

**Trecho 1 — escopo de variáveis**

```python
total = 100

def bonus():
    total = 10
    total = total + 5
    return total

r = bonus()
print("Trecho 1:", total, r)
```

**Trecho 2 — lista passada para uma função**

```python
def registrar(lista):
    lista.append(0)
    lista = [1, 1]
    lista.append(2)

nums = [5, 6]
registrar(nums)
print("Trecho 2:", nums)
```

**Trecho 3 — valor padrão e argumentos nomeados**

```python
def preco(valor, taxa=0.1, desconto=0):
    return valor + valor * taxa - desconto

print("Trecho 3:", preco(100), preco(100, desconto=20), preco(100, 0.5))
```

**Trecho 4 — `range` decrescente, `continue` e `break`**

```python
saida = ""
for n in range(10, 0, -3):
    if n % 2 == 0:
        continue
    if n < 3:
        break
    saida = saida + str(n) + " "
print("Trecho 4:", saida)
```

**Trecho 5 — `while` com `//` e `%`**

```python
n = 3407
soma = 0
while n > 0:
    soma = soma + n % 10
    n = n // 10
print("Trecho 5:", soma)
```
