print('Média de todos os valores, qual o maior, qual o menor.')
continua = 'S'
contador = acumulador = maior = menor = 0
while continua in 'Ss':
    numero = int(input('Digite um número -> '))
    continua = str(input('\033[33mContinua (S/N)? -> \033[m'))
    if contador == 0:
        maior = menor = numero
    elif contador > 0:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    contador += 1
    acumulador += numero
print('Foram {} número digitados, num valor total de {}, que dá uma média de {}'.format(contador, acumulador, acumulador/contador))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format (menor))
print('FIM!')