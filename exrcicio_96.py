def area(larg, comp):
    a =larg * comp
    print(f'A área de um terreo de largura {larg:.2f} e comprimento {comp:.2f} é {a:.2f}m2.')


#Programa principal
print('*' * 5, 'Área', '*' * 5)
lado1 = float(input('Medida do 1º lado -> '))
lado2 = float(input('Medida do 2º lado -> '))
(area(lado1, lado2))
