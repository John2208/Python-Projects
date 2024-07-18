import random

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Type a number next time")
    quit()

random_number = random.randint(0,top_of_range)
#print(random_number)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type a number next time!')
        continue

    if user_guess == random_number:
        print("You got it right")
        break
    elif user_guess > random_number:
        print("You were above the random number")     
    else:
        print("You were below the random number")   

print("You got it in " + str(guesses) + " guesses")
