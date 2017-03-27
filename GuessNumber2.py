#!/usr/bin/python
#Filename:GuessNumber2.py

number = 23
running = True

while running:
    guess = int(input("Enter an integer:"))
    if guess == number:
        print("Congratulations, you guess the right number!")
        running = False
    elif guess < number:
        print('Less!')
    else:
        print('Bigger!')
else:
    print('The loop is over!')
print('Done!')
