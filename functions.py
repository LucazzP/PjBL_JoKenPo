from random import Random

import interface

escolhas = []
tipoJogadas = ['Pedra', 'Papel', 'Tesoura']
historicoPartidas = []
historicoJogadores = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]


def avaliarJogada(escolhas):
    if escolhas[0] == escolhas[1]:
        return 0
    elif escolhas[0] == 1 and escolhas[1] == 3:
        return 1
    elif escolhas[0] == 1 and escolhas[1] == 2:
        return 2
    elif escolhas[0] == 2 and escolhas[1] == 1:
        return 1
    elif escolhas[0] == 2 and escolhas[1] == 3:
        return 2
    elif escolhas[0] == 3 and escolhas[1] == 2:
        return 1
    elif escolhas[0] == 3 and escolhas[1] == 1:
        return 2


def jogoTipo1():
    interface.escolhaJogada()

    escolhas.insert(0, int(input('Escolha a jogada do Jogador 1: \n')))

    interface.escolhaJogada()

    escolhas.insert(1, int(input('Escolha a jogada do Jogador 2: \n')))

    interface.ganhador(escolhas, 1)


def jogoTipo2():
    interface.escolhaJogada()

    escolhas.insert(0, int(input('Escolha a jogada do Jogador 1: \n')))

    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador)
    print('Escolha do Computador: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    interface.ganhador(escolhas, 2)


def jogoTipo3():
    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(0, jogadaComputador)
    print('Escolha do Computador 1: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    jogadaComputador2 = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador2)
    print('Escolha do Computador 2: ' + tipoJogadas[jogadaComputador2 - 1] + '\n')

    interface.ganhador(escolhas, 3)


def adicionarAoHistorico(statusJogada, ganhador):
    historicoPartidas.append([escolhas[0], escolhas[1], ganhador])

    if statusJogada[1] == 'Jogador 1':
        jogador1 = historicoJogadores[0]
        historicoJogadores[0] = addHistorico(statusJogada[1], ganhador, jogador1)
    if statusJogada[2] == 'Jogador 2':
        jogador1 = historicoJogadores[1]
        historicoJogadores[1] = addHistorico(statusJogada[2], ganhador, jogador1)
    if statusJogada[1] == 'Computador 1':
        jogador1 = historicoJogadores[2]
        historicoJogadores[2] = addHistorico(statusJogada[1], ganhador, jogador1)
    if statusJogada[2] == 'Computador 2':
        jogador1 = historicoJogadores[3]
        historicoJogadores[3] = addHistorico(statusJogada[2], ganhador, jogador1)


def addHistorico(jogador, ganhador, jogador1):
    ganhou = 0
    empate = 0

    if jogador == ganhador:
        ganhou = 1
    elif ganhador == 'Empate':
        empate = 1

    try:
        jogador1 = [jogador1[0] + 1, jogador1[1] + ganhou, jogador1[2] + empate]
    except:
        jogador1 = [1, ganhou, empate]

    return  jogador1