# random computer play
from random import randint
rockdict = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}

run = True



print("Welcome to Rock, Paper, Scissors!")
while(run):
    number = input("Press 1 for instructions on how to play\nPress 2 to play\nPress 3 to exit the game\n")
    number = int(number)
    if number == 1:
        print("After pressing 2 to play, press 1 for rock, press 2 for paper, and press 3 for scissors.\n")
        print("Rock beats scissors, paper beats rock, and scissors beats paper\n")
    elif number == 2:
        com = str(randint(1,3))
        choice = input("Type a number to indicate your choice.\nPress 1 for rock, press 2 for paper, and press 3 for scissors.\n")

            
        
        print("You chose " + rockdict.get(choice))
        print("The computer chose " + rockdict.get(com))

        if int(choice) == int(com):
            print("It was a draw!")
        elif int(choice) == 1 and int(com) == 2:
            print("The computer wins!")
        elif int(choice) == 1 and int(com) == 3:
            print("You win!")
        elif int(choice) == 2 and int(com) == 1:
            print("You win!")
        elif int(choice) == 2 and int(com) == 3:
            print("The computer wins!")
        elif int(choice) == 3 and int(com) == 2:
            print("You win!")
        elif int(choice) == 3 and int(com) == 1:
            print("The computer wins!")

    elif number == 3:
        print("Thanks for playing. Goodbye!")
        run = False
        break
    else:
        print("Invalid input. Try again!")