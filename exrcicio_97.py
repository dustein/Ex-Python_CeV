def contar(ini, fim, passo):
    contagem = list()
    for c in range(ini, fim+1):
        contagem.append(c)
    print(contagem[::passo])

#Programa principal
contar(0, 10, 3)
i = int(input('Início da contagem -> '))
f = int(input('Fim da contagem -> '))
p = int(input('Passo -> '))
contar(i, f, p)