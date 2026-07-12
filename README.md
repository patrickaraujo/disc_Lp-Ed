# Disciplina de Lógica de Programação e Estruturas de Dados

Repositório destinado ao armazenamento de materiais, códigos-fonte e exercícios da disciplina de **Lógica de Programação e Estruturas de Dados**. O curso parte da construção do raciocínio lógico-algorítmico até a implementação de estruturas de dados clássicas (listas, pilhas, filas e árvores), utilizando a linguagem C como principal ferramenta de codificação.

---

## 📂 Estrutura do Repositório

A organização das pastas segue o cronograma das aulas, facilitando a navegação pelos tópicos estudados:

```text
.
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
├── Aula16/
├── Aula17/
└── README.md
```

---

## 📚 Ementa Detalhada

**Aula 01 - Fundamentos: Funcionamento do Computador e Noções de Algoritmo**

* Arquitetura básica do computador: processador, memória RAM, disco rígido, dispositivos de entrada e saída.
* Papel dos softwares e diferença entre linguagens de alto e baixo nível.
* Conceito de algoritmo como processo sistemático de resolução de problemas.
* Divisão de um algoritmo em entrada, processamento e saída.
* Algoritmos clássicos de raciocínio lógico (Torre de Hanói, travessia de rio, entre outros).

**Aula 02 - Representações de Algoritmos: Fluxograma, Blocos e Pseudo-linguagem**

* Descrição narrativa, fluxograma convencional e pseudocódigo (Portugol).
* Simbologia de fluxogramas: terminal, processamento, entrada/saída, decisão, conectores.
* Representação de algoritmos por meio de blocos estruturados.
* Tradução de um problema em diferentes formas de representação.
* Exercícios de elaboração de algoritmos descritivos.

**Aula 03 - Constantes, Bases Numéricas e Representação Binária**

* Constantes e seu uso em algoritmos.
* Sistemas de numeração: decimal, binário e hexadecimal.
* Conversão de valores entre bases numéricas.
* Representação de números binários e complemento para dois.
* Aplicação prática de conversões em linguagem C.

**Aula 04 - Variáveis, Atribuição, Operadores, Entrada e Saída**

* Conceito de variável como região de memória e regras de nomenclatura.
* Tipagem de variáveis e operador de atribuição.
* Operadores aritméticos, de concatenação e de comparação.
* Comandos de entrada (`scanf`) e saída (`printf`) de dados.
* Construção dos primeiros programas completos.

**Aula 05 - Programas Sequenciais e Lógica para Programação**

* Estrutura de um programa sequencial: entrada, processamento e saída.
* Operadores relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`).
* Operadores lógicos (E, OU, NÃO) e tabelas-verdade.
* Precedência de operadores em expressões lógicas e aritméticas.
* Exercícios de fixação com programas sequenciais simples.

**Aula 06 - Comandos de Decisão**

* Estrutura condicional simples (`if`) e composta (`if/else`).
* Construção de fluxos de decisão binária.
* Boas práticas de indentação e legibilidade do código.
* Erros comuns na escrita de condicionais.
* Exercícios de classificação e validação de dados de entrada.

**Aula 07 - Decisão Múltipla e Decisão com Variável de Controle**

* Encadeamento de condições (`else if`).
* Estrutura de múltipla escolha (`switch/case`).
* Uso de variável de controle para seleção de fluxo.
* Comparação entre decisão encadeada e decisão múltipla.
* Estudo de caso: sistemas de classificação por faixas de valores.

**Aula 08 - Comandos de Repetição: Teste no Início**

* Estrutura de repetição `while`.
* Condição de parada e controle de variáveis de laço.
* Cuidados com laços infinitos.
* Situações de uso: repetição condicionada por evento de entrada.
* Exercícios práticos de contadores e acumuladores.

**Aula 09 - Comandos de Repetição: Teste no Final**

* Estrutura de repetição `do/while`.
* Diferença entre teste no início e teste no final do laço.
* Uso do `for` como estrutura de repetição com variável de controle.
* Comparação entre `while`, `do/while` e `for`.
* Exercícios de validação de entrada com repetição garantida.

**Aula 10 - Repetições Encaixadas**

* Conceito de laços aninhados (loops dentro de loops).
* Aplicações em geração de padrões e tabelas.
* Controle de múltiplas variáveis de controle simultâneas.
* Complexidade e desempenho de repetições encaixadas.
* Exercícios práticos: matrizes de caracteres e tabuadas.

**Aula 11 - Vetores e Matrizes**

* Conceito de variável composta homogênea (vetor).
* Declaração, inicialização e percurso de vetores.
* Matrizes como estruturas bidimensionais (linhas e colunas).
* Operações básicas com matrizes.
* Exercícios de busca, ordenação simples e manipulação de vetores.

**Aula 12 - Funções e Procedimentos; Passagem de Parâmetros**

* Conceito de modularização e reaproveitamento de código.
* Declaração de funções com e sem retorno.
* Passagem de parâmetros por valor e por referência.
* Escopo de variáveis locais e globais.
* Boas práticas de organização de código em funções.

**Aula 13 - Recursão**

* Conceito de recursividade e condição de parada (caso-base).
* Comparação entre soluções recursivas e iterativas.
* Exemplos clássicos: fatorial, soma de vetor, Fibonacci.
* Pilha de chamadas e uso de memória em recursão.
* Vantagens, riscos e boas práticas no uso de funções recursivas.

**Aula 14 - Alocação Estática e Dinâmica de Memória**

* Diferença entre alocação estática e dinâmica.
* Ponteiros: declaração, operadores de endereço e de indireção.
* Alocação dinâmica com `malloc`, `calloc`, `realloc` e `free`.
* Vazamentos de memória e boas práticas de liberação.
* Relação entre ponteiros e estruturas de dados dinâmicas.

**Aula 15 - Listas Lineares: Simples, Duplamente Ligadas e Circulares**

* Conceito de lista encadeada e estrutura de nó (dado + ponteiro).
* Implementação de lista simplesmente ligada: inserção, remoção e percurso.
* Listas duplamente ligadas e navegação bidirecional.
* Listas circulares e suas aplicações.
* Comparação entre listas encadeadas e vetores.

**Aula 16 - Pilhas, Filas e Deques**

* Pilha (LIFO): operações de `push` e `pop`.
* Fila (FIFO): operações de enfileirar e desenfileirar.
* Deque: inserção e remoção em ambas as extremidades.
* Implementação dessas estruturas com vetores e com listas encadeadas.
* Aplicações práticas: avaliação de expressões, filas de atendimento e buffers.

**Aula 17 - Árvores: Binárias, de Busca e Balanceamento**

* Conceito de árvore, nós, raiz e folhas.
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
