jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador -> '))
total = int(input(f'Em quantos jogos {jogador["nome"]} atuou? -> '))
for j in range(0, total):
    partidas.append(int(input(f'Gols na partida {j} -> ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('Exibições diferentes dos resultados:')
for k, v in jogador.items():
    print(f'A KEY {k} tem o VALUE {v}.')
print('Outra forma...')
for indice, valor in enumerate(jogador['gols']):
    print(f'Na partida {indice} fez {valor} gols.')
print(f"Foi um total de {jogador['total']} gols.")