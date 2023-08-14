"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#........0...1...2...3
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append('Henrique')
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
lista.append(1233)
print(lista)
del lista[-1]
#lista.clear()
print(lista)
lista.insert(0, 5)
print(lista)