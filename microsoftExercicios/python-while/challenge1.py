import random

roll = 0
count = 0

while roll != 5:

    answer = input('Guess a number between 1 and 5:')

    count += 1
    roll = random.randint(1, 5)
    if answer == roll:
        break

print(f'You guessed it in {count} tries!')



#Gabarito


# import random
#
# value = random.randint(1, 5)
# count = 0
# guess = 0
# while guess != value:
#     count += 1
#     guess = input('Guess a number between 1 and 5: ')
#     if guess.isnumeric():
#         guess = int(guess)
# else:
#     print(f'You guessed it in {count} tries!')


