
# Truco Simplificado em Python – Interface Gráfica com Tkinter

## Sobre o Projeto
Este projeto consiste em uma implementação simplificada do jogo de Truco utilizando Python e Tkinter. O objetivo é criar um ambiente funcional para um jogador humano contra um agente (CPU), servindo como base para futuras aplicações de Inteligência Artificial.

## Objetivos do Projeto

### Interface gráfica com Tkinter
Criação de uma interface interativa com cartas, animações e atualização dinâmica dos elementos visuais.

### Simulação de um ambiente de Truco simplificado 1v1
Implementação de uma versão simplificada do Truco, permitindo partidas entre jogador e CPU.

### Objetivo futuro: Inteligência Artificial por Reforço
O ambiente foi desenvolvido para possibilitar futuras implementações de Inteligência Artificial, especialmente utilizando técnicas de Aprendizado por Reforço para tomada de decisão. 

## Regras Implementadas

O jogo segue as principais regras do Truco:

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

- Interface gráfica interativa  
- Animação das cartas na mesa  
- CPU jogando automaticamente  
- Cálculo automático da manilha  
- Comparação de cartas e definição do vencedor  
- Reinício automático da partida  

## Limitações

Para simplificação do projeto, algumas regras NÃO foram implementadas:

- Jogo em duplas (2x2)  
- Pedido de Truco (3, 6, 9, 12 pontos)  
- Blefe e estratégias avançadas  

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

3. Execute no terminal:

```bash
python truco.py
```


