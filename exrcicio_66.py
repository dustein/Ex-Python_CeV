print('Números, total deles e soma. Para parar, 999')
n = conta = soma = 0
while n != 999:
    n = int(input('Informe número : '))
    if n == 999:
        break
    conta += 1
    soma += n
print(f'Foram informados {conta} números, com um somatório total de {soma}.')
