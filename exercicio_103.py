def ficha(n = "'n/i", g=0):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
            
    print(f'{n} teve {g} marcados nesta temporada.')
    

#Programa principal
nome = str(input('Nome do jogador -> '))
gols = str(input('Quantos gols marcados -> '))
ficha(nome, gols)