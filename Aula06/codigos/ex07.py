"""
Exercício 7 — Caixa eletrônico

Um caixa eletrônico entrega cédulas de R$ 100, 50, 20 e 10, sempre usando
a MENOR quantidade de cédulas possível. Crie as funções:

- valor_valido(valor): retorna True se o valor for positivo e múltiplo
  de 10; caso contrário, retorna False.
- calcula_cedulas(valor, cedulas=(100, 50, 20, 10)): retorna um
  DICIONÁRIO {cédula: quantidade} só com as cédulas usadas.
  O parâmetro cedulas é uma tupla com valor padrão.
- mostra_cedulas(resultado): mostra o dicionário de forma organizada
  (não retorna nada).

Na main(), leia valores de saque até o usuário digitar 0. Para cada valor
válido, mostre as cédulas do caixa normal e as de um caixa que só tem
notas de 50 e 10 (chame calcula_cedulas com argumento nomeado).

Dica: valor // cedula diz quantas cédulas cabem; valor % cedula é o que sobra.

Saída esperada:
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
"""


def main():
    valor = int(input("Valor do saque (0 para sair): "))
    while valor != 0:
        if valor_valido(valor):
            print("Caixa completo:")
            mostra_cedulas(calcula_cedulas(valor))

            print("Caixa só com 50 e 10:")
            mostra_cedulas(calcula_cedulas(valor, cedulas=(50, 10)))
        else:
            print("Valor inválido: use múltiplos de 10.")
        valor = int(input("Valor do saque (0 para sair): "))


def valor_valido(valor):
    return valor > 0 and valor % 10 == 0


def calcula_cedulas(valor, cedulas=(100, 50, 20, 10)):
    resultado = {}
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor = valor % cedula  # o que ainda falta entregar
    return resultado


def mostra_cedulas(resultado):
    for cedula, quantidade in resultado.items():
        print(f"  {quantidade} x R$ {cedula}")


if __name__ == "__main__":
    main()
