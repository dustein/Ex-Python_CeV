print('Fibonacci')
a = 0
b = 1
count = 3
total = int(input('Quantas posições da cadeia deseja exibir? '))
print('{} -> {} -> '.format(a, b), end='')
while count <= total:
    c = a + b
    count = count + 1
    a = b
    b = c
    print('{} -> '.format(c), end='')
print('FIM!')
