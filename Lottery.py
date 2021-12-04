import random
print('LOTTERY GAME')
def lotteryGame():
    
    lotteryList = []
    selectedNumbers= []
   
    for i in range(3):
        print(i)
        user= int(input("Enter a number ranging from 0-9:"))
        while (user in selectedNumbers or user<1 or user>9):
            print('Invalid number,please try again.')
            print(i)
            user= int(input("Enter a number ranging from 0-9:"))
    
        selectedNumbers.append(user)
        selectedNumbers.sort()

        random_number = random.randint(0,9)
        while random_number == lotteryList:
            random_number = random.randint(0,9)
        lotteryList.append(random_number)
        lotteryList.sort()

    print('Your lottery numbers:')
    print(selectedNumbers)

    print("Today's lottery numbers are:")
    print(lotteryList)

    for number in selectedNumbers:
        if number == lotteryList:
            print("WINNER!!")
        else:
            print('You Lose')
        again = str(input('Try Again? type y or n:'))
        if again == 'y':
            lotteryGame()
        else:
            break
        return
lotteryGame()