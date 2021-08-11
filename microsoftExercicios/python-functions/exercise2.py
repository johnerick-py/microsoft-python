# def print_args(*args):
#   for arg in args:
#     print(f'arg = {arg}')
#
# print_args('a')
# print_args('a', 'b')
# print_args('a', 'b', 'c')

# def print_args(*args):
#   #for arg in args:
#   #  print(f'arg = {arg}')
#   print(args)
#   print(type(args))
#
# print_args('a')
# print_args('a', 'b')
# print_args('a', 'b', 'c')

# Uma lista de argumentos arbitrários não é do tipo list, mas sim do tipo tuple.
#
# O que é uma tupla? De maneira resumida, é semelhante a uma lista, mas com algumas diferenças.
# A diferença mais notável é que não é possível modificar o conteúdo de uma tupla.
# No exemplo de código atual, a função não pode chamar append() ou remove(), chamar sort() ou reverse(),
# nem atribuir um novo valor a um elemento.

# def print_keyword_args(**kwargs):
#
#   third = kwargs.get('third', None)
#   if third != None:
#     print('third arg =', third)
#
#
# print_keyword_args(first='a')
# print_keyword_args(first='b', second='c')
# print_keyword_args(first='d', second='e', third='f')

# Nesse caso, o código chama a função print_keyword_args() três vezes.
# A cada vez, ele passa em um ou mais argumentos de palavra-chave, como first='a'.
# O corpo da função pode acessar um argumento existente específico usando o método kwargs.get().
#
# Cada chamada para kwargs.get() passa um nome e um valor padrão.
# No exemplo atual, a função procura uma palavra-chave chamada 'third'.
# Se 'third' não existir em kwargs, a variável third será definida como o valor padrão None.
#
# Ao executar o código, você deverá ver a seguinte saída:


# def print_keyword_args(**kwargs):
#
#   print('\n')
#
#   for key, value in kwargs.items():
#     print(f'{key} = {value}')
#
#   third = kwargs.get('third', None)
#   if third != None:
#     print('third arg =', third)
#
#
# print_keyword_args(first='a')
# print_keyword_args(first='b', second='c')
# print_keyword_args(first='d', second='e', third='f')