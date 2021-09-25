c = ('\033[m', # 0-sem cor
'\033[0;30;41m', # 1-vermelho
'\033[0;30;42m', # 2-verde
'\033[0;30;43m', # 3-amarelo
'\033[0;30;44m', # 4-azul
'\033[0;30;45m', # 5-roxo
'\033[7;30m') # 6-branco

def ajuda(comando):
    titulo(f'Acesando o manual do comando \'{comando}\'', 4) # {comando} está entre barras \ \ para 'escapar'. Não entendi, pesuqisar.
    print(c[6], end='')
    help(comando)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('#' * tam)
    print(f'  {msg}')
    print('#' * tam)
    print(c[0], end='')

#principal
comando = ''
while True:
    titulo('Sistema de Ajuda - PyHelp !', 3)
    comando = str(input('Help sobre Função ou Biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FINALIZADO.', 1)
