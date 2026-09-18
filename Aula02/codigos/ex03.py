'''
Uma farmácia tem 100 unidades de um remédio. O usuário informa a
quantidade vendida. O programa calcula o estoque final. Mostre se o
estoque final é menor que 20.
'''
 
def main():
    quantidade_vendida = int(input("Quantos remédios foram vendidos? "))
    estoque_final = 100 - quantidade_vendida
    verifica = estoque_final < 20
    print(f"Estoque baixo? {verifica}")
 
if __name__ == "__main__":
    main()
