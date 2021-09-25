print('Informe números inteiros conforme quiser. Para parar informe "999".')
count = soma = 0
n = int(input('Número -> '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Numero-> '))
print('FIM, a soma de todos os {} números é {}'.format(count, soma))
