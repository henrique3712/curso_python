"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'

digitos, *_ = cpf.split('-')
primeiros_digitos = digitos.split('.')
primeiros_digitos = ''.join(primeiros_digitos)

novo_valor = []
soma_valor = 0
for i, digito in enumerate(primeiros_digitos):
    num = 10 - i
    novo_valor.append(int(digito) * num)


for j in novo_valor:
    soma_valor += j
print(soma_valor)

multiplica_valor = soma_valor * 10
resto = multiplica_valor % 11
print(resto)

calcula_digito = resto if resto < 10 else 0
print(calcula_digito)
