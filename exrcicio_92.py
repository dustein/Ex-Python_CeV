from datetime import datetime
ficha = {'nome': str(input('Nome -> ')),
'nasc': int(input('Ano de nascimento -> ')),
'ctps': int(input('Número da CTPS (0 se não tiver)-> '))}
if ficha['ctps'] > 0:
    ficha['contrata'] = int(input('Ano de contratação ->'))
    ficha['salario'] = int(input('Salário recebido -> '))
ficha['idade'] = datetime.now().year - ficha['nasc']
ficha['aposenta'] = ficha['contrata'] + 35
print()
print('Cadastro:')
print(f"{ficha['nome']}, CTPS nº {ficha['ctps']}, nasceu em {ficha['nasc']}.\nFoi contratado em {ficha['contrata']}, com um salário de {ficha['salario']}.\nAcha que vai poder se aposentar no ano de {ficha['aposenta']} com idade de {ficha['aposenta'] - ficha['nasc']}.")
