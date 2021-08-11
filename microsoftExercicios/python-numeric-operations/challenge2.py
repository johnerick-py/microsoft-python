first_number = input('First number?')
operation = input('Operation?')
second_number = input('Second number?')


if first_number.isnumeric() == True and second_number.isnumeric() == True:
    first_number = int(first_number)
    second_number = int(second_number)
    if operation == '+':
        print(f'product of {first_number} + {second_number} equals {first_number + second_number}')
    if operation == '-':
        print(f'product of {first_number} + {second_number} equals {first_number - second_number}')
    if operation == '*':
        print(f'product of {first_number} + {second_number} equals {first_number * second_number}')
    if operation == '/':
        print(f'product of {first_number} + {second_number} equals {first_number / second_number}')
    if operation == '%':
        print(f'product of {first_number} + {second_number} equals {first_number % second_number}')
    if operation == '**':
        print(f'product of {first_number} + {second_number} equals {first_number ** second_number}')
    if operation.isalnum() == True or operation.isalpha() == True or operation.isdecimal():
        print('Operation not recognized.')
        exit()
elif first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Please input a number.')
    exit()



#Gabarito
# print('Simple calculator!')
#
# first_number = input('First number? ')
#
# if first_number.isnumeric() == False:
#     print('Please input a number.')
#     exit()
#
# operation = input('Operation? ')
#
# second_number = input('Second number? ')
#
# if second_number.isnumeric() == False:
#     print('Please input a number.')
#     exit()
#
# first_number = int(first_number)
# second_number = int(second_number)
#
# result = 0
# if operation == '+':
#     result = first_number + second_number
#     label = 'sum'
# elif operation == '-':
#     result = first_number - second_number
#     label = 'difference'
# elif operation == '*':
#     result = first_number * second_number
#     label = 'product'
# elif operation == '/':
#     result = first_number / second_number
#     label = 'quotient'
# elif operation == '**':
#     result = first_number ** second_number
#     label = 'exponent'
# elif operation == '%':
#     result = first_number % second_number
#     label = 'modulus'
# else:
#     print('Operation not recognized.')
#     exit()
#
# print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))




