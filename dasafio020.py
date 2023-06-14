print('===== DESAFIO 020 =====')
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos aluno.')
print('Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

import random
list = ['Juan', 'Renan', 'Rafael', 'Luiz']
random.shuffle(list)
print('A nova ordem é: {}'.format(list))

for i in list:
    sorteado = random.choice(list)
    print(sorteado)

