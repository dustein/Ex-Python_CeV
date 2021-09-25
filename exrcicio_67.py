print('Tabuada')
print('Quer ver a tabuada de qual número?')
while True:
    n = int(input('Número -> '))
    if n == 0:
        break
    for tab in range (1, 11):
        print(f'{n} x {tab} = {n * tab}')
print('Finalizado')