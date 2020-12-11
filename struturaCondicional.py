#ESTRUTURA CONDICIONAL IF ELSE

nota = int(input('Digite sua nota: '))
if nota >= 5 and nota <=10:
    print('Você tirou {}!!!'.format(nota))
    print('Parabéns, você foi aprovado')
elif nota < 5:
     print('Você tirou {}'.format(nota))
     print('Você está de prova final!!!')


recuperacao = int(input('Digite a nota da recuperação: '))
if recuperacao == 5:
    print('Você tirou {}'.format(recuperacao))
    print('Parabéns, você aprovado!!!')
elif recuperacao < 5:
    print('Você tirou {}'.format(recuperacao))
    print('Você foi reprovado!!!')
