'''
    Exercício Tutoreado 1:
    Peça ao usuário a temperatura atual. Verifique se a temperatura
    está entre 20 e 25 graus.
'''
 
def main():
    temp = float(input("Digite a temperatura: "))
    #   verifica = temp >= 20 and temp <= 25
    verifica = 20 <= temp <=25
    print(f"A temperatura está agradável? {verifica}")
  
if __name__ == "__main__":
  main()
