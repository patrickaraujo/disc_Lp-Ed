"""
Exercício Tutoreado 2 — Catálogo de livros: ordenar e depois buscar

Uma biblioteca guarda os livros como uma lista de tuplas (título, ano).
Faça um programa que:

  a) Ordene a lista pelo ANO, do mais antigo para o mais novo, usando o
     Insertion Sort (sem usar sort() nem sorted()). Mostre os anos depois
     de cada passada, para acompanhar o algoritmo.
  b) Implemente buscaBinaria(lista, ano), que devolve o índice do livro
     daquele ano ou -1 se não houver. A cada passo, mostre inicio, fim e
     meio, como num teste de mesa.
  c) Busque os anos 1938 e 1950.

Saída esperada:
    Anos originais: [1899, 1937, 1890, 1938, 1865, 1928, 1977]
    Passada 1: [1899, 1937, 1890, 1938, 1865, 1928, 1977]
    Passada 2: [1890, 1899, 1937, 1938, 1865, 1928, 1977]
    Passada 3: [1890, 1899, 1937, 1938, 1865, 1928, 1977]
    Passada 4: [1865, 1890, 1899, 1937, 1938, 1928, 1977]
    Passada 5: [1865, 1890, 1899, 1928, 1937, 1938, 1977]
    Passada 6: [1865, 1890, 1899, 1928, 1937, 1938, 1977]
    --- Buscando 1938 ---
      inicio=0 fim=6 meio=3 -> ano 1928
      inicio=4 fim=6 meio=5 -> ano 1938
    Encontrado: Vidas Secas (posição 5)
    --- Buscando 1950 ---
      inicio=0 fim=6 meio=3 -> ano 1928
      inicio=4 fim=6 meio=5 -> ano 1938
      inicio=6 fim=6 meio=6 -> ano 1977
    Nenhum livro de 1950.
"""


def anos(lista):
    # Lista auxiliar só com os anos, para exibir o andamento
    resultado = []
    for titulo, ano in lista:
        resultado.append(ano)
    return resultado


def insertionSort(lista):
    # Ideia: a parte da esquerda (até i-1) já está ordenada.
    # Pegamos o elemento i e o "inserimos" no lugar certo dessa parte,
    # empurrando para a direita quem for maior que ele.
    for i in range(1, len(lista)):
        atual = lista[i]                 # a tupla que vamos inserir
        j = i - 1
        # Comparamos pelo ANO: posição [1] da tupla
        while j >= 0 and lista[j][1] > atual[1]:
            lista[j + 1] = lista[j]      # empurra para a direita
            j = j - 1
        lista[j + 1] = atual             # encaixa na posição livre
        print(f"Passada {i}:", anos(lista))


def buscaBinaria(lista, ano):
    # PRÉ-CONDIÇÃO: a lista precisa estar ordenada pelo ano.
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2       # // -> índice inteiro
        print(f"  inicio={inicio} fim={fim} meio={meio} -> ano {lista[meio][1]}")
        if lista[meio][1] == ano:
            return meio
        elif lista[meio][1] > ano:
            fim = meio - 1               # descarta a metade da direita
        else:
            inicio = meio + 1            # descarta a metade da esquerda
    return -1


def main():
    livros = [
        ("Dom Casmurro", 1899),
        ("Capitães da Areia", 1937),
        ("O Cortiço", 1890),
        ("Vidas Secas", 1938),
        ("Iracema", 1865),
        ("Macunaíma", 1928),
        ("A Hora da Estrela", 1977),
    ]
    print("Anos originais:", anos(livros))
    insertionSort(livros)

    for procurado in [1938, 1950]:
        print(f"--- Buscando {procurado} ---")
        pos = buscaBinaria(livros, procurado)
        if pos != -1:
            print(f"Encontrado: {livros[pos][0]} (posição {pos})")
        else:
            print(f"Nenhum livro de {procurado}.")

    # Para pensar: a busca sequencial olharia até 7 livros para concluir
    # que 1950 não existe. A binária olhou 3. Com 1000 livros, seriam
    # até 1000 contra cerca de 10.


if __name__ == "__main__":
    main()
