"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
'''nome = 'Luiz'
noutra_variavel = nome
nome = 'João'
print(nome)
print(noutra_variavel)'''

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a  # toda alteração na lista_a acontece na lista_b

lista_a.pop()

print(lista_a)
print(lista_b)

lista_b = lista_a.copy()  # Faz uma copia dos valores da lista_a na lista_b
                          # se houver alteração na lista_a não interfere na lista_b
lista_a.append(1.2)

print(lista_a)
print(lista_b)

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)