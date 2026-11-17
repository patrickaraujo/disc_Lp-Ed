"""
Exercício 1 — Tempo de viagem

Leia a distância de uma viagem (em km) e a velocidade média do ônibus
(em km/h). Calcule o tempo total de viagem em MINUTOS (número inteiro) e
mostre-o no formato "X h Y min", usando os operadores // e %.

Mostre também o tipo do dado lido ANTES e DEPOIS da conversão com float().
Se a viagem durar mais de 4 horas, avise que haverá uma parada obrigatória.

Saída esperada:
    Distância (km): 245
    Velocidade média (km/h): 70
    Tipo lido: <class 'str'> | tipo convertido: <class 'float'>
    Tempo total: 210 minutos
    Duração: 3 h 30 min
    Viagem sem parada obrigatória.
"""


def main():
    texto = input("Distância (km): ")       # input() devolve str
    distancia = float(texto)                # conversão para float
    velocidade = float(input("Velocidade média (km/h): "))

    print("Tipo lido:", type(texto), "| tipo convertido:", type(distancia))

    # tempo em horas = distância / velocidade -> em minutos, * 60
    # int() descarta a parte decimal (os segundos)
    minutos_totais = int(distancia / velocidade * 60)

    horas = minutos_totais // 60     # divisão inteira: quantas horas cheias
    minutos = minutos_totais % 60    # resto: os minutos que sobram

    print("Tempo total:", minutos_totais, "minutos")
    print(f"Duração: {horas} h {minutos} min")

    # "mais de 4 horas" = mais de 240 minutos
    if minutos_totais > 240:
        print("Atenção: haverá uma parada obrigatória.")
    else:
        print("Viagem sem parada obrigatória.")


if __name__ == "__main__":
    main()
