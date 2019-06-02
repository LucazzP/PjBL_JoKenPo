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
    teste = he
    if teste >= 1:
        print('┍-----┭---------------------------┑\n'
              '| Num |  Tipo de Jogo             |\n'
              '┝-----┽---------------------------┥\n'
              '|  1  |  Humano x Humano          |\n'
              '|  2  |  Humano x Computador      |\n'
              '|  3  |  Computador x Computador  |\n'
              '|  4  |  Histórico de Partida     |\n'
              '┗-----┵---------------------------┙\n')
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
    print("\n" * 30)
    print('┍-----┭---------------------------┑\n'
          '| Num |  Escolha sua jogada!      |\n'
          '┝-----┽---------------------------┥\n'
          '|  1  |  Pedra                    |\n'
          '|  2  |  Papel                    |\n'
          '|  3  |  Tesoura                  |\n'
          '┗-----┵---------------------------┙\n')



def ganhador(escolhas, tipoJogo):
    print("\n" * 30)
    if tipoJogo == 2:
        statusJogada.insert(2, 'Computador')
    elif tipoJogo == 3:
        statusJogada.insert(2, 'Computador 1')
        statusJogada.insert(3, 'Computador 2')

    if functions.avaliarJogada(escolhas) != 0:
        print(functions.statusJogada[functions.avaliarJogada(escolhas)] + ' GANHOU!')
    else:
        print(functions.statusJogada[functions.avaliarJogada(escolhas)])