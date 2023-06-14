print('===== DESAFIO 009 =====')
print('Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada')

numbers = int(input('Entre com o número: '))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list:
    result = i * numbers
    print('{} x {:2} = {}'.format(numbers, i, result))
