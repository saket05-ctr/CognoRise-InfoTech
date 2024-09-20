# ROCK, PAPER, SCISSORS GAME !!


import random

round=1
while round == 1:
    computer=random.randint(-1, 1)

    print("\nR for rock \nP for paper \nS for scissor \n")
    user_choice=input("enter your choice: ")[0]
    user_choice = user_choice.upper()

    dict={"R": -1,"P": 0,"S": 1}
    you=dict[user_choice]

    reversed_dict ={-1:"R", 0:"P", 1:"S"}


    if you ==computer:
        print("its a draw!")

    else:
        if(computer==1 and you==0):
            print("you lose!")

        elif(computer==1 and you==-1):
            print("you win!")

        elif(computer==0 and you==1):
            print("you win!")

        elif(computer==0 and you==-1):
            print("you lose!") 

        elif(computer==-1 and you==0):
            print("you win!")

        elif(computer==-1 and you==1):
            print("you lose!") 

        else:
            print("something went wrong")

    
    print(f"computer's choice: {reversed_dict[computer]}\nyour choice: {reversed_dict[you]}")
    round=int(input("want to play one more round ?...enter 1 for YES and 0 for NO: "))

    
print("Thanks for playing the game...Come Again..")


