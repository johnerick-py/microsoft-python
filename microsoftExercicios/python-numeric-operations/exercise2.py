
# numeric_value = '7'
# print(numeric_value.isnumeric())
#
# string_value = 'Bob'
# print(string_value.isnumeric())

# Outras funções is__()
# O tipo de dados str do Python dá suporte a muitas funções auxiliares semelhantes. Como você está começando, algumas das mais úteis incluem:
#
# OUTRAS FUNÇÕES IS__()
# Função	Finalidade
# isalnum()	Verifica se a cadeia de caracteres não tem caracteres especiais, como %, $, #, @ ou !.
# isalpha()	Verifica se a cadeia de caracteres contém apenas letras do alfabeto.
# isdecimal()	Verifica se a cadeia de caracteres contém apenas valores decimais (números).
# istitle()	Verifica se a cadeia de caracteres segue as regras de uso de maiúsculas (como em uma frase).
# isupper()	Verifica se a cadeia de caracteres contém apenas letras maiúsculas.
# islower()	Verifica se a cadeia de caracteres contém apenas letras minúsculas.
#
# first_value = input('First Number: ')
#
# if first_value.isnumeric() == False:
#     print('Value is not a number.')
#     exit()
#
# second_value = input('Second Number: ')
#
# if second_value.isnumeric() == False:
#     print('Value is not a number.')
#     exit()
#
# first_value = int(first_value)
# second_value = int(second_value)
#
# sum = first_value + second_value
# print('Sum: ' + str(sum))


# Etapa 4 – Atualizar o exemplo de código para usar o operador lógico or

# first_value = input('First Number: ')
# second_value = input('Second Number: ')
#
# if first_value.isnumeric() == False or second_value.isnumeric() == False:
#     print('Please enter numbers only.')
#     exit()
#
# first_value = int(first_value)
# second_value = int(second_value)
#
# sum = first_value + second_value
# print('Sum: ' + str(sum))

