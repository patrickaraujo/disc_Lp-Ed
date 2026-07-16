# 🐍 Guia de instalação do Spyder

O **Spyder** é um ambiente de desenvolvimento para Python voltado especialmente para programação científica, análise de dados e aprendizado de máquina.

Este guia apresenta a instalação no:

- 🪟 Windows;
- 🍎 macOS;
- 🐧 Ubuntu;
- 🌿 Linux Mint.

Site oficial do Spyder:

<https://www.spyder-ide.org/>

---

# 🪟 Instalação no Windows

## 1. Acesse o site oficial

Abra o navegador e entre em:

<https://www.spyder-ide.org/>

Em seguida, clique em **Download**.

Você também pode acessar diretamente a página:

<https://www.spyder-ide.org/download>

## 2. Baixe o instalador

Na página de download, selecione a opção para **Windows**.

O arquivo baixado terá um nome semelhante a:

```text
Spyder-Windows-x86_64.exe
```

## 3. Execute a instalação

1. Abra a pasta **Downloads**.
2. Dê dois cliques no instalador do Spyder.
3. Caso o Windows mostre uma mensagem de segurança, clique em **Mais informações**.
4. Depois, clique em **Executar assim mesmo**.
5. Siga as instruções apresentadas pelo instalador.
6. Aguarde a conclusão da instalação.

## 4. Abra o Spyder

1. Abra o menu **Iniciar**.
2. Pesquise por **Spyder**.
3. Clique no programa para iniciá-lo.

> ⏳ Na primeira execução, o Spyder pode demorar um pouco mais para abrir.

---

# 🍎 Instalação no macOS

O Spyder possui instaladores diferentes para computadores Mac com processador **Apple Silicon** e **Intel**.

## 1. Descubra qual é o processador do Mac

1. Clique no símbolo da Apple, no canto superior esquerdo.
2. Selecione **Sobre Este Mac**.
3. Verifique a informação apresentada em **Chip** ou **Processador**.

Escolha a versão correspondente:

- **Apple M1, M2, M3, M4 ou mais recente:** Apple Silicon;
- **Intel:** versão para processadores Intel.

## 2. Acesse o site oficial

Abra:

<https://www.spyder-ide.org/download>

## 3. Baixe o instalador correto

Selecione a opção correspondente ao processador do computador.

O arquivo baixado terá um nome semelhante a:

```text
Spyder-macOS-arm64.pkg
```

ou:

```text
Spyder-macOS-x86_64.pkg
```

## 4. Execute a instalação

1. Abra a pasta **Downloads**.
2. Dê dois cliques no arquivo `.pkg`.
3. Siga as instruções apresentadas.
4. Caso seja solicitado, informe a senha do computador ou use o Touch ID.
5. Conclua a instalação.

## 5. Abra o Spyder

O Spyder pode ser aberto por uma destas opções:

- pasta **Aplicativos**;
- **Launchpad**;
- busca do **Spotlight**.

Para usar o Spotlight, pressione:

```text
Command + Espaço
```

Depois, digite:

```text
Spyder
```

> 🔒 Caso o macOS bloqueie a abertura, entre em **Ajustes do Sistema → Privacidade e Segurança** e autorize a execução do Spyder.

---

# 🐧 Instalação no Ubuntu ou Linux Mint pelo terminal

Instalar o Spyder no **Ubuntu** ou no **Linux Mint** pelo terminal é um processo simples. Existem três métodos principais, dependendo de como você prefere gerenciar programas e ambientes Python.

Para abrir o terminal, pressione:

```text
Ctrl + Alt + T
```

---

## ⚡ Método 1: usando o APT

### O método mais rápido e simples

Este método instala o Spyder diretamente dos repositórios da sua distribuição Linux.

É indicado para quem deseja uma instalação rápida, integrada ao sistema e suficiente para atividades introdutórias de programação.

### 1. Atualize a lista de pacotes

No terminal, execute:

```bash
sudo apt update
```

Pressione `Enter`.

Caso o sistema solicite uma senha, digite a senha do seu usuário e pressione `Enter`.

> 🔐 Durante a digitação da senha, nenhum caractere aparecerá na tela. Isso é normal no Linux.

### 2. Instale o Spyder

Execute:

```bash
sudo apt install spyder
```

Quando o terminal solicitar uma confirmação, pressione:

```text
S
```

ou:

```text
Y
```

A letra exibida depende do idioma do sistema.

### 3. Abra o Spyder

Depois da instalação, execute:

```bash
spyder
```

Também é possível procurar por **Spyder** no menu de aplicativos.

> ℹ️ A versão disponível pelo APT pode ser mais antiga que a versão mais recente publicada pelo projeto Spyder.

---

## 📊 Método 2: usando Conda

### Recomendado para ciência de dados e ambientes Python

Este método é indicado para estudantes que trabalham com:

- ciência de dados;
- inteligência artificial;
- aprendizado de máquina;
- bibliotecas com versões diferentes;
- múltiplos projetos Python.

> ⚠️ Para usar este método, é necessário já ter o **Anaconda**, **Miniconda** ou **Miniforge** instalado no computador.

O Conda permite criar um ambiente separado para o Spyder. Isso reduz conflitos entre versões de bibliotecas e projetos.

### 1. Crie um ambiente para o Spyder

Execute:

```bash
conda create -n spyder-env -c conda-forge spyder
```

Quando o Conda solicitar confirmação, digite:

```text
y
```

e pressione `Enter`.

### 2. Ative o ambiente

Execute:

```bash
conda activate spyder-env
```

Quando o ambiente estiver ativo, o terminal deverá apresentar algo semelhante a:

```text
(spyder-env)
```

antes do nome do usuário.

### 3. Abra o Spyder

Com o ambiente ativo, execute:

```bash
spyder
```

### 4. Como abrir novamente em outro momento

Sempre que quiser usar essa instalação do Spyder, abra o terminal e execute:

```bash
conda activate spyder-env
spyder
```

### 5. Como sair do ambiente

Depois de fechar o Spyder, você pode desativar o ambiente executando:

```bash
conda deactivate
```

> ✅ Este método é uma boa escolha para projetos de ciência de dados porque mantém o Spyder e suas bibliotecas organizados em um ambiente próprio.

---

## 📦 Método 3: usando Flatpak

### Uma alternativa para obter uma versão mais recente

As versões disponíveis pelo APT podem estar desatualizadas. O Flatpak permite instalar uma versão empacotada de forma independente dos pacotes principais do sistema.

No Linux Mint, o Flatpak normalmente já está disponível. No Ubuntu, pode ser necessário instalá-lo.

### 1. Instale o Flatpak

Execute:

```bash
sudo apt update
sudo apt install flatpak
```

### 2. Adicione o Flathub

Execute:

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

O **Flathub** é o repositório usado para localizar e instalar o Spyder pelo Flatpak.

### 3. Instale o Spyder

Execute:

```bash
flatpak install flathub org.spyder_ide.spyder
```

Confirme a instalação quando o terminal solicitar.

### 4. Abra o Spyder

Execute:

```bash
flatpak run org.spyder_ide.spyder
```

O Spyder também poderá aparecer no menu de aplicativos.

> ⚠️ O pacote do Spyder no Flathub é mantido pela comunidade e aparece como não verificado pelo desenvolvedor na página do Flathub.

---

# 🤔 Qual método escolher no Ubuntu ou Linux Mint?

## ⚡ Escolha o APT quando:

- você quer o processo mais simples;
- está começando a programar;
- usará o Spyder para exercícios e scripts básicos;
- não precisa obrigatoriamente da versão mais recente.

Comandos:

```bash
sudo apt update
sudo apt install spyder
spyder
```

## 📊 Escolha o Conda quando:

- você já possui Anaconda, Miniconda ou Miniforge;
- trabalha com ciência de dados ou aprendizado de máquina;
- precisa instalar diferentes bibliotecas;
- deseja separar os ambientes de cada projeto;
- quer reduzir conflitos entre versões de pacotes.

Comandos:

```bash
conda create -n spyder-env -c conda-forge spyder
conda activate spyder-env
spyder
```

## 📦 Escolha o Flatpak quando:

- você não quer usar Conda;
- deseja uma versão que pode ser mais recente que a oferecida pelo APT;
- prefere que o programa fique mais isolado do restante do sistema.

Comandos:

```bash
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.spyder_ide.spyder
flatpak run org.spyder_ide.spyder
```

> 🎓 **Recomendação para esta disciplina:** caso o professor não determine outro método, utilize o **Método 1 — APT**, por ser o mais simples para iniciantes.

---

# ✅ Testando a instalação

Depois de abrir o Spyder, localize o **Editor** e digite:

```python
import sys

print("Spyder instalado com sucesso! 🎉")
print("Versão do Python:", sys.version)
```

Salve o arquivo com o nome:

```text
teste_spyder.py
```

Para executar, clique no botão verde de execução ou pressione:

```text
F5
```

O **Console IPython** deverá mostrar uma mensagem semelhante a:

```text
Spyder instalado com sucesso! 🎉
```

---

# 🛠️ Solução de problemas no Linux

## O terminal informa que o pacote `spyder` não foi encontrado

Tente atualizar novamente a lista de pacotes:

```bash
sudo apt update
```

Depois, execute:

```bash
sudo apt install spyder
```

## O comando `spyder` não foi encontrado

Caso tenha instalado pelo APT, confirme a instalação:

```bash
sudo apt install spyder
```

Caso tenha instalado pelo Conda, ative primeiro o ambiente:

```bash
conda activate spyder-env
spyder
```

Caso tenha instalado pelo Flatpak, use:

```bash
flatpak run org.spyder_ide.spyder
```

## O comando `conda` não foi encontrado

Isso significa que o Anaconda, Miniconda ou Miniforge não está instalado ou não foi configurado no terminal.

Nesse caso, utilize o método APT:

```bash
sudo apt update
sudo apt install spyder
```

## O Spyder instalado pelo Flatpak não aparece no menu

Reinicie a sessão do usuário ou reinicie o computador. Depois, procure novamente por **Spyder** no menu de aplicativos.

Também é possível abri-lo diretamente pelo terminal:

```bash
flatpak run org.spyder_ide.spyder
```

---

# 🔗 Links úteis

- Site oficial do Spyder: <https://www.spyder-ide.org/>
- Página de download: <https://www.spyder-ide.org/download>
- Documentação de instalação: <https://docs.spyder-ide.org/current/installation.html>
- Spyder no Flathub: <https://flathub.org/apps/org.spyder_ide.spyder>

---

*📅 Guia revisado em agosto de 2026. Os comandos e a aparência das páginas podem mudar em versões futuras.*
