"""
    TIPOS DE ERROS
        - Sintático
            Significa digitar algum código errado.
            ex.: correto - print(), errado: prit()

        - Léxico
            Siginifica digitar um comando invertido por mais que o mesmo esteja certo
            ex.: correto - print('Olá Mundo!!!'), errado - ('Olá mundo!!!')print

        - Semântico
            Siginifica um erro de lógica dentro da sua aplicação.
            ex.: correto int = 33, errado int = 33.0
            ex.: correto
                 try:
                    x = int(input('Digite sua idade: '))
                 except:
                 print('Digite sua idade corretamente!!!')

                 errado
                 x = int(input('Digite sua idade: ')) #não houve tratamento na lógica
                 print(x)

"""


try:
    x = int(input('Digite sua idade: '))#Este campo aceitará apenas números, caso digita uma string irá imprimir a mensagem e fechar o programa
except:
    print('Digite sua idade corretamente!!!')
else:
    print(f'A idade digitada: {x}')
finally:
    print()
    print('Programa encerrado!!!')