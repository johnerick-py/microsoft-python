import random

value = random.randint(1, 10)
count = 0
guess = 0


while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 10: ')
    print(f'Enter guess #{count}: {guess}')

    if guess.isnumeric() == False:
        print('Numbers only, please!')
        continue

    if guess.isnumeric():
        guess = int(guess)

    if guess > value:
        print('Your guess is too high, try again!')
        continue

    if guess < value:
        print('Your guess is too low, try again!')
        continue
else:
    print(f'You guessed it in {count} tries!')