def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'Com idade de {idade} não pode votar...')
    elif idade >= 18:
        print(f'Tem {idade} anos. Voto OBRIGATÓRIO')
    else:
        print(f'Voto facultativo, você tem {idade} anos.')

#printicpal
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
