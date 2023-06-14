print('===== DESAFIO 019 =====')
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,')
print('lendo o nome deles e escrevendo o nome do escolhido')

aluno1 = str(input('Entre com o nome do 1° aluno: '))
aluno2 = str(input('Entre com o nome do 2° aluno: '))
aluno3 = str(input('Entre com o nome do 3° aluno: '))
aluno4 = str(input('Entre com o nome do 4° aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

import random

escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))