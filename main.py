#!/usr/bin/python
# -*- coding: UTF-8 -*-
import interface
import functions

tipoJogos = ['humano x humano', 'humano x computador', 'computador x computatador ']
tipoJogadores = ['jogador 1', 'jogador 2', 'computador 1', 'computador 2', 'Empate']
tipoJogadas = ['pedra', 'papel', 'tesoura']
historicoPartidas = [] # [['pedra', ''papel', 'jogador 2'],['pedra', ''papel', 'jogador 2']] [[0, 1, 1],[0, 1, 1]]
historicoJogadores = [[],[],[],[]] # [["jogador 1"numeroPartidas, numeroVitorias, numeroEmpates],["jogador 2"],["Computador 1"],["Computador 1"]]
interface.msgBemVindo()
estatistica = 0

while True:
    if estatistica >= 1:
        tipoJogo = interface.escolherTipoJogo(estatistica)
    else:
        tipoJogo = interface.escolherTipoJogo(0)

    if tipoJogo == 1:
        functions.jogoTipo1()
    elif tipoJogo == 2:
        functions.jogoTipo2()
    elif tipoJogo == 3:
        functions.jogoTipo3()
    elif tipoJogo == 4:
        interface.historico()
    estatistica += 1

