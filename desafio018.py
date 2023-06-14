print('===== DESAFIO 018 =====')
print('Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo')
'''
sen = cateto oposto / hipotenusa
cos = cateto adjacente / hipotenusa
tan = cateto oposto / cateto adjacente
'''

import math

num = float(input('Entre com o ângulo que precisa calcular: '))

print('O cosseno e a tangente do ângulo {}° são: {:.2f} e {:.2f}'.format(num, math.cos(num), math.tan(num)))
