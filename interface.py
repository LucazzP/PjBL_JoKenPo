#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import functions

statusJogada = ['Empate', 'Jogador 1', 'Jogador 2']
tipoJogadas = ['Pedra', 'Papel', 'Tesoura']

# Mensagem de boas-vindas
def msgBemVindo():
    print('┍---------------------------------┑\n'
          '|      BEM VINDO AO JOKENPO!      |\n'
          '┝-----┭---------------------------┥\n'
          '| Num |  Integrantes              |\n'
          '┝-----┽---------------------------┥\n'
          '|  1  |  Lucas Henrique Polazzo   |\n'
          '|  2  |  Renan Maciel Antunes     |\n'
          '|  3  |  Pedro Henrique Lucho     |\n'
          '┗-----┵---------------------------┙\n')

#Interface de escolha do tipo de jogo
def escolherTipoJogo(he):
    estatistica = he
    #Se já foi jogado mostra a opção de histórico de partida
    if estatistica >= 1:
        print('┍-----┭-------------------------------------------┑\n'
              '| Num |  Tipo de Jogo e Configurações             |\n'
              '┝-----┽-------------------------------------------┥\n'
              '|  1  |  Humano x Humano                          |\n'
              '|  2  |  Humano x Computador                      |\n'
              '|  3  |  Computador x Computador                  |\n'
              '|  4  |  Histórico de Partida                     |\n'
              '┗-----┵-------------------------------------------┙\n')
    else:
        print('┍-----┭---------------------------┑\n'
              '| Num |  Tipo de Jogo             |\n'
              '┝-----┽---------------------------┥\n'
              '|  1  |  Humano x Humano          |\n'
              '|  2  |  Humano x Computador      |\n'
              '|  3  |  Computador x Computador  |\n'
              '┗-----┵---------------------------┙\n')

    #Fazer a escolha
    escolha = int(input('Escolha o tipo de jogo: \n'))

    return escolha

#Interface para escolher a jogada
def escolhaJogada():
    print('┍-----┭---------------------------┑\n'
          '| Num |  Escolha sua jogada!      |\n'
          '┝-----┽---------------------------┥\n'
          '|  1  |  Pedra                    |\n'
          '|  2  |  Papel                    |\n'
          '|  3  |  Tesoura                  |\n'
          '┗-----┵---------------------------┙\n')

#Histórico
def historico():
    #Vetores com os jogadores / resultado  
    tipoJogadores = ['Jogador 1', 'Jogador 2', 'Computador 1', 'Computador 2', 'Empate']
    #Vetor das jogadas possíveis
    tipoJogadas = ['Pedra', 'Papel', 'Tesoura']
    #Variável para não ter que ficar importando toda hora
    historicoJogadores = functions.historicoJogadores
    historicoPartidas = functions.historicoPartidas
    
    #Valores iniciais de vitória para cada jogador
    jogador1P = 0
    jogador2P = 0
    computador1P = 0
    computador2P = 0

    #Porcentagem de vitória 
    if historicoJogadores[0][0] != 0:
        jogador1P = (historicoJogadores[0][1] / historicoJogadores[0][0]) * 100
    if historicoJogadores[1][0] != 0:
        jogador2P = (historicoJogadores[1][1] / historicoJogadores[1][0]) * 100
    if historicoJogadores[2][0] != 0:
        computador1P = (historicoJogadores[2][1] / historicoJogadores[2][0]) * 100
    if historicoJogadores[3][0] != 0:
        computador2P = (historicoJogadores[3][1] / historicoJogadores[3][0]) * 100

    #Interface com formatação para os valores serem colocados nos devidos lugares (Qtd de jogos/vitorias/empates e % de vitória)
    print('┍--------------┭-------┭-----------┭---------┭-----------┑\n'
          '| Player       | Jogos | Vitorias | Empates | % Vitoria  |\n'
          '┝--------------┽-------┽-----------┽---------┽-----------┥\n'                                                    
          '| Jogador 1    |    {}  |     {}    |     {}   |    {:.2f} %  |\n'
          '| Jogador 2    |    {}  |     {}    |     {}   |    {:.2f} %  |\n'
          '| Computador 1 |    {}  |     {}    |     {}   |    {:.2f} %  |\n'
          '| Computador 2 |    {}  |     {}    |     {}   |    {:.2f} %  |\n'
          '┗--------------┵-------┵-----------┵---------┵-----------┙\n\n'.format(
        historicoJogadores[0][0], historicoJogadores[0][1], historicoJogadores[0][2], jogador1P,
        historicoJogadores[1][0], historicoJogadores[1][1], historicoJogadores[1][2], jogador2P,
        historicoJogadores[2][0], historicoJogadores[2][1], historicoJogadores[2][2], computador1P,
        historicoJogadores[3][0], historicoJogadores[3][1], historicoJogadores[3][2], computador2P,
    ))

    #Interface com formatação para os valores serem colocados nos devidos lugares (Tipo de jogadas feitas pelos jogadores e ganhador)
    print('┍--------------┭------------┭------------┑\n'
          '| Jogador 1    | Jogador 2 |  Ganhador  |\n'
          '┝--------------┽-----------┽------------┥')
    
    #Cada jogo uma linha
    for historico in historicoPartidas:  
        print('|  {}     |  {}     |  {}  |'.format(
            tipoJogadas[historico[0] - 1], tipoJogadas[historico[1] - 1], historico[2]
        ))

    print('┗--------------┵-----------┵------------┙\n\n\n\n\n\n\n\n')


def ganhador(escolhas, tipoJogo):
    statusJogada = ['Empate', 'Jogador 1', 'Jogador 2']

    #Humano x Computador
    if tipoJogo == 2:
        statusJogada.remove('Jogador 1')
        statusJogada.insert(1, 'Computador 1')
    
    #Computador x Computador
    elif tipoJogo == 3:
        statusJogada.remove('Jogador 1')
        statusJogada.insert(1, 'Computador 1')
        statusJogada.remove('Jogador 2')
        statusJogada.insert(2, 'Computador 2')

    #Mostrar quem ganhou
    ganhador = statusJogada[functions.avaliarJogada(escolhas)]

    if functions.avaliarJogada(escolhas) != 0:
        print(ganhador + ' GANHOU!')
    else:
        print(ganhador)

    #Enviar para o histório quem ganhou
    functions.adicionarAoHistorico(statusJogada, ganhador)
