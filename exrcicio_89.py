alunos = list()
temp = list()
while True:
    temp.append(str(input('Nome : ')))
    temp.append(int(input('Nota 1 : ')))
    temp.append(int(input('Nota 2 : ')))
    alunos.append(temp[:])
    temp.clear()
    continua = str(input('Continua? s/n -> '))
    if continua in 'Nn':
        break
print()
print('_-_' * 5, 'Boletim', '_-_' * 5)
print()
for a, n in enumerate(alunos):
    print(f'{a} - {alunos[a][0]:<10} - Nota <{alunos[a][1]}> e <{alunos[a][2]}> | Média {(alunos[a][1]/alunos[a][2])/2:.2f}')
print('_-_' * 12)
while True:
    exibe = int(input('Exibir notas de algum aluno? (999) para encerrar - > '))
    if exibe == 999:
        break
    elif exibe == alunos[0]:
        print(f'{a} tirou notas {alunos[a][1]} e {alunos[a][2]}.')
              
print('Encerrado.')