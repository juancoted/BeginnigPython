print('===== DESAFIO 007 =====')
print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média')

note1 = float(input('Entre com a primeira nota: '))
note2 = float(input('Entre com a segunda nota: '))

media = (note1 + note2)/2

print('Sua média é: {:.1f}'.format(media))