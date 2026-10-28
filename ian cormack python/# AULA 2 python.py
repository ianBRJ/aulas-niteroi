# AULA 2 python
'''
salario = input('Diga seu slário')

print('salário: R$' , salario)

texto = input("valor: ")
valor = float(texto.replace(",","."))
print(valor)
'''
'''
entrada = int(input("entrada: "))
saida = int(input("gastos: "))
saldo = entrada - saida


if saldo > 0:
    print("sobrou")
elif saldo == 0:
    print('zero à zero')
else:
    print('vamos economizar! \nVc gastou muito')

'''

salario = float(input('Salário do mes: ').replace(",","."))
extra = float(input('Renda extra do mes: ').replace(",","."))
mercado = float(input('Gastos com mercado: ').replace(",","."))
transporte = float(input('Gastos com transporte: ').replace(",","."))

entrada = salario + extra
saida = mercado + transporte
saldo = entrada - saida

if saldo > 0:
    print("Parabéns, sobrou dinheiro esse mes")
elif saldo == 0:
    print('Ufa, zero à zero')
else:
    print('Vamos economizar! \nVc gastou muito esse mes')