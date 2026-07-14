# Disciplina de Lógica de Programação e Estruturas de Dados

Repositório destinado ao armazenamento de materiais, códigos-fonte e exercícios da disciplina de **Lógica de Programação e Estruturas de Dados**. O curso é focado na linguagem Python, partindo da construção do raciocínio lógico-algorítmico até a implementação de estruturas de dados clássicas (vetores, matrizes, listas encadeadas, pilhas, filas e árvores).

---

## 📂 Estrutura do Repositório

A organização das pastas segue o cronograma das aulas, facilitando a navegação pelos tópicos estudados:

```text
.
├── AVC/
├── Aula01/
├── Aula02/
├── Aula03/
├── Aula04/
├── Aula05/
├── Aula06/
├── Aula07/
├── Aula08/
├── Aula09/
├── Aula10/
├── Aula11/
├── Aula12/
├── Aula13/
├── Aula14/
├── Aula15/
└── README.md
```

---

## 📚 Ementa Detalhada

**Aula 01 - Fundamentos: Funcionamento do Computador e Noções de Algoritmo**

* Arquitetura básica do computador: processador, memória RAM, disco rígido, dispositivos de entrada e saída e softwares.
* Diferença entre linguagens de alto e baixo nível, e entre linguagens interpretadas e compiladas.
* Conceito de algoritmo como processo sistemático de resolução de problemas.
* Divisão de um algoritmo em entrada, processamento e saída.
* Algoritmos clássicos de raciocínio lógico (Torre de Hanói, travessia de rio, entre outros).

**Aula 02 - Representações de Algoritmos: Fluxograma, Blocos e Pseudo-linguagem**

* Descrição narrativa, fluxograma convencional e pseudocódigo (Portugol).
* Simbologia de fluxogramas: terminal, processamento, entrada/saída, decisão, conectores.
* Representação de algoritmos por meio de blocos estruturados.
* Tradução de um problema em diferentes formas de representação.
* Exercícios de elaboração de algoritmos descritivos antes da escrita em Python.

**Aula 03 - Constantes, Bases Numéricas e Representação Binária**

* Constantes e seu uso em algoritmos.
* Sistemas de numeração: decimal, binário e hexadecimal.
* Conversão de valores entre bases numéricas em Python (`bin`, `hex`, `int(x, base)`).
* Representação de números binários e complemento de dois.
* Aplicação prática de conversões com funções nativas da linguagem.

**Aula 04 - Variáveis, Atribuição, Operadores, Entrada e Saída**

* Conceito de variável como referência a um objeto na memória e regras de nomenclatura.
* Tipagem dinâmica em Python e inferência automática de tipos.
* Operadores aritméticos, de concatenação (`+`) e de repetição (`*`) em strings.
* Comandos de entrada (`input`) e saída (`print`), com conversão de tipos (`int`, `float`).
* Construção dos primeiros programas completos em Python.

**Aula 05 - Programas Sequenciais e Lógica para Programação**

* Estrutura de um programa sequencial: entrada, processamento e saída.
* Operadores relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`) e o tipo booleano.
* Operadores lógicos (`and`, `or`, `not`) e tabelas-verdade.
* Precedência de operadores em expressões lógicas e aritméticas.
* Exercícios de fixação com programas sequenciais simples.

**Aula 06 - Comandos de Decisão: Simples, Múltipla e por Variável de Controle**

* Estrutura condicional simples (`if`) e composta (`if/else`).
* Encadeamento de condições com `elif` (decisão múltipla).
* Seleção de fluxo por variável de controle: dicionários como alternativa ao `switch` e a estrutura `match/case`.
* Boas práticas de indentação e legibilidade do código Python.
* Exercícios de classificação e validação de dados de entrada.

**Aula 07 - Comandos de Repetição: Teste no Início e Teste no Final**

* Estrutura de repetição `while` (teste no início) e cuidados com laços infinitos.
* Simulação de teste no final (`do/while`) em Python com `while True` e `break`.
* Uso do `for` associado a `range()` como repetição com variável de controle.
* Comparação entre `while`, `for` e a simulação de `do/while`.
* Exercícios de validação de entrada com repetição garantida.

**Aula 08 - Vetores e Matrizes**

* Listas em Python como estrutura equivalente a vetores.
* Declaração, indexação, fatiamento (*slicing*) e percurso de listas.
* Matrizes representadas por listas de listas (linhas e colunas).
* Operações básicas com matrizes e introdução à biblioteca `numpy`.
* Exercícios de busca, contagem e manipulação de listas.

**Aula 09 - Repetições Encaixadas**

* Conceito de laços aninhados (*loops* dentro de *loops*).
* Aplicações em geração de padrões, tabelas e percurso de matrizes.
* Controle de múltiplas variáveis de controle simultâneas.
* Complexidade e desempenho de repetições encaixadas.
* Exercícios práticos: tabuadas e manipulação de matrizes bidimensionais.

**Aula 10 - Funções e Procedimentos; Passagem de Parâmetros**

* Conceito de modularização e reaproveitamento de código com `def`.
* Funções com e sem retorno (`return` versus `print`).
* Parâmetros posicionais, nomeados, valores *default* e passagem por referência a objetos.
* Escopo de variáveis locais e globais (`global`).
* Criação e importação de bibliotecas (módulos) próprias.

**Aula 11 - Recursão**

* Conceito de recursividade e condição de parada (caso-base).
* Comparação entre soluções recursivas e iterativas.
* Exemplos clássicos: fatorial, soma de lista, Fibonacci.
* Pilha de chamadas em Python e limite de recursão (`sys.setrecursionlimit`).
* Vantagens, riscos e boas práticas no uso de funções recursivas.

**Aula 12 - Alocação Estática e Dinâmica de Memória**

* Diferença conceitual entre alocação estática e dinâmica de memória.
* Objetos mutáveis e imutáveis (listas, tuplas, strings, dicionários).
* Referências a objetos: função `id()`, operador `is` e efeitos colaterais em funções.
* Cópia rasa (*shallow copy*) versus cópia profunda (*deep copy*).
* Como o Python gerencia memória automaticamente (contagem de referências e *garbage collector*), como preparação conceitual para as estruturas encadeadas via classes e objetos.

**Aula 13 - Listas Lineares: Simples, Duplamente Ligadas e Circulares**

* Conceito de lista encadeada e representação de nó com classes (`self.dado`, `self.proximo`).
* Implementação de lista simplesmente ligada: inserção, remoção e percurso.
* Listas duplamente ligadas e navegação bidirecional.
* Listas circulares e suas aplicações.
* Comparação entre listas encadeadas (classes) e listas nativas do Python.

**Aula 14 - Pilhas, Filas e Deques**

* Pilha (LIFO): operações de empilhar e desempilhar usando listas.
* Fila (FIFO): operações de enfileirar e desenfileirar.
* Deque: inserção e remoção em ambas as extremidades com `collections.deque`.
* Implementação dessas estruturas também por meio de classes e listas encadeadas.
* Aplicações práticas: avaliação de expressões, filas de atendimento e buffers.

**Aula 15 - Árvores: Binárias, de Busca e Balanceamento**

* Conceito de árvore, nós, raiz e folhas; representação por classes em Python.
* Árvores binárias de busca (ABB): inserção, remoção e busca.
* Percursos em árvore: pré-ordem, em ordem e pós-ordem.
* Balanceamento de árvores binárias e rotações (simples e duplas).
* Aplicações práticas de árvores e noções do algoritmo de Dijkstra.

---

## 📖 Referências Bibliográficas

**Referência Básica:**
BACKES, André. *Linguagem C: completa e descomplicada*. Rio de Janeiro: Elsevier, 2018.

**Referência Complementar:**
BACKES, André Ricardo. *Algoritmos e Estruturas de Dados em Linguagem C*. Rio de Janeiro: LTC - Livros Técnicos e Científicos Editora, 2022.

**Bibliografia Básica:**
EDELWEISS, Nina, LIVI, Maria Castro. *Algoritmos e Programação com Exemplos em Pascal e C*. Bookman, 01/2014.

MANZANO, José Augusto G., LOURENÇO, André Evandro, MATOS, Ecivaldo. *Algoritmos - Técnicas de Programação*, 2nd edição. Érica, 06/2016.

PERKOVIC, Ljubomir. *Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações*. LTC, 04/2016.

**Bibliografia Complementar:**
MANZANO, José Augusto G., OLIVEIRA, Jayr de. *Algoritmos - Lógica para Desenvolvimento de Programação de Computadores*, 28th edição. Érica, 06/2016.

SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. Bookman, 08/2011.

SOFFNER, Renato. *Algoritmos e Programação em Linguagem C*, 1ª edição. Saraiva, 08/2013.

TOSCANI, Laira Vieira, VELOSO, Paulo S. *Complexidade de Algoritmos - V13 - UFRGS*. Bookman, 01/2012.

TUCKER, Allen, Noonan, Robert. *Linguagens de Programação*, 2nd edição. AMGH, 01/01/2009.
