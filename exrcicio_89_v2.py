ficha = list()
while True:
    nome = str(input('Nome : '))
    nota1 = int(input('Primeira Nota : '))
    nota2 = int(input('Segunda Nota : '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    print(ficha)
    continua = str(input('Continua? s/n -> '))
    if continua in 'Nn':
        break
print('\n- - - - B O L E T I M - - - -')
print('{:<4}{:<12}{:>10}'.format('Nº', 'NOME', 'RESULTADO'))
for f, a in enumerate(ficha):
    print(f'{f} - {a[0]:_<10} - Nota final -> {a[2]:.2f}')
    #print(f)
    #print(a)
    #print(f'media é {a[2]}')
    #print(f'Notas são {a[1][0]} + {a[1][1]}...')
    #print(f'aluno é {a[0]}')
individual = str(input('Especificar notas de qual aluno (nº). [999 para encerra] -> '))
if individual == 999:
    break
elif individual = f:
    print(f)
