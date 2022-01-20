# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

name = "" #initialize name variable
sayNumber = random.randint(1, 100) #generates random number between 1 and 100.
thinkNumber = random.randint(1, 100) #generates random number between 1 and 100.

def bearGrylls(): #Our game function. The goal of the game is to pick the correct path based on survival knowledge and judgement.
    print("Hello. Welcome to your adventure with Bear Grylls.")
    name = input("What is your name? ") #get input from user
    print(f'{name}, we do not have much time. Make your way over that helicopter right now.') #f strings used to implement variables in our strings.
    print("*sprinting to chopper*")
    while True: #while true meaning we will stay in this loop until a 'break' thing is triggered. makes sure our user enters a valid input.
        correctName = input(f'Hello mate, I am Bear Grylls. Your name was {name} correct? (y/n) ')
        if (correctName.lower() == "y"): #checks user input
            print("Nice to meet you. We are approaching our dropping location. We need to deliver these extremely fragile vials to the doctor located in the middle of Koh Samui, a tropical island in the Gulf of Thailand. The island is overgrown by jungle so we need to drop down by the shore and make our way towards the middle. ")
            break #breaks out of loop
        if (correctName.lower() == "n"):
            print("Meh, it is now. We are approaching our dropping location. We need to deliver these extremely fragile vials to the doctor located in the middle of Koh Samui, a tropical island in the Gulf of Thailand. The island is overgrown by jungle so we need to drop down by the shore and make our way towards the middle. ")
            break
        print("Please enter either 'y' or 'n'") #error message
    print("*jumping out of chopper*")
    while True:
        decision1 = input(f'Alright {name}, this is where I need you. The jungle looks a bit harsh here, should we try making our way to the middle from this point (1) or should we go take a walk further down the coast and try to find a better spot (2)? (1/2) ')
        if (decision1 == "1"):
            print("The jungle was too harsh. You missed the venomous snake that you stepped on. You are so dead.")
            exit() #exit program
        if (decision1 == "2"):
            print("You make your way down the coast and find a better entry point")
            break
        else:
            print("Please enter either '1' or '2'")
    print("*entering jungle*")
    while True:
        decision2 = input(f'{name}, we are faced with this giant cliff on the side of the river (1) or that scary looking bridge that looks like it is going to collapse (2). Which route do you suggest we take? (1/2) ')
        if (decision2 == "1"):
            print("You both slip trying to climb to the top of the cliff and break the fragile vials. Mission Failed.")
            exit() #exit program
        if (decision2 == "2"):
            print("You manage to pass the bridge. Someone will definitely fall to their death one of these days...")
            break
        else:
            print("Please enter either '1' or '2'")
    print("Nice work making it this far. Let's keep going.")
    print(f'Mate, let''s play a game. I''m gonna say a random number between 1-100 and then think of another one between 1-100, take a guess if you think the number that I''m thinking of is higher or lower than the number I said.')
    while True:
        decision3 = input(f'Alright mate, the number is {sayNumber}. Am I thinking of a number higher or lower than that? (h/l) ')
        if (decision3 == "h"):
            if (thinkNumber > sayNumber):
                print(f'Nice, you got it. I was thinking of {thinkNumber}')
                break
            else:
                print("You lose. Mission failed. (unlucky)")
                exit()
        if (decision3 == "l"):
            if (thinkNumber > sayNumber):
                print("You lose. Mission failed. (unlucky)")
                exit()
            else:
                print(f'Nice, you got it. I was thinking of {thinkNumber}')
                break
        else:
            print("Please choose either 'h' or 'l'")
    print(f'Alright {name}, I think we''re almost at the village. I can hear the people.')
    while True:
        decision4 = input(f'We''re faced with a difficult decision here. Should we use the tree vines to lower ourselves down this cliff (1) or should we hope that the water below is deep enough and jump (2)? (1/2) ')
        if (decision4 == "1"):
            print("You lower yourself down to the ground below the cliff and make it to the village. You manage to deliver the vials in tact. Mission complete.")
            break
        if (decision4 == "2"):
            print("It seems that the water was deep enough but the fall was so high that it felt like landing on concrete when you hit it. Every bone in your body shattered. You are so dead.")
            exit()
        else:
            print("Please choose either '1' or '2'")

#https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid
#I used the following article to allow players to restart the loop if they made an invalid choice. What I got from this was the idea of
#using while and break.

if __name__ == '__main__': #main method. anything inside this method is run when the green play button is clicked.
    bearGrylls()
