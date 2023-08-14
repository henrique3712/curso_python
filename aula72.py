# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total

result = multiplica(1, 2, 3, 4, 5)
print(result)



def par_impar(num):
    resp = num % 2 == 0
    if resp:
        return f'{num} é par'
    
    return f'{num} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))