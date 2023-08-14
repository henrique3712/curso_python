"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf = '702923106'

nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
resultado1 = 0
lista_resultado1 = []
for i, digito_1 in enumerate(nove_digitos):
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    resultado1 = int(digito_1) * contador_regressivo_1
    lista_resultado1.append(resultado1)
    print(f'{int(digito_1)} * {contador_regressivo_1} = {resultado1}')
    contador_regressivo_1 -= 1

print()
print(*lista_resultado1, sep=' + ', end=' = ')
print(resultado_digito_1)
print(f'{resultado_digito_1} * 10 = {resultado_digito_1 * 10}')
resto = (resultado_digito_1 * 10) % 11
print(f'{(resultado_digito_1 * 10)} % 11 = {resto}')

ultimo_digito = resto if resto < 10 else 0
print(f'Décimo dígito: {ultimo_digito}\n')

novo_digito = nove_digitos + str(ultimo_digito)
print(novo_digito, end='\n\n')

contador_regressivo_2 = 11

resultado_digito_2 = 0
resultado2 = 0
lista_resultado2 = []
for j, digito_2 in enumerate(novo_digito):
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    resultado2 = int(digito_2) * contador_regressivo_2
    lista_resultado2.append(resultado2)
    print(f'{int(digito_2)} * {contador_regressivo_2} = {resultado2}')
    contador_regressivo_2 -= 1

print()
print(*lista_resultado2, sep=' + ', end=' = ')
print(resultado_digito_2)
print(f'{resultado_digito_2} * 10 = {resultado_digito_2 * 10}')
resto = (resultado_digito_2 * 10) % 11
print(f'{(resultado_digito_2 * 10)} % 11 = {resto}')

ultimo_digito = resto if resto < 10 else 0
print(f'Último dígito: {ultimo_digito}\n')

novo_cpf = novo_digito + str(ultimo_digito)
print(novo_cpf)