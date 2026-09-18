'''
A velocidade máxima é 80 km/h. Peça a velocidade do carro e verifique
se a velocidade está acima de 80 km/h.
'''
 
def main():
    km = float(input("Qual a velocidade? "))
    multa = km > 80
    print(f"O carro foi multado? {multa}")
 
if __name__ == "__main__":
    main()
