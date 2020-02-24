#  Inspiration: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs
#  Ref: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

from tkinter import *
from random import randint
import ctypes  # An included library with Python install.


#  Pop up GUI
popup = Tk()    # For user select game rounds
main = Tk()     # Main Pop up

#  Number of game rounds
globalGameRound = 0

#  Player play options
globalUserPlayOption = "None"

#  Start flag
start = False
#  Create a list of play options
playOptions = ["Rock", "Paper", "Scissors"]

#  Randomize computer play options
computerPlayOption = playOptions[randint(0, 2)]


#  Desc: Verify sser's play option ()
#  Param: Input from user
#  Retval: Rock, Paper, Scissors, False
def verifyUserPlayOption(argument):
    if argument.lower() == "rock" or \
        argument.lower() == "paper" or  \
            argument.lower() == "scissors":
        return argument
    else:
        return False


#  Desc: Is the game tied? (Assume that the input from
#        user are valid)
#  Param: User and computer play options
#  Retval: True or False
def isTheGameTied(userOption, computerOption):
    if userOption.lower() == computerOption.lower():
        return True
    else:
        return False


#  Desc: Determine the winner when the game is not tied
#        (Assume that the options are valid)
#  Param: User and computer play options
#  Retval: Return result of the game in string
def gameNotTiedHandler(userOption, computerOption):
    if userOption.lower() == "rock" and computerOption.lower() == "scissors":
        return "You win! Rock beats Scissors."
    elif userOption.lower() == "rock" and computerOption.lower() == "paper":
        return "You lose! Paper beats Rock."
    elif userOption.lower() == "paper" and computerOption.lower() == "rock":
        return "You win! Paper beats Rock."
    elif userOption.lower() == "paper" and computerOption.lower() == "scissors":
        return "You lose! Scissors beats Paper."
    elif userOption.lower() == "scissors" and computerOption.lower() == "paper":
        return "You win! Scissors beats Paper."
    elif userOption.lower() == "scissors" and computerOption.lower() == "rock":
        return "You lose! Rock beats Scissors."


#  Desc: Main function to call functions to perform
#        the game
#  Param: None
#  Retval: None
def gameManager():
    gameRound = int(input("Please choose how many rounds to play."))
    while gameRound != 0:
        userPlayOption = input("Rock, Paper, Scissors?")
        computerPlayOption = playOptions[randint(0, 2)]
        while not verifyUserPlayOption(userPlayOption):  # Invalid input
            userPlayOption = input("Invalid input, try again. Rock, Paper, Scissors?")
        if isTheGameTied(verifyUserPlayOption(userPlayOption), computerPlayOption):
            print("Tie!")
        else:
            print(gameNotTiedHandler(userPlayOption, computerPlayOption))

        gameRound -= 1


if __name__ == "__main__":
    # Commented out for unittests else hang instantiating tests...
    # Uncomment to test the game here
    #gameManager()
    #main()
#  ref: https://www.youtube.com/watch?v=ELkaEpN29PU

#  -------------------GUI-----------------------------
#   Create windows object

    def userSelectRock():
        global globalUserPlayOption
        globalUserPlayOption = "Rock"
        print("You selected Rock")

    def userSelectPaper():
        global globalUserPlayOption
        globalUserPlayOption = "Paper"
        print("You selected Paper")

    def userSelectScissors():
        global globalUserPlayOption
        globalUserPlayOption = "Scissors"
        print("You selected Scissors")

    def userInputRound(arg):
        print(arg)

    def userSelectOneRound():
        global globalGameRound
        globalGameRound = 1
        popup.destroy()
        print(globalGameRound)

    def userSelectThreeRound():
        global globalGameRound
        globalGameRound = 3
        popup.destroy()
        print(globalGameRound)

    def userSelectTenRound():
        global globalGameRound
        globalGameRound = 10
        popup.destroy()
        print(globalGameRound)


#  Create an popup message box for user to select game round
def popupMsgSelectGameRound(msg):

    popup.wm_title("Game Menu")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="1", command=userSelectOneRound)
    B1.pack()
    B2 = Button(popup, text="3", command=userSelectThreeRound)
    B2.pack()
    B3 = Button(popup, text="10", command=userSelectTenRound)
    B3.pack()
    popup.deiconify()


def popupMain():
    main.title('Rock, Paper and Scissors Game, by Jason')
    main.geometry('500x350')

    #  Create the play option buttons
    main.ButtonRock = Button(main, text="Rock", command=userSelectRock).place(x=2, y=2)
    main.ButtonPaper = Button(main, text="Paper", command=userSelectPaper).place(x=50, y=50)
    main.ButtonScissors = Button(main, text="Scissors", command=userSelectScissors).place(x=100, y=100)

    main.mainloop()


popupMsgSelectGameRound("Please select the rounds to be played.")
popupMain()






