# mana_jogador = 5
# mana_invocar = int(input('Qual o custo de mana?: '))
#
# if mana_invocar <= mana_jogador:
#     mana_jogador = mana_jogador - mana_invocar
#     print('Pode invocar a carta')
# else:
#     print('Sua mana atual é {}, você não tem mana suficiente'.format(mana_jogador))
#
# print('sua mana atual é {}'.format(mana_jogador))

# print('informe o tipo da carta que você deseja buscar: ',
#       '(1) Druida',
#       '(2) Caçador',
#       '(3) Mago',
#       '(4) Paladino',
#       '(5) Xamã')
#
# tipoCarta = input('Digite um número: ')
#
# if tipoCarta == '1':
#     tipoCarta = 'Druida'
# elif tipoCarta == '2':
#     tipoCarta == 'Caçador'
# elif tipoCarta == '3':
#     tipoCarta = 'Mago'
# elif tipoCarta == '4':
#     tipoCarta = 'Paladino'
# elif tipoCarta == '5':
#     tipoCarta = 'Xamã'
# else:
#     print('Erro, nenhum tipo correspondente!')
#
# print('Você escolheu o tipo {}'.format(tipoCarta))


# pokedex = ['Charmander', 'Bulbasauro', 'squirtler', 'Butterfly', 'Pikachu']
#
# print(pokedex[0])
# print(len(pokedex))
# a,b = 0, 1
# while b < 10:
#     print(b)
#     a,b = b, a+b
#
# from threading import Thread
# minha_lista = []
# def funcao():
#     for i in range(100000):
#         minha_lista.append(1)
#     for i in range(100000):
#         minha_lista.pop()
# if __name__ == '__main__':
#     tarefas = []
#     for indice in range(10):
#         tarefa = Thread(target=funcao)
#         tarefas.append(tarefa)
#         tarefa.start()
#
#         print(len(minha_lista))
#         for tarefa in tarefas:
#             tarefa.join()
#         print(len(minha_lista))

# lista = ["cachorro", "hamster", ["pato", "galinha", "porco"], "gato"]
# print(lista[3][2])

# def dobra(y):
#     x = y + y
#     return x
# x = 5
# dobra(x)
# dobra(x)
# print(x)

# x = [2,9,1,5]
# i = 1
# j = 2
# i, x[i] = j * 2 - x[j] ** 2, 0
# print(x)
# a = 1
# while a < 10:
#     if a % 2 == 0:
#         break
#     else:
#         a += 1
# print(a)

from flask import Flask, request

app = Flask(__name__)
@app.route('/teste', methods=['POST'])
def teste_post():
    if request.method == 'POST':
        return "Requisição POST"
    else:
        return "Requesição GET"

if __name__ == '__main__':
    app.run()