print('===== DESAFIO 015 =====')
print('Crie um programa que pergunte a quantidade de KM percorridos por um carro e a quantidade de dias pelos quais ele foi alugado.')
print('Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.')

diasAlugado = int(input('Total de dias alugado(s): '))
kmPercorrido = float(input('Entre com  a quantidade de KM percorrido: '))


precoApagar = (kmPercorrido * 0.15) + (diasAlugado * 60)

print('O valor de suas despesas foi: R${:.2f}'.format(precoApagar))
