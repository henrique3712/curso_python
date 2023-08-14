
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
num_tentativas = 0

while True:
    num_tentativas += 1
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    nova_palavra = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            nova_palavra += letra_secreta
        else:
            nova_palavra += '*'
        
    print(nova_palavra)

    if nova_palavra == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!!! PARABÉNS!!!')
        print(f'A palavra secreta era "{palavra_secreta}"')
        print('Tentativas:', num_tentativas)
        break

    





    
   





    