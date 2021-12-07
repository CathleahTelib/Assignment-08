import random

inputNumber= random.randint(0,100)

while True:
    print('Please guess the number between 0-100')
    guessNumber= int(input())
    if guessNumber == inputNumber:
        print("You guessed it right!")
        print("The random number is",inputNumber)
    elif guessNumber > inputNumber:
        print("The number you input is Greater than the random number")
    elif guessNumber < inputNumber:
        print('The number you input is Less than the random number')
