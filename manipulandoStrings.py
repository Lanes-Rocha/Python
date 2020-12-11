"""
    FUNÇÕES PARA MANIPULAR STRINGS

    upper()
    lower()
    len()
    replace('str', 'str')
    count('str')
    find('str')
    title()
"""

nome = 'lanes lopes rocha'
nome = nome.upper() # A função upper() deixa todos os caracteres maiúsculos
print(nome)

nome1 = 'LANES LOPES ROCHA'
nome1 = nome1.lower()# A função lower() deixa todos os caracteres minúsculos
print(nome1)

str = 'lanes lopes rocha'
str = str.title()# A função title() deixa todos os primeiros caracteres de cada palavra em maiúsculo
print(str)

str2 = 'Lanes'
print(len(str2))# A função len() conta a quantidade de caracteres em uma string, conta espaços também

nomecomleto = 'Lanes Lopes'
nomecomleto = nomecomleto.replace('Lopes', 'Rocha')
print(nomecomleto)

letras = 'cccc eeee dddd ddddd efffff'
print(letras.count('d'))# A função count é utilizada para contar quantas vezes um letra aparece na string

pesquisaposicao = 'Lanes Rocha'
pesquisaposicao = pesquisaposicao.find('a')# A função find() irá pesquisar a posição do caracter apenas até a primeira letra encontrada
#A string Lanes Rocha a letra a apesar de aparecer duas vzs o find() irá mostrar a posição apenas do primeiro a
print(pesquisaposicao)