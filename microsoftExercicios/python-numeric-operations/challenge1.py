# Escrever um programa para converter as temperaturas de Fahrenheit em Celsius

fahrenheit = input('What is the temperature in fahrenhheit?')

if fahrenheit.isnumeric() == False:
    print('Input is not a number.')
    exit()


celsius = (int(fahrenheit) - 32) * 5/9
print('Temperature in celsius is {}'.format(int(celsius)))

#Gabarito

# fahrenheit = input('What is the temperature in Fahrenheit?  ')
#
# if fahrenheit.isnumeric() == False:
#     print('Input is not a number.')
#     exit()
#
# fahrenheit = int(fahrenheit)
#
# celsius = int((fahrenheit - 32) * 5/9)
# print('Temperature in celsius is ' + str(celsius))

