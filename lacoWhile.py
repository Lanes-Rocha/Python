#ESTRUTURA DE REPETIÇÃO WHILE
while True:
    print('1 - Entrar com os dados\n'
          '2 - Imprimir os dados\n'
          '0 - sair\n'
          )
    opcao = int(input('Digite sua opção: '))

    if(opcao == 1):
        nome = input('Digite seu nome: ')
        idade = input("Digite sua idade: ")
        sexo = input('M - Masculino, F - Feminino: ')
        escolaridade = input('Digite sua Formação: ')
    if(opcao == 2):
        print(nome)
        print(idade)
        print('Seu sexo é: {}'.format(sexo))
        print()
    if(opcao == 0):
        print('Programa encerrado!!!')
    break








