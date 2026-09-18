'''
Uma caixa suporta até 50 kg. Peça ao usuário o peso da caixa e
o peso que ele deseja adicionar. Faça um programa que verifique se
cabe dentro da caixa.
'''
 
def main():
    peso_caixa = float(input("Digite o peso da caixa: "))
    peso_adicional = float(input("Digite o peso que deseja adicionar: "))
    verifica = peso_caixa + peso_adicional <= 50.0
    print(f"Cabe dentro da caixa? {verifica}")
 
if __name__ == "__main__":
    main()
