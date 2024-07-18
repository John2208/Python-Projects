print('Welcome to my Quiz')

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print('Incorrect!')

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print('Incorrect!')

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print('Incorrect!')

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score +=1
else:
    print('Incorrect')


print("You got " +  str(score)  + " Questions correct")
print("You got " + str((score/4)*100) + " %. ")