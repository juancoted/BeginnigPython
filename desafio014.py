print('===== DESAFIO 014 =====')
print('Crie um programa que leia um valor em Celsius e converta em Fahrenheit: ')
#Formula é: 0°C * (9/5) + 32 =  32°F
gc = float(input('Entre com a temperatuda em Celsius: '))
gf = gc * (9 / 5) + 32
print('A conversão de {}°C para Fahrenheit é: {}°F'.format(gc, gf))
