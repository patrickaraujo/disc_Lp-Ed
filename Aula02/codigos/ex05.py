'''
Peça a nota da prova e a frequência (%) de um aluno. Verifique se a
nota é maior ou igual a 6 e a frequência maior ou igual a 75.
'''
 
def main():
    nota = float(input("Digite sua nota: "))
    freq = float(input("Digite sua frequência: "))
    verifica = nota >= 6 and freq >= 75
    print(f"Aluno aprovado? {verifica}")
 
if __name__ == "__main__":
    main()
