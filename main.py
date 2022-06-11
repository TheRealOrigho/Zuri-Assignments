import random

choices = ["Rock", "Paper", "Scissors"]

def user_choice():
    select_choice = input("Select from options \n R for Rock \n P for Paper \n S for Scissors \n")
    if select_choice in ["R", "r"]:
        select_choice = "Rock"
    elif select_choice in ["P", "p"]:
        select_choice = "Paper"
    elif select_choice in ["S", "s"]:
        select_choice = "Scissors"
    else:
        print("Invalid Choice")
        return user_choice()
    return select_choice

def computer_choice():
    comp_choice = random.choice(choices)
    return comp_choice

def main_game(): 
    while True:
        player_choice = user_choice()
        com_choice = computer_choice()
        
        if player_choice == com_choice:
            print("Computer: ", com_choice)
            print("Player: ", player_choice)
            print("Game was a Tie")
        
        elif player_choice == "Rock":
            if com_choice == "Paper":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Lose")
                
            if com_choice == "Scissors":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Win")
            
        elif player_choice == "Paper":
            if com_choice == "Rock":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Win")
            if com_choice == "Scissors":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Loose")
                
        elif player_choice == "Scissors":
            if com_choice == "Rock":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Lose")
            if com_choice == "Paper":
                print("Computer: ", com_choice)
                print("Player: ", player_choice)
                print("You Win")
                
        play_choice = input("Do you want to play again ? \n Y --- Yes \n N --- No \n").lower()
        if play_choice != "y":
            break
    print("This game has ended")

main_game()
    

