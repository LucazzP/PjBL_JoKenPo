#!/usr/bin/python
# -*- coding: UTF-8 -*-
import interface
import functions

#Tipos de jogo
tipoJogos = ['Humano x Humano', 'Humano x Computador', 'Computador x Computatador ']

#Tipos de jogadores
tipoJogadores = ['Jogador 1', 'Jogador 2', 'Computador 1', 'Computador 2', 'Empate']

#Tipos de jogadas
tipoJogadas = ['pedra', 'papel', 'tesoura']

#Histórico de cada partida
historicoPartidas = [] # [['pedra', ''papel', 'jogador 2'],['pedra', ''papel', 'jogador 2']] [[0, 1, 1],[0, 1, 1]]

#Histórico de todas as partidas de cada jogador
historicoJogadores = [[],[],[],[]] # [["jogador 1"numeroPartidas, numeroVitorias, numeroEmpates],["jogador 2"],["Computador 1"],["Computador 1"]]

#Mensagem de bem vindo
interface.msgBemVindo()

#Variável inicial que mostra que não há histórico
estatistica = 0

while True:
    #Se já foi jogado, mostra a opção do histórico
    if estatistica >= 1:
        tipoJogo = interface.escolherTipoJogo(estatistica)
    else:
        tipoJogo = interface.escolherTipoJogo(0)

    #Escolha do tipo de jogo e encaminhamento para o determinado
    #Humano x Humano
    if tipoJogo == 1:
        functions.jogoTipo1()
        
    #Humano x Computador
    elif tipoJogo == 2:
        functions.jogoTipo2()
        
    #Computador x Computador    
    elif tipoJogo == 3:
        functions.jogoTipo3()
        
    #Historico
    elif tipoJogo == 4:
        interface.historico()
    estatistica += 1

