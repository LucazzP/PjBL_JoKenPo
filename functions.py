from random import Random

import interface

#Vetores iniciais
escolhas = []
tipoJogadas = ['Pedra', 'Papel', 'Tesoura']
historicoPartidas = []
historicoJogadores = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

#Jogada ganhadora
def avaliarJogada(escolhas):
    #Empate
    if escolhas[0] == escolhas[1]:
        return 0
    #Pedra x Tesoura = Pedra ganha
    elif escolhas[0] == 1 and escolhas[1] == 3:
        return 1
    #Pedra x Papel = Papel ganha
    elif escolhas[0] == 1 and escolhas[1] == 2:
        return 2
    #Papel x Pedra = Papel ganha
    elif escolhas[0] == 2 and escolhas[1] == 1:
        return 1
    #Papel x Tesoura = Tesoura ganha
    elif escolhas[0] == 2 and escolhas[1] == 3:
        return 2
    #Tesoura x Papel = Tesoura ganha
    elif escolhas[0] == 3 and escolhas[1] == 2:
        return 1
    #Tesoura x Pedra = Pedra ganha
    elif escolhas[0] == 3 and escolhas[1] == 1:
        return 2

#Humano x Humano
def jogoTipo1():
    #Escolher a jogada a ser feita (Humano 1)
    interface.escolhaJogada()

    escolhas.insert(0, int(input('Escolha a jogada do Jogador 1: \n')))
    
    #Escolher a jogada a ser feita (Humano 2)
    interface.escolhaJogada()

    escolhas.insert(1, int(input('Escolha a jogada do Jogador 2: \n')))

    interface.ganhador(escolhas, 1)

#Humano x Humano
def jogoTipo2():
    #Escolher a jogada a ser feita (Humano 1)
    interface.escolhaJogada()

    escolhas.insert(0, int(input('Escolha a jogada do Jogador 1: \n')))
    
    #Jogada do computador, aleatória 
    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador)
    print('Escolha do Computador: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    interface.ganhador(escolhas, 2)


#Computador x Computador
def jogoTipo3():
    #Jogada do computador 1, aleatória
    jogadaComputador = Random.randint(Random(), 1, 3)
    escolhas.insert(0, jogadaComputador)
    print('Escolha do Computador 1: ' + tipoJogadas[jogadaComputador - 1] + '\n')

    #Jogada do computador 1, aleatória
    jogadaComputador2 = Random.randint(Random(), 1, 3)
    escolhas.insert(1, jogadaComputador2)
    print('Escolha do Computador 2: ' + tipoJogadas[jogadaComputador2 - 1] + '\n')

    interface.ganhador(escolhas, 3)

#Adicionar ao histórico quem ganhou
def adicionarAoHistorico(statusJogada, ganhador):
    historicoPartidas.append([escolhas[0], escolhas[1], ganhador])

    #Jogador 1 Ganhou
    if statusJogada[1] == 'Jogador 1':
        jogador1 = historicoJogadores[0]
        historicoJogadores[0] = addHistorico(statusJogada[1], ganhador, jogador1)
    #Jogador 2 Ganhou
    if statusJogada[2] == 'Jogador 2':
        jogador1 = historicoJogadores[1]
        historicoJogadores[1] = addHistorico(statusJogada[2], ganhador, jogador1)
    #Computador 1 Ganhou
    if statusJogada[1] == 'Computador 1':
        jogador1 = historicoJogadores[2]
        historicoJogadores[2] = addHistorico(statusJogada[1], ganhador, jogador1)
    #Computador 2 Ganhou
    if statusJogada[2] == 'Computador 2':
        jogador1 = historicoJogadores[3]
        historicoJogadores[3] = addHistorico(statusJogada[2], ganhador, jogador1)

#Adicionar ao histórico quantidade de vitórias e empates de cada jogador
def addHistorico(jogador, ganhador, jogador1):
    ganhou = 0
    empate = 0

    #Adicionar quantidade de vitórias
    if jogador == ganhador:
        ganhou = 1
    #Adicionar quantidade de empates
    elif ganhador == 'Empate':
        empate = 1

    #Adicionar quantidades aos jogadores
    try:
        jogador1 = [jogador1[0] + 1, jogador1[1] + ganhou, jogador1[2] + empate]
    except:
        jogador1 = [1, ganhou, empate]

    return  jogador1