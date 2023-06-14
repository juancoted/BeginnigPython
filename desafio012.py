print('===== DESAFIO 012 =====')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto')

preco = float(input('Entre com  o valor do seu produto: '))
precoDesconto = preco - (preco * 5/100)

print('O valor com o desconto de 5% é: {:.2f}'.format(precoDesconto))