#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import functions

statusJogada = ['Empate', 'Jogador 1', 'Jogador 2']
tipoJogadas = ['Pedra', 'Papel', 'Tesoura']


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


def escolherTipoJogo(he):
    estatistica = he
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

    escolha = int(input('Escolha o tipo de jogo: \n'))

    return escolha


def escolhaJogada():
    print('┍-----┭---------------------------┑\n'
          '| Num |  Escolha sua jogada!      |\n'
          '┝-----┽---------------------------┥\n'
          '|  1  |  Pedra                    |\n'
          '|  2  |  Papel                    |\n'
          '|  3  |  Tesoura                  |\n'
          '┗-----┵---------------------------┙\n')


def historico():
    tipoJogadores = ['Jogador 1', 'jogador 2', 'Computador 1', 'computador 2', 'Empate']
    tipoJogadas = ['Pedra', 'Papel', 'Tesoura']
    historicoJogadores = functions.historicoJogadores
    historicoPartidas = functions.historicoPartidas

    jogador1P = 0
    jogador2P = 0
    computador1P = 0
    computador2P = 0

    if historicoJogadores[0][0] != 0:
        jogador1P = (historicoJogadores[0][1] / historicoJogadores[0][0]) * 100
    if historicoJogadores[1][0] != 0:
        jogador2P = (historicoJogadores[1][1] / historicoJogadores[1][0]) * 100
    if historicoJogadores[2][0] != 0:
        computador1P = (historicoJogadores[2][1] / historicoJogadores[2][0]) * 100
    if historicoJogadores[3][0] != 0:
        computador2P = (historicoJogadores[3][1] / historicoJogadores[3][0]) * 100

    print('┍--------------┭-------┭-----------┭---------┭-----------┑\n'
          '| Player       | Jogos | Vitorias | Empates | % Vitoria |\n'
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

    print('┍--------------┭------------┭------------┑\n'
          '| Jogador 1    | Jogador 2 |  Ganhador  |\n'
          '┝--------------┽-----------┽------------┥')

    for historico in historicoPartidas:
        print('|  {}      | {}   |  {}  |'.format(
            tipoJogadas[historico[0] - 1], tipoJogadas[historico[1] - 1], historico[2]
        ))

    print('┗--------------┵-----------┵------------┙\n\n\n\n\n\n\n\n')


def ganhador(escolhas, tipoJogo):
    statusJogada = ['Empate', 'Jogador 1', 'Jogador 2']

    if tipoJogo == 2:
        statusJogada.remove('Jogador 1')
        statusJogada.insert(1, 'Computador 1')
    elif tipoJogo == 3:
        statusJogada.remove('Jogador 1')
        statusJogada.insert(1, 'Computador 1')
        statusJogada.remove('Jogador 2')
        statusJogada.insert(2, 'Computador 2')

    ganhador = statusJogada[functions.avaliarJogada(escolhas)]

    if functions.avaliarJogada(escolhas) != 0:
        print(ganhador + ' GANHOU!')
    else:
        print(ganhador)

    functions.adicionarAoHistorico(statusJogada, ganhador)
