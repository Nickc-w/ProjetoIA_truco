
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

### Parâmetros de Aprendizado

O agente utiliza alguns parâmetros para controlar o processo de aprendizado:

- Epsilon (ε): controla a frequência com que a CPU explora novas ações em vez de utilizar a melhor ação conhecida.
- Alpha (α): controla o quanto novas experiências influenciam os valores armazenados na Q-Table.
- Gamma (γ): controla a importância das recompensas futuras durante o processo de aprendizado.


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
* Exibição da Q-table e dos estados aprendidos no terminal


## Limitações

Para simplificação do projeto, algumas regras NÃO foram implementadas:

- Jogo em duplas (2x2)  
- Pedido de Truco (3, 6, 9, 12 pontos)  
- Blefe e estratégias avançadas

## Bibliotecas utilizadas
- tkinter (interface gráfica)
- Pillow (manipulação de imagens)
- pickle (persistência da Q-table)
- random (embaralhamento e sorteio de cartas)

## Autores
  - Nicolly Cândida Santa Cruz
  - Pedro Cerqueira Rosa de Resende
  - Ryan
  - Arthur torquato
  - Letícia Borsaro

## Como executar o projeto

1. Baixe ou clone este repositório e execute o arquivo principal do projeto.

2. Instale a biblioteca necessária:

```bash
pip install pillow
```

3. Execute o arquivo `truco.py` utilizando o botão Run da sua IDE
ou pelo terminal:

```bash
python truco.py
```


