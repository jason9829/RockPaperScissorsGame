#  Inspiration: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs
#  Ref: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

from tkinter import *
from random import randint
import ctypes  # An included library with Python install.
import sys

#  Pop up GUI
popup = Tk()    # For user select game rounds
main = Tk()     # Main Pop up

#  Game Status Flag/ To start or end the game
STOP_GAME_FLAG = 999

# Gameplay status
userWinCount = 0
tieCount = 0
computerWinCount = 0
gameRound = 1

#  Number of game rounds
globalGameRound = STOP_GAME_FLAG

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

    # Commented out for unittests else hang instantiating tests...
    # Uncomment to test the game here
    # gameManager()


#  -----------------For GUI (Not for Test)------------------------
#  Desc: Determine the winner when the game is not tied
#        (Assume that the options are valid) - GUI version
#  Param: User and computer play options
#  Retval: Return result of the game in string
def gameNotTiedHandlerGUI(userOption, computerOption):
    if userOption.lower() == "rock" and computerOption.lower() == "scissors":
        global userWinCount
        userWinCount += 1
        print(userWinCount)
        return "You win! Rock beats Scissors.  "
    elif userOption.lower() == "rock" and computerOption.lower() == "paper":
        global computerWinCount
        computerWinCount += 1
        print(computerWinCount)
        return "You lose! Paper beats Rock.   "
    elif userOption.lower() == "paper" and computerOption.lower() == "rock":
        userWinCount += 1
        return "You win! Paper beats Rock.    "
    elif userOption.lower() == "paper" and computerOption.lower() == "scissors":
        computerWinCount += 1
        return "You lose! Scissors beats Paper.   "
    elif userOption.lower() == "scissors" and computerOption.lower() == "paper":
        userWinCount += 1
        return "You win! Scissors beats Paper.   "
    elif userOption.lower() == "scissors" and computerOption.lower() == "rock":
        computerWinCount += 1
        return "You lose! Rock beats Scissors."


# Show the score between user, tie and computer
# Ref: https://stackoverflow.com/questions/31707206/tkinter-label-counter-variable
def updateScoreBoard():
    userWin_Label = Label(main, text="User Win: " + str(userWinCount))
    userWin_Label.place(x=110, y=150)

    gameTie_Label = Label(main, text="Tie: " + str(tieCount))
    gameTie_Label.place(x=110, y=210)

    ComputerWin_Label = Label(main, text="Computer Win: " + str(computerWinCount))
    ComputerWin_Label.place(x=110, y=270)


#  Update the game round and display on main windows
def updateGameRound():
    gameRound_Label = Label(main, text="Game round: " + str(gameRound))
    gameRound_Label.config(font=("Courier", 10))
    gameRound_Label.place(x=370, y=20)


def userSelectRock():
    global globalUserPlayOption
    globalUserPlayOption = "Rock"
    print("You selected Rock")
    main.quit()
    # quit() will close the window but not mainloop()
    # destroy() will close the windows and mainloop()


def userSelectPaper():
    global globalUserPlayOption
    globalUserPlayOption = "Paper"
    print("You selected Paper")
    main.quit()


def userSelectScissors():
    global globalUserPlayOption
    globalUserPlayOption = "Scissors"
    print("You selected Scissors")
    main.quit()


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


def userSelectExit():
    sys.exit()


#  Create an popup message box for user to select game round
#  Ref: https://www.youtube.com/watch?v=4McKSuuUQ-0
def popupMsgSelectGameRound(msg):

    popup.wm_title("Game Menu")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="1", width=10, height=5, command=userSelectOneRound)
    B1.pack()
    B2 = Button(popup, text="3", width=10, height=5, command=userSelectThreeRound)
    B2.pack()
    B3 = Button(popup, text="10", width=10, height=5, command=userSelectTenRound)
    B3.pack()
    B4 = Button(popup, text="Exit", width=10, height=5, command=userSelectExit)
    B4.pack()
    popup.deiconify()


# GUI menu to play the game
def popupMain():
    main.resizable(False, False)
    main.title('Rock, Paper and Scissors Game, by Jason')
    main.geometry('500x350')

    #  Create the play option buttons
    #  Ref: https://stackoverflow.com/questions/46284901/how-do-i-resize-buttons-in-pixels-tkinter/
    #  Reference to resize the button
    main.ButtonRock = Button(main, text="Rock", command=userSelectRock).place(x=0, y=0, width=100, height=116)
    main.ButtonPaper = Button(main, text="Paper", command=userSelectPaper).place(x=0, y=116, width=100, height=116)
    main.ButtonScissors = Button(main, text="Scissors", command=userSelectScissors).place(x=0, y=232, width=100,
                                                                                          height=116)


# GUI message box just to display the message
# with an OK button
def popupMsg(msg):
    ctypes.windll.user32.MessageBoxW(0, msg, "Message", 16)


# Show message on the window
def showMsg(msg):
    if msg is None:
        return ''
    msg_Label = Label(main, text="Message: " + msg)
    msg_Label.config(font=("Courier", 10))
    msg_Label.place(x=150, y=40)


# Find the winner of the game
def getWinner(userWin, Tie, computerWin):
    if userWin > computerWin:
        return "The winner is User, YOU WIN!"
    elif userWin < computerWin:
        return "The winner is Computer, YOU LOSE!"
    else:
        global gameRound
        gameRound += 1
        return "Game tied! Play one more round..."


#  Desc: Main function to call functions to perform
#        the game - GUI version
#  Param: None
#  Retval: None
def gameManagerGUI():
    popupMsgSelectGameRound("Please select the rounds to be played or exit.")
    global globalGameRound
    global globalUserPlayOption
    global gameRound

    while globalGameRound != 0:
        updateGameRound()
        updateScoreBoard()
        popupMain()
        userPlayOption = globalUserPlayOption
        computerPlayOption = playOptions[randint(0, 2)]
        if isTheGameTied(userPlayOption, computerPlayOption):
            global tieCount
            tieCount += 1
            updateScoreBoard()
            #  Could not find a way to update the text
            #  This is a work around
            showMsg("Tie!                                ")
        else:
            if globalGameRound != STOP_GAME_FLAG:
                showMsg(gameNotTiedHandlerGUI(userPlayOption, computerPlayOption))
                updateScoreBoard()
        globalGameRound -= 1
        gameRound += 1
        main.mainloop()
    popupMsg(getWinner(userWinCount, tieCount, computerWinCount))
    gameRound = 1   # Reset the value


while True:
    gameManagerGUI()






