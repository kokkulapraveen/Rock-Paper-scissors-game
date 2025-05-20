import random
print("WELCOME TO rock paper scissor  GAME ")
response= input("Do You Want To Play The Game: ")
if response.lower() !="yes":
    quit()

user_wins=0
computer_wins=0
options=["rock","scissor","paper"]
while True:
    user_input=input("choose one option from Rock Paper Scissor or Q to quit: ").lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue
    random_number= random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked ", computer_pick+".")
    if user_input=='rock' and computer_pick=="scissor":
        print("You Won! ")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You Won! ")
        user_wins+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("You Won! ")
        user_wins+=1
    elif user_input== computer_pick:
        print("Draw")
        continue
    else:
        print("You Lost")
        computer_wins+=1


print("You Won ",user_wins,' times. ')
print("Computer won ",computer_wins,' times. ')
print("Game Over ")




