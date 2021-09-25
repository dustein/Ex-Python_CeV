cadastros = list()
pessoa = dict()
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome -> '))
    while True:
        pessoa['sexo'] = str(input('Sexo M/F -> ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Favor informar apenas M ou F.')
    pessoa['idade'] = int(input('Idade -> '))
    somaidade += pessoa['idade']
    cadastros.append(pessoa.copy())
    continua = str(input('Continua? s/n -> ')).upper()
    if continua == 'N':
        break
print(cadastros)
print(f'Foram {len(cadastros)} pessoas cadastradas.')
print(f'A média das idades é {somaidade/2:.0f}.')
