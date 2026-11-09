import os
import random

past = os.path.dirname(os.path.abspath(__file__))
cdr = os.path.join(past, 'Ert1_ranking.txt')

hardcore = False
if input('Hardcore? ') == 'S':
    hardcore = True
    maxtents = int(input('Quantos chutes? '))

tents = 0
scr = []
vi = int(input('Qual o menor valor? '))
vf = int(input('Qual o maior valor? '))
rst = random.randint(vi, vf)

nome = input('Digite seu nome ')

if nome.strip().lower() == 'delete':
        with open(cdr, 'w'):
            pass

        scr = []
        print('Histórico de jogadas apagado com sucesso')
        nome = input('Digite seu nome ')

while True:
    try:
        cht = int(input('Qual o seu palpite? '))
        mai = cht + 50
        men = cht - 50
        tents += 1
        if hardcore:
            maxtents -= 1

        if cht == rst:
            print(f'Você acertou em {tents} tentativas!')
            scr.append(tents)
            scr.sort()

            if hardcore:
                with open(cdr, 'a') as arq:
                    arq.write(f"{nome} ganhou o hardcore em {tents} de {maxtents} tentativas. A margem da partida era entre {vi} e {vf}\n")
            else:
                with open(cdr, 'a') as arq:
                    arq.write(f"{nome} acertou em {tents} tentativas. A margem da partida era entre {vi} e {vf}\n")

            print(f'Seu recorde de tentativas é {min(scr)}')

            if input('Quer sair? ') == 'S':
                break

            else:
                rst = random.randint(vi, vf)
                tents = 0

        elif cht < rst:
            if mai < rst:
                print('Tente um número bem maior')

            else:
                print('Tente um número maior')

        else:
            if men > rst:
                print('Tente um número bem menor')

            else:
                print('Tente um número menor')

        if hardcore and maxtents == 0:
            print('Game Over, suas tentativas acabaram')

            with open(cdr, 'a') as arq:
                arq.write(f"{nome} perdeu o hardcore que tinha {maxtents} tentativas. A margem da partida era entre {vi} e {vf}\n")
            break

    except ValueError:
        print('Erro de digitação, coloque apenas números na resposta')