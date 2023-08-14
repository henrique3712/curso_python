'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista 
não permita que o programa quebre com
erros de indices inexistentes na lista.
'''
import os

lista = []
while True:
       
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    os.system('clear')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_a_apagar = input('Escolha o índice para apagar: ')
        try:
            indice_a_apagar = int(indice_a_apagar)
            lista.pop(indice_a_apagar)
        except (IndexError, ValueError):
            print('Esse indice não existe.')

    elif opcao == 'l':
        if bool(lista) is False:
            print('Não há nada para listar.')

        for indice, item in enumerate(lista):
            print(indice, item)

    else:
        print('Opção Inválida.')
