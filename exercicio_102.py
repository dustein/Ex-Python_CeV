def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f = f * c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            if c == 1:
                print(f'{c} = ', end='')

    print(f'O fatorial de {n} é {f}.')

#principal
fatorial(5, show=True)