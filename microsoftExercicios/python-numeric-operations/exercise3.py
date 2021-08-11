# first_value = 5
# second_value = 4
#
# sum = first_value + second_value
# difference = first_value - second_value
# product = first_value * second_value
# quotient = first_value / second_value
# modulus = first_value % second_value
# exponent = first_value ** second_value
#
# print('Sum: ' + str(sum))
# print('Difference: ' + str(difference))
# print('Product: ' + str(product))
# print('Quotient: ' + str(quotient))
# print('Modulus: ' + str(modulus))
# print('Exponent: ' + str(exponent))

# O Python segue o acrônimo PEMDAS, que indica a ordem na qual as operações devem ser executadas.
#
# P arênteses: resolva primeiro as operações entre parênteses.
# E xponentes: resolva os expoentes.
# M ultiplicação: resolva a multiplicação, da esquerda para a direita.
# D ivisão: resolva a divisão, da esquerda para a direita.
# A dição: resolva a adição, da esquerda para a direita.
# S ubtração: resolva a subtração, da esquerda para a direita.

# print(3 + 4 * 5)
# print((3 + 4) * 5)

# first_value = 5
# second_value = 4
#
# quotient = first_value / second_value
#
# print(type(quotient))
# print(quotient)

# Ao converter um valor float em um valor int, você precisará estar ciente do truncamento.

# pi = 3.14
# print(type(pi))
# print(int(pi))
#
# uptime = 99.99
# print(type(uptime))
# print(int(uptime))

# Como você pode ver no caso da variável chamada uptime, apenas usar a função int() faz com que os valores após o decimal sejam removidos, em vez de arredondar o valor inteiro para o próximo número inteiro (100).
#
# Para evitar o truncamento, use a função round() interna. Atualize o código que você escreveu nesta etapa para incluir uma chamada à função round(). O código deverá corresponder ao seguinte:


# pi = 3.14
# print(type(pi))
# print(int(pi))
# print(round(pi))
#
# uptime = 99.99
# print(type(uptime))
# print(int(uptime))
# print(round(uptime))

# código que faz o arredondamento para uma casa decimal específica

# first_value = round(7.654321, 2)
# print(first_value)
#
# second_value = round(9.87654, 3)
# print(second_value)

