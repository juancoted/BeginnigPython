print('===== DESAFIO 008 =====')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centémetros e milímetros')
# km hm dam m dm cm mm
# 1 metro = 100 centimetros
# 1 metro = 1000 milimetros
centimetros = 100
milimetros = 1000

metro = float(input('Entre com o valor em metros: '))
resultCentimentros = centimetros * metro
resultMilimetros = milimetros * metro

print('Os valores de {} metros em milimetros e centimentros são:  {:.0f} e {:.0f}'.format(metro, resultMilimetros, resultCentimentros))
