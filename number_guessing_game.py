import random
number = random.randint(1,10)
print ("Welcome to Number Guessing Game !")
print ("I have selected a number between 1 and 10 . Can you guess it in 3 attempts ?")
attempts = 3
while attempts >0:
    user_guess = int(input("Enter your guess : "))
    if user_guess == number:
        print ("Congratualtions You Won")
    if user_guess > number:
        print ("you chose a higher number")
    if user_guess < number:
        print ("you chose a lower number")
    attempts -=1
    print (f"you have {attempts} attempts left.\n")
if attempts ==0:
    print ("Ahh ! Ran out of attempt , the number was ")
    print (number)
