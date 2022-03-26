import random
from termcolor import colored

Names = []
Scores = []
choices=["Rock", "Paper", "Scissors"]

def DisplayPlayers():
    print("**********************")
    size=len(Names)
    for i in range(size):
        print(Names[i], " " ,Scores[i])
    print("**********************") 

def AddNameandScore():
    print("**********************")
    x=input("Enter username: ")
    y=int(input("Enter score: "))
    print("**********************")
    Names.append(x)
    Scores.append(y)
    DisplayPlayers()
    
def DeletePlayer():
    Name=input("Enter Name to delete player: " )
    x=Names.index(Name)
    print(x)
    Names.pop(x)
    Scores.pop(x)

def HighestScore():
    x=Scores.index(max(Scores))
    print(Names[x], "has the highest score of", Scores[x])

def UpdateScore(Name):
    if Name not in Names:
        Names.append(Name)
        Scores.append(0)
    x=Names.index(Name)
    Scores[x]=Scores[x]+1
    print("**********************")
    print(Names, "   ", Scores[x])
    print("**********************")

def Game():
    Name=input("Enter username here: ")
    user=input("Enter your choice from Rock, Paper, or Scissors: ")
    computer=random.choice(choices)
    print("You chose,", user, "and computer chose,", computer)
    if user==computer:
        print("It's a tie!")
    elif user=="Rock" or user=="rock":
        if computer=="Paper":
            print("Paper covers rocks, you lost.")
        elif computer=="Scissors":
            print("Rock crushes scissors, you win!")
            UpdateScore(Name)
    elif user=="Paper" or user=="paper":
        if computer=="Rock":
            print("Paper covers rock, you win!")
            UpdateScore(Name)
        elif computer=="Scissors":
            print("Scissors cuts paper, you lost.")
    elif user=="Scissors" or user=="scissors":
        if computer=="Rock":
            print("Rock crushes scissors, you lost.")
        elif computer=="Paper":
            print("Scissor cuts paper, you win!")
            UpdateScore(Name)



print("Welcome to Rock, Paper, Scissors!")
while True:
    print("Choose your option \n Display : To Display Players \n Add : To Add a Player \n Delete : Delete a Player \n High : To Display the Highest Score \n Play : To Continue with the Game \n Exit : To Exit the Game")
    x=input("Enter choice here: ")
    if x=="Display" or x=="display":
        DisplayPlayers()
    elif x=="Add" or x=='add':
        AddNameandScore()
    elif x=="Delete" or x=="delete":
        DeletePlayer()
    elif x=="High" or x=="high":
        HighestScore()
    elif x=="Exit" or x=="exit":
        break
    elif x=="Play" or x=="play":
        Game()