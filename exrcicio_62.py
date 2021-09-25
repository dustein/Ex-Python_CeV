print('*-*' * 10)
print('{:^30}'.format('Progressão Aritimética'))
print('*-*' * 10)
print('Informe o Primeiro Termo e a razão para resultado da Progressão Aritimética. \nPara encerrar informe (0).')
primeiro = int(input('Primeiro termo -> '))
razao = int(input('Razão -> '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Exibir mais quantos resultados? '))
print('Finalizado com {} resulados'.format(count))

