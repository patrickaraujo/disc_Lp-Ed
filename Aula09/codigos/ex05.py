"""
Exercício 5 — Preveja antes de rodar

Para cada trecho abaixo, ESCREVA no caderno (ou em um comentário) qual
será a saída ANTES de executar. Depois, rode o arquivo e confira.
Para cada previsão errada, explique o que você não tinha considerado.

Trecho 1 — escopo de variáveis (local x global)
Trecho 2 — lista passada para uma função
Trecho 3 — parâmetros com valor padrão e argumentos nomeados
Trecho 4 — range decrescente, continue e break
Trecho 5 — while com // e %

Saída esperada: veja o gabarito comentado ao lado de cada print.
"""

# ---------------- Trecho 1 ----------------
total = 100


def bonus():
    total = 10            # cria uma variável LOCAL (não mexe na global)
    total = total + 5
    return total


r = bonus()
print("Trecho 1:", total, r)        # 100 15


# ---------------- Trecho 2 ----------------
def registrar(lista):
    lista.append(0)       # modifica a lista ORIGINAL (mesma lista)
    lista = [1, 1]        # agora 'lista' aponta para uma lista NOVA
    lista.append(2)       # só a lista nova muda


nums = [5, 6]
registrar(nums)
print("Trecho 2:", nums)            # [5, 6, 0]


# ---------------- Trecho 3 ----------------
def preco(valor, taxa=0.1, desconto=0):
    return valor + valor * taxa - desconto


print("Trecho 3:", preco(100), preco(100, desconto=20), preco(100, 0.5))
# 110.0 90.0 150.0  -> no 3º, 0.5 vai para 'taxa' (2º parâmetro pela posição)


# ---------------- Trecho 4 ----------------
saida = ""
for n in range(10, 0, -3):          # 10, 7, 4, 1  (o 0 não entra)
    if n % 2 == 0:
        continue                    # pula os pares: 10 e 4
    if n < 3:
        break                       # n = 1 encerra o laço
    saida = saida + str(n) + " "
print("Trecho 4:", saida)           # 7


# ---------------- Trecho 5 ----------------
n = 3407
soma = 0
while n > 0:
    soma = soma + n % 10            # último dígito
    n = n // 10                     # remove o último dígito
print("Trecho 5:", soma)            # 3 + 4 + 0 + 7 = 14
