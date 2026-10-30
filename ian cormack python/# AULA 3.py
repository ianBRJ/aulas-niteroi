# AULA 3
'''
ganhos = []
ganhos.append(["venda de doces",150])
ganhos.append(["servico extra", 50])

ganhos = ['venda de salgados', 120]

print(ganhos[0])
'''

print('=== MEU DINHEIRO NA TELA===')
salario = float(input('Salário do mes (R$): ').replace(',','.'))
ganhos=[]
gastos=[]

while True:
    print('\n1 - Adicionar renda extra ' \
    '\n2 - Adicionar gasto ' \
    '\n3 - Ver saldo ' \
    '\n0 - Sair')
    opcao = input('Escolha uma opção ')

    if opcao == '1':
        descricao = input('De onde veio o dinheiro? ')
        valor = float(input('valor (R$): ').replace(',','.'))
        ganhos.append([descricao, valor])
        print('Renda extra anotada!')

            
    elif opcao == '2':
        descricao = input('Qual foi o gasto? ')
        valor = float(input('valor (R$): ').replace(',','.'))
        gastos.append([descricao, valor])
        print('Gasto anotado!')

    elif opcao == '3':
         entradas = salario
         for ganho in ganhos:
              entradas = entradas + ganho[1]

         saidas = 0
         for gasto in gastos:
            saidas = saidas + gasto[1]

         print('Entradas: R$', entradas, '\nGastos: R$', saidas, "\nSaldo: R$", entradas - saidas)

    elif opcao == '0':
        print('Até a próxima!')
        break

    else:
         print('Opção inválida. Tente outra vez.')
