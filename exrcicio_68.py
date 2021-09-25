from random import randint
count = 0
print('Escolha um número. Eu vou escolher outro.\nO total será Par ou Ímpar!?')
while True:
    jogador = int(input('Ecolha seu número -> '))
    count += 1
    computador = randint(0, 10)
    total = jogador + computador
    escolha = jogo = ' '
    while escolha not in 'PI':
        escolha = str(input('Acha que vai ser PAR ou ÍMPAR ( P / I ) ? ')).upper().strip()[0]
        print(f'Eu escolhi {computador}, você escolheu {jogador}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Deu PAR, você venceu !')
        else:
            print('Deu ÍMPAR, você perdeu, tchau!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Deu ÍMPAR, você venceu !')
        else:
            print('Deu PAR, você errou, bye!')
            break
print(f'Foram {count} partidas. FIM!')
