"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

num_nome = nome.isalpha()


if num_nome == True:
    tam_nome = len(nome)

    if tam_nome <= 4:
        print('Seu nome é curto')
    elif tam_nome >= 5 and tam_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Nome Inválido')
