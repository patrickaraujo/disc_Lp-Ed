"""
Exercício Tutoreado 2 — Caça-bugs: fechamento de vendas da semana

Uma loja abre de segunda a sexta (5 dias) e tem meta diária de R$ 500,00.
Um estagiário escreveu a função fechamento_com_bugs(vendas, meta), que
deveria:
  (1) calcular a venda MÉDIA por dia;
  (2) contar quantos dias ATINGIRAM a meta (venda >= meta).

O programa roda SEM mensagem de erro, mas o gerente estranhou o relatório:
a média informada é menor do que a venda de qualquer dia da semana.

Roteiro (como na prova!):
  a) Faça o TESTE DE MESA da versão com bugs e anote a saída exibida.
     Depois, calcule à mão qual deveria ser a saída correta.
  b) Encontre os DOIS erros de lógica e explique o efeito de cada um.
  c) Corrija o código (função fechamento) e justifique cada alteração.

Saída esperada ao rodar este arquivo:
    Vendas: [700.0, 480.0, 510.0, 300.0, 510.0]
    --- Versão com bugs ---
    Média por dia: R$ 100.00
    Dias que atingiram a meta: 1
    --- Versão corrigida ---
    Média por dia: R$ 500.00
    Dias que atingiram a meta: 3
"""


def fechamento_com_bugs(vendas, meta=500.0):
    total = 0
    dias_meta = 0
    for i in range(len(vendas)):
        total = total + vendas[i]
        if vendas[i] >= meta:
            dias_meta = dias_meta + 1
        return total / 7, dias_meta          # <- olhe com atenção esta linha


# ---------------------------------------------------------------------
# a) TESTE DE MESA da versão com bugs, vendas = [700, 480, 510, 300, 510]
#
#   i | vendas[i] | total | vendas[i] >= 500? | dias_meta | o que acontece
#   --+-----------+-------+-------------------+-----------+------------------
#   0 |   700.0   | 700.0 |       True        |     1     | return (700/7, 1)
#
#   O laço para na 1ª volta! Saída exibida: média 100.00 e 1 dia na meta.
#   Saída correta: total = 2500.0 -> média = 2500 / 5 = 500.00;
#                  dias na meta: 700, 510 e 510 -> 3.
#
# b) Os dois erros:
#   ERRO 1 — o return está INDENTADO dentro do for. O return encerra a
#            função imediatamente, então só o primeiro dia é processado.
#   ERRO 2 — a divisão é por 7 (dias da semana), mas a loja só abre 5 dias.
#            O certo é dividir pela quantidade de elementos: len(vendas).
#
#   Os erros são INDEPENDENTES:
#     - corrigindo só o ERRO 1: média = 2500 / 7 = 357.14 (ainda errada)
#     - corrigindo só o ERRO 2: média = 700 / 5 = 140.00 e 1 dia (ainda errado)
# ---------------------------------------------------------------------


# c) Versão corrigida
def fechamento(vendas, meta=500.0):
    total = 0
    dias_meta = 0
    for i in range(len(vendas)):
        total = total + vendas[i]
        if vendas[i] >= meta:
            dias_meta = dias_meta + 1
    # CORREÇÃO 1: return FORA do laço (mesmo nível de indentação do for),
    #             só depois de todos os dias terem sido somados.
    # CORREÇÃO 2: divide por len(vendas) -> funciona para qualquer
    #             quantidade de dias.
    return total / len(vendas), dias_meta


# ---------------------------------------------------------------------
# BÔNUS — erro de EXECUÇÃO x erro de LÓGICA
# Troque o for por este while e rode:
#
#     i = 0
#     while i <= len(vendas):       # <= em vez de <
#         total = total + vendas[i]
#         i = i + 1
#
# Agora aparece IndexError: list index out of range, porque o último
# índice válido é len(vendas) - 1. Erros de execução o Python mostra;
# erros de lógica (como os dois acima) só o teste de mesa encontra.
# ---------------------------------------------------------------------


def main():
    vendas = [700.0, 480.0, 510.0, 300.0, 510.0]
    print("Vendas:", vendas)

    print("--- Versão com bugs ---")
    media, dias = fechamento_com_bugs(vendas)
    print(f"Média por dia: R$ {media:.2f}")
    print("Dias que atingiram a meta:", dias)

    print("--- Versão corrigida ---")
    media, dias = fechamento(vendas)
    print(f"Média por dia: R$ {media:.2f}")
    print("Dias que atingiram a meta:", dias)


if __name__ == "__main__":
    main()
