import random

tents = 0
scr = []

while True:
    try:
        vi = int(input('Qual o menor valor? '))
        vf = int(input('Qual o maior valor? '))
        rst = random.randint(vi, vf)
        cht = int(input('Qual o seu palpite? '))
        mai = cht + 50
        men = cht - 50
        tents += 1

        if cht == rst:
            print(f'Você acertou em {tents} tentativas!')
            scr.append(tents)
            scr.sort()
            jog = 1

            print(f'Seu recorde de tentativas é {min(scr)}')

            if len(scr) == 2:
                print(f'Seu top 2 é: 1° {scr[0]} e 2° {scr[1]}')
                
            elif len(scr) > 2:
                print(f'Seu top 3 é: 1° {scr[0]}, 2° {scr[1]} e 3° {scr[2]}')

            if input('Quer sair') == 'S':
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

    except ValueError:
        print('Erro de digitação, coloque apenas números na resposta')