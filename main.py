#!/usr/bin/python
# -*- coding: UTF-8 -*-
import interface
import functions

tipoJogos = ['humano x humano', 'humano x computador', 'computador x computatador ']
tipoJogadores = ['jogador 1', 'jogador 2', 'computador 1', 'computador 2', 'Empate']
tipoJogadas = ['pedra', 'papel', 'tesoura']
historico = []  # [['pedra', ''papel', 'jogador 2'],['pedra', ''papel', 'jogador 2']] [[0, 1, 1],[0, 1, 1]]
print ("\n" * 80)
interface.msgBemVindo()
hes = 0

while True:
    if hes >= 1:
        tipoJogo = interface.escolherTipoJogo(hes)
    else:
        tipoJogo = interface.escolherTipoJogo(0)

    if tipoJogo == 1:
        functions.jogoTipo1()
    elif tipoJogo == 2:
        functions.jogoTipo2()
    elif tipoJogo == 3:
        functions.jogoTipo3()
    elif tipoJogo == 4:
        functions.jogoTipo4()
    hes += 1

