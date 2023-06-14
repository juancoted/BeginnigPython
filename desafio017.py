print('===== DESAFIO 017 =====')
print('Crie um programa que leia o comprimeiro do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule')
print('e mostre o comprimento da hipotenusa.')

'''
co = float(input('Entre com o comprimento do cateto oposto: '))
ca = float(input('Entre com o comprimento do cateto adjacente:'))
hp = (co ** 2 + ca ** 2) ** (1/2)

print('A soma do cateto oposto {} mais o cateto adjancente {} é igual a hipotenusa {:.2f} '.format(co, ca, hp))'''

import math
co = float(input('Entre com o comprimento do cateto oposto: '))
ca = float(input('Entre com o comprimento do cateto adjacente:'))
hp = math.hypot(co,ca)

print('A hipotenusa vai medir {:.2f}'.format(hp))