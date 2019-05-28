#!/usr/bin/python
# -*- coding: UTF-8 -*-
import interface
import functions

tipoJogos = ['humano x humano', 'humano x computador', 'computador x computatador ']
tipoJogadores = ['jogador 1', 'jogador 2', 'computador 1', 'computador 2', 'Empate']
tipoJogadas = ['pedra', 'papel', 'tesoura']
historico = []  # [['pedra', ''papel', 'jogador 2'],['pedra', ''papel', 'jogador 2']] [[0, 1, 1],[0, 1, 1]]

interface.msgBemVindo()

while True:
    tipoJogo = interface.escolherTipoJogo()

    if tipoJogo == 1:
        functions.jogoTipo1()
    elif tipoJogo == 2:
        functions.jogoTipo2()
    elif tipoJogo == 3:
        functions.jogoTipo3()
