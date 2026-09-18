# Este algoritmo simula um "detector de grito": ele analisa se a frase digitada
# pelo usuário foi escrita inteiramente em letras maiúsculas (como um grito) e,
# em caso positivo, reage de forma bem-humorada, convertendo o texto para minúsculas.
# Caso contrário, ele "provoca" o usuário mostrando como a frase ficaria se fosse gritada.
# A função é dividida em duas partes: a primeira usa apenas if/else, e a segunda
# usa um if aninhado para verificar também se a frase termina com ponto de exclamação.
 
def main():
    print("--- Parte 1: só if e else ---")
    frase1 = input("Digite uma frase (do jeito que quiser): ")
 
    if frase1.isupper():
        print("😱 CALMA! Por que você está GRITANDO?")
        print("Deixa eu traduzir num tom mais educado:")
        print(frase1.lower())
    else:
        print("Que educado(a) você é! 😊")
        print("Mas imagina se você tivesse GRITADO isso:")
        print(frase1.upper())
 
    print("\n--- Parte 2: if aninhado ---")
    frase2 = input("Digite outra frase (agora vamos analisar mais a fundo): ")
 
    if frase2.isupper():
        print("😱 CALMA! Por que você está GRITANDO?")
 
        if frase2.strip().endswith("!"):
            print("E ainda por cima com PONTO DE EXCLAMAÇÃO?! Você está MUITO bravo(a) hoje.")
        else:
            print("Pelo menos não usou exclamação... já é alguma coisa.")
 
        print("Deixa eu traduzir num tom mais educado:")
        print(frase2.lower())
    else:
        print("Que educado(a) você é! 😊")
        print("Mas imagina se você tivesse GRITADO isso:")
        print(frase2.upper())
 
 
if __name__ == "__main__":
    main()
