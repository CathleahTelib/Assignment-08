import random

inputNumber= random.randint(0,100)
while True:
    print('Please guess the number between 0-100')
    guessNumber= int(input())
    if guessNumber == inputNumber:
        print("You guessed it right!")
        print("The random number is",inputNumber)
    elif guessNumber > inputNumber:
        print("Greater than")
    elif guessNumber < inputNumber:
        print('Less than')
