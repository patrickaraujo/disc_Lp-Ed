"""
Exercício 6 — Funções numéricas

Crie as funções abaixo. Todas devem RETORNAR o resultado (não usar
print dentro delas). Considere apenas números inteiros positivos.

- reverso(n): retorna o número ao contrário. Ex.: 127 -> 721.
- quantidade_digitos(n): retorna quantos dígitos o número tem. Ex.: 2026 -> 4.
- potencia(a, b=2): retorna a elevado a b SEM usar o operador **.
  Se b não for informado, calcula o quadrado.

Na main(), leia um número n e mostre o reverso e a quantidade de dígitos.
Depois, leia a e b e mostre potencia(a, b) e potencia(a).

Dica: n % 10 devolve o último dígito de n, e n // 10 remove o último dígito.

Saída esperada:
    Digite um número inteiro positivo: 127
    Reverso: 721
    Quantidade de dígitos: 3
    Base: 3
    Expoente: 4
    3 elevado a 4 = 81
    3 ao quadrado = 9
"""


def main():
    n = int(input("Digite um número inteiro positivo: "))
    print("Reverso:", reverso(n))
    print("Quantidade de dígitos:", quantidade_digitos(n))

    a = int(input("Base: "))
    b = int(input("Expoente: "))
    print(f"{a} elevado a {b} = {potencia(a, b)}")
    print(f"{a} ao quadrado = {potencia(a)}")  # usa o valor padrão b=2


def reverso(n):
    invertido = 0
    while n > 0:
        ultimo = n % 10                     # pega o último dígito
        invertido = invertido * 10 + ultimo  # "empurra" para a esquerda e soma
        n = n // 10                         # descarta o último dígito
    return invertido


def quantidade_digitos(n):
    if n == 0:
        return 1
    contador = 0
    while n > 0:
        n = n // 10
        contador += 1
    return contador


def potencia(a, b=2):
    resultado = 1
    for i in range(b):
        resultado = resultado * a
    return resultado


if __name__ == "__main__":
    main()
