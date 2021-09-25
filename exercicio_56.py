print('#' * 60)
print('{:^60}'.format('E s t a t í s t i c a'))
print('#' * 60)
print('Informe os dados sobre as quatro pessoas para análise.\nSerá gerada a estatística:')
media = 0
mulheres = 0
mulherjovem = 0
idadevelho = 0
nomevelho = ''
for pessoas in range (1, 5):
    print('\033[34m*** Dados da {}ª pessoa ***\033[m'.format(pessoas))
    nome = str(input('Nome -> ')).strip()
    idade = int(input('Idade -> '))
    sexo = str(input('Sexo [M]/[F] -> ')).strip()
    media = media + idade
    if pessoas == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        nomevelho = nome
    if sexo in 'Ff':
        mulheres += 1
    if idade < 20:
        mulherjovem += 1
print('A idade média dos participantes da pesquisa é de {:.1f}'.format(media / 4))
print('Foram contabilizadas {} mulheres, sendo {} com idade abaixo de 20 anos.'.format(mulheres, mulherjovem))
print('O homem mais velho se chama {}'.format(nomevelho))

