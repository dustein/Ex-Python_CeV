print('-|-' * 20)
print('-|-' * 20)
print('{:^60}'.format('Pesos e Pesos'))
print('-|-' * 20)
print('-|-' * 20)
maior = 0
menor = 0
for pessoa in range (1, 6):
    peso = float(input('Peso da pessoa {}-> '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} Kg, o menor de {} Kg'.format(maior, menor))
