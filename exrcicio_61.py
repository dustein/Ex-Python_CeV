print('*' * 22)
print('Progressão Aritimética')
print('*' * 22)
fase = 0
pa = 0
ra = 0
inicio = int(input('\nValor inicial -> '))
ra = int(input('Razão -> '))
while fase < 10:
    fase += 1
    if fase == 1:
        pa = inicio
    else:
        pa += ra
        
    print(pa, '-- ', end='')
    print('FIM')
        