x = [1, 2, 3, 4, 5]
print(x)

y = int(input('Digite um número para retirar da lista: '))

if y not in x:
    print('Não contém o num na lista')
elif y in x:
    x.remove(y)
    print('O valor foi removido...')
    print(x)


