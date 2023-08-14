"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_str = input('Digite um número inteiro: ')

try:
    num_int = int(num_str)
    resto_num = num_int % 2
    if resto_num == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('O número digitado não é um número inteiro')

'''
num_str = input('Digite um número inteiro: ')

if num_str.isdigit():
    num_int = int(num_str)
    resto_num = num_int % 2
    if resto_num == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
else:
    print('O número digitado não é um número inteiro')
'''