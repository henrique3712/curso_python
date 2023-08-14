"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

tam_nome = len(nome)
conta_letra = 0
nova_string = ''

while conta_letra < tam_nome:
    nova_string += f'*{nome[conta_letra]}'
    conta_letra += 1

print(nova_string)