import random
print('Hello, what\'s your name?')
name = input()

print('Well, ' + name + ', I\'m thinking of a random number between 1 and 20.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. I was thinking of ' + str(secretNumber) + '.')
