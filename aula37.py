"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1 

    if contador == 6:
        print('Não vou mostrar o ', contador)
        continue

    if contador >= 11 and contador <= 29:
        if contador == 11:
            print('Não vou mostrar do 11 ao 29')
        continue
    
    print(contador)    

    if contador == 40:
        break


print('Acabou')