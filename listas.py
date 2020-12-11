"""
    append
    insert(0, 'x)
    pop(1)
    remove('x)
    len()
    sort()
    reverse

    max()
    min()
    sum()


"""
# MONTANDO UMA LISTA(VETOR)

lista = [1, 5, 6]
lista.append(18)# a função append() irá adicionar o numero 18 na última posição da minha lista(vetor)
print(lista)

lista.insert(3, 'Lanes Rocha')# a função insert irá adicionar a string na posição 3 da lista(vetor)
print(lista)

lista.pop() # a função pop() retira as informações da última posição
lista.pop(2)
print(lista)

lista.remove('Lanes Rocha')# a função remove apaga a informação na minha lista
print(lista)

print(len(lista))# a função lista imprimi a qnt de ítens na minha lista

ordenacao = [6,5,7,8,9,1,0]
ordenacao.sort()# a função sort() ordena em ordem crescente os itens na minha lista
print(ordenacao)

ordenacao.sort(reverse=True) # com o parêmentro reverse=True ordena em ordem decrescente
print(ordenacao)

str = ['rocha', 'lanes']
str.reverse()# a função reverse inverte os itens nas posicoes da minha lista
print(str)

n = [1, 2, 3, 4 , 5]
print(max(n))# a função max() mostra o maior número dentro do vetor
print(min(n))# a função max() mostra o menor número dentro do vetor
print(sum(n))# a função sum() soma todos os ítens do vetor