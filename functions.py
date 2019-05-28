from random import Random

import interface

escolhas = []
statusJogada = ['Empate', 'Jogador 1', 'Jogador 2']
tipoJogadas = ['Pedra', 'Papel', 'Tesoura']

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

    interface.escolhaJogada()

    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador)
    print('Escolha do Computador: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    interface.ganhador(escolhas, 2)


def jogoTipo3():
    interface.escolhaJogada()

    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador)
    print('Escolha do Computador: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    interface.escolhaJogada()

    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador)
    print('Escolha do Computador: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    interface.ganhador(escolhas, 3)
