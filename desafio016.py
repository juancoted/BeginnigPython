print('===== DESAFIO 016 =====')
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira')
# Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

'''
    from math import trunc
    num = float(input('Digite um valor: '))
    print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))