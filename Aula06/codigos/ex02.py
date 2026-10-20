"""
Exercício 2 — Temperaturas da semana

Os dias da semana nunca mudam, então guarde-os em uma TUPLA:
    dias = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")

Leia a temperatura (em °C) de cada dia, guardando-as em uma LISTA.
Em seguida, mostre:
- a lista de temperaturas;
- a temperatura média da semana;
- a maior e a menor temperatura, e em que dia cada uma ocorreu;
- quantos dias tiveram temperatura acima de 30°C.

Não use as funções prontas sum(), max() e min(): percorra a lista com um laço.

Saída esperada:
    Temperatura de Dom: 28
    Temperatura de Seg: 31
    Temperatura de Ter: 33
    Temperatura de Qua: 22
    Temperatura de Qui: 19
    Temperatura de Sex: 30
    Temperatura de Sáb: 25
    Temperaturas: [28.0, 31.0, 33.0, 22.0, 19.0, 30.0, 25.0]
    Média: 26.9°C
    Maior: 33.0°C (Ter)
    Menor: 19.0°C (Qui)
    Dias acima de 30°C: 2
"""


def main():
    dias = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")

    # Leitura: um valor para cada dia da tupla
    temperaturas = []
    for dia in dias:
        t = float(input(f"Temperatura de {dia}: "))
        temperaturas.append(t)

    print("Temperaturas:", temperaturas)

    # Guardamos o ÍNDICE da maior e da menor: ele serve para as duas
    # estruturas (temperaturas[i] e dias[i]).
    soma = 0
    i_maior = 0
    i_menor = 0
    dias_calor = 0

    for i in range(len(temperaturas)):
        soma += temperaturas[i]
        if temperaturas[i] > temperaturas[i_maior]:
            i_maior = i
        if temperaturas[i] < temperaturas[i_menor]:
            i_menor = i
        if temperaturas[i] > 30:
            dias_calor += 1

    media = soma / len(temperaturas)

    print(f"Média: {format(media, '.1f')}°C")
    print(f"Maior: {temperaturas[i_maior]}°C ({dias[i_maior]})")
    print(f"Menor: {temperaturas[i_menor]}°C ({dias[i_menor]})")
    print("Dias acima de 30°C:", dias_calor)


if __name__ == "__main__":
    main()
