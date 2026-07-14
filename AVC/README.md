## 📝 **Trabalho Prático - Aplicação de Estruturas de Dados a um Cenário Real**

### **Objetivo**
Cada grupo deve desenvolver, em Python, um sistema que aplique os conceitos de lógica de programação e estruturas de dados estudados durante o curso a um **cenário sorteado** entre os disponíveis abaixo.

---

### **Formato da Avaliação**
- A AVC é o **único** instrumento avaliativo desta etapa, não havendo entregas intermediárias ao longo do semestre.
- Aplicada na **última semana de aula**, com apresentação obrigatória do grupo (código funcionando + explicação das estruturas utilizadas).
- Trabalho em **grupo**, de **3 a 5 integrantes** (ajustável pelo docente conforme o tamanho da turma).
- Todos os integrantes devem ser capazes de explicar qualquer parte do código durante a apresentação — a nota é do grupo, mas perguntas individuais podem ajustar a nota de cada membro.

### **Como funciona o sorteio**
- Cada grupo sorteia **um único cenário** da lista da seção seguinte (sugestão: papeletas numeradas, ou sorteio público em sala em uma aula com antecedência mínima de 3-4 semanas da AVC).
- Não é permitido trocar de cenário após o sorteio.
- Se o número de grupos for maior que o número de cenários, o docente pode repetir cenários entre grupos diferentes (bom para comparar soluções distintas para o mesmo problema) ou incluir cenários adicionais seguindo o mesmo padrão desta lista.
- Os **requisitos técnicos** (próxima seção) são os mesmos para todos os cenários — o que muda é o domínio/contexto que cada grupo deve modelar.

---

### **Requisitos Mínimos Comuns (fundamentos, valem para qualquer cenário sorteado)**

Todo sistema, independentemente do cenário e da estrutura de dados escolhida, deve conter:

- **Lógica e algoritmo (Aulas 01-02):** fluxograma do fluxo principal do sistema, entregue junto ao código e coerente com o que foi implementado.
- **Variáveis, operadores e entrada/saída (Aulas 03-05):** cadastro interativo via `input()` dos dados principais da entidade do cenário, com conversão adequada de tipos e alguma regra de negócio (cálculo, validação, prioridade etc.) que use operadores relacionais e lógicos.
- **Comandos de decisão (Aula 06):** menu principal do sistema com múltiplas opções.
- **Comandos de repetição (Aula 07):** o menu permanece em execução até o usuário escolher sair, e as entradas críticas são validadas com repetição garantida.
- **Funções e procedimentos (Aula 10):** o sistema deve ser modularizado em funções (uma função por operação), evitando código repetido.

### **Estrutura de Dados a Aplicar (o grupo escolhe)**

Além dos fundamentos acima, cada grupo deve escolher **pelo menos uma estrutura de dados** dentre as ensinadas na disciplina e aplicá-la de forma central e bem justificada ao seu cenário sorteado — não é necessário (nem esperado) usar todas.

Estruturas disponíveis para escolha:

- **Vetores e matrizes** (Aulas 08-09) — útil quando o cenário tem algo naturalmente organizável em grade (vagas, poltronas, salas, prateleiras).
- **Recursão** (Aula 11) — útil para cálculos que se repetem sobre si mesmos (totais, valores progressivos, buscas).
- **Listas lineares encadeadas** — simples, duplamente ligada ou circular (Aula 13) — úteis para históricos e sequências de eventos.
- **Pilhas** (Aula 14) — úteis para ações do tipo "desfazer última operação" ou processamento no sentido inverso.
- **Filas ou deques** (Aula 14) — úteis para ordens de espera/atendimento.
- **Árvores binárias de busca e balanceamento** (Aula 15) — úteis para cadastro e busca rápida por uma chave (nome, código, identificador).

**Critérios para a estrutura escolhida ser aceita como válida:**
- Deve ser implementada com classes/lógica própria (não basta usar só a função pronta do Python, exceto quando a própria aula ensinou uma função nativa como ferramenta principal, ex. `numpy` para matrizes ou `collections.deque`).
- Deve resolver um problema real do cenário (não pode ser um trecho "decorativo" desconectado do restante do sistema).
- Deve suportar as operações básicas esperadas para aquela estrutura (ex.: em uma árvore, inserir, buscar e percorrer; em uma pilha, empilhar e desempilhar; em uma lista encadeada, inserir, remover e percorrer).
- No relatório técnico, o grupo deve justificar por que aquela estrutura foi a escolhida para o cenário, e não outra.

> Grupos que quiserem aplicar mais de uma estrutura são bem-vindos a fazer isso e serão valorizados na avaliação, mas isso não é obrigatório.

---

### **Lista de Cenários para Sorteio**

Cada cenário abaixo traz uma breve descrição e sugestões (não obrigatórias) de como mapear os conceitos da seção anterior ao domínio.

**1. Estacionamento**
Sistema de controle de entrada/saída de veículos em um pátio.
*Sugestões:* matriz = mapa de vagas; fila = veículos aguardando vaga; árvore = cadastro por placa.

**2. Locadora de Filmes/Jogos**
Sistema de aluguel e devolução de itens de um acervo.
*Sugestões:* matriz = prateleiras (corredor × prateleira); fila = lista de espera por um item popular; árvore = catálogo por título.

**3. Central de Atendimento (Banco/Hospital)**
Sistema de triagem e chamada de senhas de atendimento.
*Sugestões:* matriz = guichês/consultórios (linha × horário); fila = ordem de chegada; pilha = últimas senhas chamadas (para rechamar).

**4. Pedidos de uma Lanchonete/Delivery**
Sistema de recebimento e preparo de pedidos.
*Sugestões:* matriz = mesas do salão; fila = pedidos aguardando preparo; árvore = cardápio ordenado por código do item.

**5. Controle de Estoque de uma Loja**
Sistema de entrada e saída de mercadorias.
*Sugestões:* matriz = layout do depósito (corredor × prateleira); recursão = cálculo do valor total em estoque; árvore = produtos ordenados por código.

**6. Reserva de Salas/Auditórios**
Sistema de agendamento de espaços de uma instituição.
*Sugestões:* matriz = grade de horários × salas; fila = solicitações aguardando confirmação; árvore = salas ordenadas por identificador.

**7. Gerenciador de Tarefas (To-Do List Corporativo)**
Sistema de controle de tarefas de uma equipe, com prioridades.
*Sugestões:* matriz = quadro de tarefas (membro × dia da semana); pilha = desfazer última ação; árvore = tarefas ordenadas por prazo/prioridade.

**8. Bilheteria de Cinema/Teatro**
Sistema de venda de ingressos com escolha de assento.
*Sugestões:* matriz = mapa de poltronas (fileira × assento); fila = compradores aguardando disponibilidade; árvore = sessões ordenadas por horário.

**9. Torre de Controle Aéreo**
Sistema simplificado de pouso e decolagem de aeronaves.
*Sugestões:* fila = ordem de pouso/decolagem; pilha = histórico de últimas operações; árvore = voos ordenados por código.

**10. Agenda de Contatos/Catálogo Telefônico**
Sistema de cadastro e busca de contatos.
*Sugestões:* árvore = contatos ordenados por nome; lista encadeada = histórico de chamadas/mensagens; matriz = grade de favoritos por categoria.

> O docente pode adicionar novos cenários seguindo o mesmo padrão (uma entidade principal, algo naturalmente organizável em grade, algo com ordem de espera e algo naturalmente ordenável por chave).

---

### **Critérios de Avaliação**

- **Lógica e correção dos algoritmos** (15%): fluxograma/pseudocódigo coerente com o código; decisões e repetições corretas.
- **Fundamentos de programação** (20%): variáveis, operadores, entrada/saída, decisão e repetição bem aplicados no menu e nas regras do cenário.
- **Funções e modularização** (15%): código bem organizado em funções, sem repetição desnecessária, com parâmetros usados de forma justificada.
- **Estrutura de dados escolhida** (35%): implementação correta e completa da estrutura escolhida, bem integrada ao sistema e resolvendo um problema real do cenário (não apenas decorativa).
- **Relatório técnico** (5%): justificativa clara de por que aquela estrutura foi escolhida para o cenário sorteado.
- **Apresentação e domínio do código pelo grupo** (10%): clareza na explicação, funcionamento ao vivo do sistema e respostas às perguntas.

---

### **Entrega**
- Código-fonte completo, comentado e organizado em módulos/funções.
- Fluxograma ou pseudocódigo do fluxo principal (Aula 01-02), em arquivo separado (imagem ou PDF).
- Curto relatório técnico (1 página) indicando qual(is) estrutura(s) de dados foi(ram) escolhida(s), por que ela(s) faz(em) sentido para o cenário sorteado, e como foi(ram) implementada(s).
- Apresentação ao vivo, na última semana de aula, com o sistema em execução.
