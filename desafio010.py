print('===== DESAFIO 010 =====')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar')
print('Considere US$1,00 = R$3.27')
dolar = 4.49
real = float(input('Quanto você tem em reais: '))

if real >= 4.49:
    podeComprar = real / dolar
    print('Você pode comprar até {:.2f}'.format(podeComprar))
else:
    print('Não é possível comprar Dolar!')

