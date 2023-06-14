print('===== DESAFIO 007 =====')
print('Faça um programa que leia a largura e a altura da parede em metros, calcule a sua área e a quantidade ', end='')
print('de tinta necessária para pintá=la, sabendo que cada tinta, pinta uma área de 2m².')

largura = float(input('Entre com a largura da sua parede: '))
altura = float(input('Entre com a altura da sua parede: '))

area = largura * altura
tinta = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m2.'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))