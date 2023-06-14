print('===== DESAFIO 013 =====')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento')

salario = float(input('Entre com  o valor do seu salário: '))
novoSalario = salario + (salario * 15/100)

print('Seu salário atual é de: R${:.2f} com os 15% de aumento.'.format(novoSalario))
