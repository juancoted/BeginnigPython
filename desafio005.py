print('===== DESAFIO 005 =====')
print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor')

number = int(input('Entre com um número inteiro: '))
previews = number - 1
next = number + 1
print('Seu número foi {} e seu antecessor é {} e seu sucessor é {}'.format(number, previews, next))
#ou .format(number,(previwes -1), (next + 1)
