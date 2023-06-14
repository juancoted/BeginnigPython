print('===== DESAFIO 004 =====')
print('Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas '
      'as informações possíveis sobre ela')

valor = input('Entre com algum valor no teclado: ')
print('é um número: ', valor.isnumeric())
print('É um número AlphaNumerico: ', valor.isalnum())
print(valor.isalpha())
print(valor.isascii())
print(valor.isdigit())
print(valor.isdecimal())
print(valor.isidentifier())
print(valor.islower())
print(valor.isprintable())
print('Só tem espaços: ', valor.isspace())
print(valor.istitle())
print(valor.isupper())
print(valor.__init_subclass__())


