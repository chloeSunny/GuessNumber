#!/usr/bin/python
#Filename:GuessNumber.py

number = 23
guess = int(input("Enter an integer:")) #python3.x uses input() to replace raw_input()

if guess == number:
    print('Congratulations, you guess the right number')
    print('but you win nothing')
elif guess < number:
    print('Less!')
else:
    print('Bigger')
print('Done!')
                      
