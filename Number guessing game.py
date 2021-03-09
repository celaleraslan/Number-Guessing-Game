import random,time

def countdown():
    for i in range(5,0,-1):
        time.sleep(1)
        print(i)

def exit():
    print("The program shuts down...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("The program is closed.")

def initiation():
    print("Game Launching...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    start_game()

def start_game(prediction = 5):

    print("The Number Guessing Game Is About To Begin...")
    print("!!!Remember you got five guesses!!!")

    countdown()

    correct_value = random.randint(0,50)

    while(prediction > 0):
        guess = int(input("I kept a number between 0 and 50 in my mind. Guess which one?"))

        if(guess > correct_value):
            print("You should minimize your guess :)")
            prediction-=1
        elif(guess < correct_value):
            print("You should increase your guess :)")
            prediction -= 1
        else:
            print("You got it right, congratulations :) The number I kept in my mind was ",correct_value)
            break

    if(prediction == 0):
        print("Your guessing right is over, you didn't know the number I kept in my mind.")
        print("The number I kept in my mind was ", correct_value)

    key = input("Do you want to play again? Y / N:")

    if(key == "Y"):
        initiation()
    else:
        exit()

start_game()
