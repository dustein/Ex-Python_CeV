time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador -> '))
    total = int(input(f'Partidas jogadas por {jogador["nome"]} -> '))
    for p in range(0, total):
        partidas.append(int(input(f'Gols no {p+1}º jogo -> ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    jogador.clear()
    
    while True:
        continua = str(input('Continua? S/N -> '))
        if continua in 'NnSs':
            break
        print('Respoda apenas S ou N !')
    if continua in 'Nn':
        break
print('-|-' * 20)
#print('cod ', end='') # só decoração da aparência escrevendo a coluna codigo do jogador
for i in jogador.keys(): # para cada elemento das chaves de jogador
    print(f'{i:<15}') # mostre o nome da chave 
for k, v in enumerate(time): #para a chave k e o valor v
    print(f'{k:<4}', end='')
    for d in v.values(): # para cada dado d bos valores v 
         print(f'{str(d):<15}', end='') # para cada STRING dos valores... vai pegar o que for STRING e não pegar o que for INTEIRO etc
    print() 

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar) -> '))
    if busca == 999:
        break
    if busca >= len(time): #se o pedido na busca for maior que o tamanho do time
        print(f'ERRO! Não existe jogador com o código {busca}.') 
    else:
        print(f'MAIS DADOS SOBRE O JOGADOR {time[busca]["nome"]}:') #o nome do jogador está dentro de time, que tem um indice numerico que é o indice da busca, e dentro tem outro elemento que é o nome gravado no dicionário
        for i, g in enumerate(time[busca]["gols"]): # para o indice, a quantidade de gols de time na busca do campo gols
            print(f'     > No jogo {i+1} fez {g} gols.')
    print('#' * 20)
print()
print('PROGRAMA ENCERRADO PELO USUÁRIO')
