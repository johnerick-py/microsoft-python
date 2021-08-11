# def say_hello():
#   print('Hello World!')
#
# say_hello()

# def say_hello(name):
#   print(f'Hello {name}!')
#
# say_hello('Bob')

# def say_hello(name='World', greeting=None):
#   if greeting == None:
#     print(f'Hello {name}!')
#   else:
#     print(f'{greeting} {name}!')
#
# say_hello()
# say_hello('Bob')
# say_hello(greeting='Howdy')
# say_hello('Bob', 'Howdy')

# Etapa 6 – Comentar o código das etapas anteriores e adicionar uma nova função que retorna um valor

# def add_two_numbers(x, y):
#   return x + y
#
#
# add_two_numbers(4, 6)
# result = add_two_numbers(5, 7)
# print(result)

# Etapa 7 – Comentar o código das etapas anteriores e adicionar uma nova função que retorna uma lista

# def create_deck():
#   suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
#   ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#   deck = []
#
#   for  suit in suits:
#     for rank in ranks:
#       deck.append(f'{rank} of {suit}')
#
#   return deck
#
# my_deck = create_deck()
# print(len(my_deck))

# value = 1
#
# def some_function():
#     value = 10
#     return value
#
# print(value)
# some_function()
# print(value)
