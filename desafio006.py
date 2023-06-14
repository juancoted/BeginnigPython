print('===== DESAFIO 006 =====')
print('Crie um algoritimo que leia um número e mostre o seu dobro triplo e raiz quadrada')

number = int(input('Entre com um número: '))
double = number * 2
triple = number * 3
raiz = number ** (1/2)
print('O dobro do número {} é {} e o triplo é {} e a sua raiz é {:.2f} '.format(number, double, triple, raiz))
