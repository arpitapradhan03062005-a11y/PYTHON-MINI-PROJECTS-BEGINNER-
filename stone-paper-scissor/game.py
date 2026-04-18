'''
stone = 1
paper = 0
scissor = -1
'''
import random

computer = random.choice([1,0,-1])
youstr = input("Enter your choice :")
dict = {"s":1,"p":0,"sc":-1}
r_dict = {1:"Stone",0:"Paper",-1:"Scissor"}
you = dict[youstr]

print(f"You chose {r_dict[you]} and computer chose {r_dict[computer]}")

if(computer == you):
    print("Its a draw!!")
else:
    if(computer==1 and you==0):
        print("You won!!")
    elif(computer==1 and you==-1):
        print("You lose!!")
    elif(computer==0 and you==1):
        print("You lose!!")
    elif(computer==0 and you==-1):
        print("You won!!")
    elif(computer==-1 and you==1):
        print("You won!!")
    elif(computer==-1 and you==0):
        print("You lose!!")
    else:
        print("Something went wrong!!")
