"""
This is an implementation of the game "rock paper scissors lizard Spock" (RPS-5), 
first invented by Sam Kass and Karen Bryla, and popularised in the TV show The Big Bang 
Theory. It seeks to solve the issue of the standard "rock paper scissors" (RPS-3), which 
is the rate of producing ties in the game. This modification adds two more possible moves 
to play, increasing the chances of a win being reached on the first try.

In this program, you will play against the computer, it will offer you a game, and then
you will play your choice. A dictionary is used to check player and computer choices 
against win conditions.
"""
from random import choice
from time import sleep

def play():
    # the "moves" for the user and computer are initialised
    player = ""
    comp = ""
    # the dictionary stores thet choices and potential win conditions for the game
    # ie player = rock, comp = scissors, therefore if rock is checked, and scissors
    # corresponds to it, what action is done by the rock?
    # rock breaks scissors
    dict = {
        "rock": {"lizard":"crushes", "scissors":"breaks"},
        "paper": {"rock":"cover", "spock":"disproves"},
        "scissors": {"paper":"cuts", "lizard":"decapitates"},
        "lizard": {"paper":"eats", "spock":"poisons"},
        "spock": {"scissors":"smashes", "rock":"vaporises"}
    }
    while player ==  comp:
        print("\nRock, paper, scissors, lizard, Spock!")
        comp = choice(["rock","paper","scissors","lizard","spock"])
        while True:
            try:
                player = input("Shoot!\t\t")
                if player not in dict:
                    raise KeyError
                break
            except KeyError:
                sleep(1.5)
                print("That's not... do you not know what the game is?")
        
        print("\n|    Computer\t|    Player\t|")
        print("|    %s\t|    %s\t|\n" % (comp.capitalize(), player.capitalize()))
        # here is the actual logic of the game, a draw is checked for, else a winner is decided
        if player == comp:
            sleep(1)
            print("It's a tie!")
            sleep(1.5)
            print("Let's go again! Ready?")
            sleep(2)
        else:
            sleep(1)
            if comp in dict[player]:
                print("%s %s %s, you win!" % (player.capitalize(), dict[player][comp], comp))
            else: print("%s %s %s, computer wins!" % (comp.capitalize(), dict[comp][player], player))

if __name__ == "__main__":
    playgame = input("Would you like to play a game of rock paper scissors lizard Spock?\n[y/n]\t\t").lower()
    if playgame == ("y" or "yes"):
        play()
    else: print("Okay then, maybe another time.")