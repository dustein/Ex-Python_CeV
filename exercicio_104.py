def leiaInt(pedenum):
    ok = False
    valor = 0
    while True:
        num = str(input(pedenum))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('Apenas número inteiro!')    
        if ok:
            break
    return valor

#programa principal
num = leiaInt('Informe um número inteiro -> ')
print(f'Você escreveu o número {num}.')