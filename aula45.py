"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
"""texto = iter('Luiz')  # __iter__()"""
texto = 'Silva'
iterador = iter(texto)  # iterator

while True:
    try:
        letra = (next(iterador))
        print(letra)
    
    except StopIteration:
        break

texto1 = 'Silva'.lower()

for letra in texto1:
    print(letra)



'''print(texto.__next__())  # __next__()
print(next(texto))
print(next(texto))
print(next(texto))'''