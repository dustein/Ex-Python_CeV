print('Jogo de Dados')
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(1,6),
'jogador2' : randint(1, 6),
'jogador3' : randint(1, 6),
'jogador4' : randint(1, 6)}
print(':: Jogadas ::')
for r, j in jogo.items():
    print(f'{r} acertou {j} nos dados.')
sleep(2)
ranking = list()
print()
print('=-=-= R A N K I N G = - = - =')
print()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # itemgetter função de dicionário para pegar o valor do item
for c, j in enumerate(ranking):
    sleep(1)
    print(f'{c+1}º colocado {j[0]} com {j[1]} pontos.')