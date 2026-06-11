
# Truco Simplificado em Python – Interface Gráfica com Tkinter

## Sobre o Projeto

Este projeto consiste em uma implementação simplificada do jogo de Truco paulistano utilizando Python e Tkinter. O sistema permite partidas entre um jogador humano e uma CPU controlada por um agente de Inteligência Artificial baseado em Q-Learning.

O principal problema abordado é a tomada de decisão da CPU durante uma partida de Truco, ou seja, determinar qual carta deve ser jogada em cada situação para aumentar as chances de vitória.

O objetivo do projeto é aplicar conceitos de Aprendizado por Reforço em um ambiente de jogo, permitindo que a CPU aprenda estratégias ao longo das partidas por meio de estados, ações, recompensas e atualização de uma Q-table.

### Inteligência Artificial por Reforço (Q-Learning)

O projeto utiliza um agente baseado em Q-Learning para controlar as decisões da CPU durante as partidas.

A cada jogada, a CPU observa o estado atual do jogo, escolhe uma ação e recebe uma recompensa de acordo com o resultado obtido. Essas recompensas são utilizadas para atualizar uma Q-table, que armazena o conhecimento adquirido pelo agente ao longo das partidas.

Os estados representam a situação observada pela CPU, considerando as forças das cartas disponíveis em sua mão e a força da carta jogada pelo adversário. As ações representam a escolha de qual carta disponível será utilizada na rodada.

O sistema de recompensas foi desenvolvido para incentivar decisões estratégicas, recompensando vitórias e penalizando derrotas, especialmente em situações que envolvem o uso inadequado de manilhas.

A Q-table é salva em arquivo, permitindo que o aprendizado seja preservado entre diferentes execuções do programa.

## Como a Inteligência Artificial Funciona

A CPU utiliza a técnica de Aprendizado por Reforço (Q-Learning) para aprender quais decisões tendem a gerar melhores resultados durante as partidas.

### Estados

Os estados representam a situação atual observada pela CPU.

No projeto, cada estado é composto por:

* As forças das cartas disponíveis na mão da CPU
* A força da carta jogada pelo adversário

Exemplo:

```text
((0, 5, 103), 8)
```

Onde:

* `0` representa uma carta fraca
* `5` representa uma carta de força intermediária
* `103` representa uma manilha
* `8` representa a força da carta jogada pelo adversário

Dessa forma, a CPU consegue analisar o contexto atual antes de tomar uma decisão.

### Ações

As ações representam as possíveis jogadas da CPU.

Cada ação corresponde à escolha de uma das cartas disponíveis em sua mão.

Exemplo:

* Ação 0 → jogar a primeira carta disponível
* Ação 1 → jogar a segunda carta disponível
* Ação 2 → jogar a terceira carta disponível

### Sistema de Recompensas

O aprendizado da CPU é baseado em recompensas e penalidades.

Alguns exemplos utilizados no projeto:

* Vitória na rodada: recompensa positiva
* Derrota na rodada: penalidade
* Vitória utilizando uma carta comum: recompensa maior
* Desperdício de manilha: penalidade adicional
* Vitória da mão: grande recompensa
* Derrota da mão: grande penalidade

Esse sistema incentiva a CPU a utilizar suas cartas de forma mais eficiente ao longo das partidas.


## Q-Table

A Q-Table armazena o conhecimento adquirido pela CPU.

Para cada estado do jogo, a tabela guarda uma avaliação para cada ação possível.

Quando uma ação produz bons resultados, seu valor aumenta. Quando produz resultados ruins, seu valor diminui.

Ao longo das partidas, a CPU passa a priorizar ações que historicamente geraram melhores recompensas.

O agente utiliza a estratégia epsilon-greedy, alternando entre explorar novas ações e utilizar o conhecimento já adquirido armazenado na Q-Table.

Sempre que a Q-table é salva, o terminal exibe apenas informações resumidas sobre o aprendizado e a exportação (quantidade de estados e confirmação do CSV). A tabela completa é exportada automaticamente para `q_table.csv`, permitindo visualização detalhada no Excel ou no VS Code. O armazenamento principal da IA continua sendo o arquivo `q_table.pkl`.

### Como visualizar o `q_table.csv`

Para ver a tabela organizada em colunas no VS Code, instale as extensões **CSV** e **Excel Viewer**.

Depois de abrir o arquivo `q_table.csv`, use `Ctrl + Shift + V` para abrir a visualização em tabela (Excel Viewer: Open Preview).

Também é possível abrir o arquivo diretamente no Microsoft Excel.

### Parâmetros de Aprendizado

O agente utiliza alguns parâmetros para controlar o processo de aprendizado:

- Epsilon (ε): controla a frequência com que a CPU explora novas ações em vez de utilizar a melhor ação conhecida. Na interface gráfica, o valor padrão é `0.2`.
- Max epsilon: valor inicial da exploração no treino offline (`1.0`). Quanto maior, mais a CPU explora no começo do `--train`.
- Min epsilon: valor mínimo de exploração (`0.01`). A CPU nunca explora abaixo disso.
- Epsilon decay: taxa de redução do epsilon após cada partida (`0.995`). Faz a CPU passar gradualmente de explorar para usar o que já aprendeu.
- Alpha (α): controla o quanto novas experiências influenciam os valores armazenados na Q-Table (`0.3`).
- Gamma (γ): controla a importância das recompensas futuras durante o processo de aprendizado (`0.9`).


### Interface gráfica com Tkinter
Criação de uma interface interativa com cartas, animações e atualização dinâmica dos elementos visuais.

### Simulação de um ambiente de Truco simplificado 1v1
Implementação de uma versão simplificada do Truco, permitindo partidas entre jogador e CPU.

## Regras Implementadas

O jogo segue as principais regras do Truco Paulista:

- Cada jogador recebe 3 cartas  
- Uma carta vira define a manilha  
- A manilha é a carta seguinte na sequência da vira  
- Ordem das cartas: 4 < 5 < 6 < 7 < Q < J < K < A < 2 < 3  
- A manilha sempre vence qualquer carta comum  
- Em caso de disputa entre manilhas, a força é decidida pelo naipe  
- Comparação entre cartas jogadas  
- Sistema de rodadas (melhor de 3)  
- O jogador que vencer 2 rodadas ganha a partida  
- A partida pode terminar antes da terceira rodada  

## Funcionalidades

* Interface gráfica interativa
* Animação das cartas na mesa
* CPU jogando automaticamente
* Cálculo automático da manilha
* Comparação de cartas e definição do vencedor
* Reinício automático da partida
* Agente de Inteligência Artificial baseado em Q-Learning
* Representação de estados do jogo para tomada de decisão
* Sistema de recompensas e penalidades
* Atualização automática da Q-table durante as partidas
* Persistência do aprendizado em arquivo (.pkl)
* Estratégia de exploração e aproveitamento (epsilon-greedy)
* Exibição resumida da Q-table no terminal (quantidade de estados e confirmação do CSV)
* Exportação automática da Q-table completa para `q_table.csv`
* Treinamento offline da CPU pelo terminal (sem abrir a interface gráfica)
* Avaliação do desempenho da CPU pelo terminal


## Limitações

Para simplificação do projeto, algumas regras NÃO foram implementadas:

- Jogo em duplas (2x2)  
- Pedido de Truco (3, 6, 9, 12 pontos)  
- Blefe e estratégias avançadas

## Bibliotecas utilizadas
- tkinter (interface gráfica)
- Pillow (manipulação de imagens)
- pickle (persistência da Q-table)
- csv (exportação da Q-table para visualização)
- random (embaralhamento e sorteio de cartas)

## Autores
  - Nicolly Cândida Santa Cruz
  - Pedro Cerqueira Rosa de Resende
  - Ryan
  - Arthur torquato
  - Letícia Borsaro

## Como executar o projeto

1. Baixe ou clone este repositório.

2. Instale a biblioteca necessária:

```bash
pip install pillow
```

3. Abra o terminal na pasta do projeto (onde está o arquivo `truco.py`).

4. Escolha uma das opções abaixo.

### Jogar normalmente (interface gráfica)

Abre o jogo na tela. Você joga contra a CPU clicando nas cartas.

```bash
python truco.py
```

A CPU aprende durante as partidas e salva o progresso em `q_table.pkl`. Ao fim de cada mão, a tabela completa também é exportada para `q_table.csv`.

### Treinar a CPU (pelo terminal, sem abrir o jogo)

Simula várias partidas automaticamente para a CPU aprender mais rápido.

```bash
python truco.py --train 1000
```

O número `1000` é a quantidade de partidas simuladas. Você pode trocar:

```bash
python truco.py --train 50
python truco.py --train 5000
```

Quanto maior o número, mais a CPU treina — porém demora mais.

Ao final, o progresso é salvo em `q_table.pkl`. No terminal, são exibidas as mensagens resumidas (`Q-table salva com N estados` e `CSV atualizado com sucesso`) e a tabela completa é exportada para `q_table.csv`.

### Avaliar a CPU (pelo terminal, sem abrir o jogo)

Testa o desempenho da CPU **sem alterar** o que ela já aprendeu.

```bash
python truco.py --eval 100
```

O número `100` é a quantidade de partidas de teste. Você pode trocar:

```bash
python truco.py --eval 50
python truco.py --eval 200
```

No final, o terminal exibe um resumo com vitórias, derrotas, taxa de vitória e reward médio. Exemplo:

```text
Avaliação (100 partidas):
Vitórias: 52
Derrotas: 48
Taxa de vitória: 52.0%
Reward médio: 10.0
```

### Ordem sugerida para testar

Se você quer ver se a IA está melhorando, siga estes passos:

1. Treinar: `python truco.py --train 2000`
2. Avaliar: `python truco.py --eval 200`
3. Jogar: `python truco.py`

Repita o treino e a avaliação para comparar os resultados.

> **Observação:** também é possível executar o arquivo `truco.py` pelo botão Run da sua IDE, mas os comandos `--train` e `--eval` funcionam apenas pelo terminal.

