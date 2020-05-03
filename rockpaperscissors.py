#  Inspiration: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs
#  Ref: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

from tkinter import *
from random import randint
import ctypes  # An included library with Python install.
import sys

#  Pop up GUI
popup = Tk()  # For user select game rounds
main = Toplevel()  # Main Pop up

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

#  Desc: Verify user's play option ()
#  Param: Input from user
#  Retval: Rock, Paper, Scissors, False
def verifyUserPlayOption(argument):
    if argument.lower() == "rock" or \
            argument.lower() == "paper" or \
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


# Determine is the end result is tied with input str
def isGameTied(arg):
    if arg == "Game tied! Play one more round...":
        return True
    else:
        return False


# Show the score between user, tie and computer
# Ref: https://stackoverflow.com/questions/31707206/tkinter-label-counter-variable
def updateScoreBoard():
    userWin_Label = Label(main, text="User Win: " + str(userWinCount))
    userWin_Label.place(x=110, y=150)

    gameTie_Label = Label(main, text="Tie: " + str(tieCount))
    gameTie_Label.place(x=110, y=210)

    ComputerWin_Label = Label(main, text="Computer Win: " + str(computerWinCount))
    ComputerWin_Label.place(x=110, y=270)


#  Reset the scoreboard after the game is completed
def resetScoreBoard():
    global userWinCount, tieCount, computerWinCount
    userWinCount = 0
    tieCount = 0
    computerWinCount = 0
    updateScoreBoard()


#  Update the game round and display on main windows
def updateGameRound():
    if globalGameRound == STOP_GAME_FLAG:
        gameRound_Label = Label(main, text="Round left: " + "XX" + "  ")
    else:
        gameRound_Label = Label(main, text="Round left: " + str(globalGameRound) + "  ")

    gameRound_Label.config(font=("Courier", 10))
    gameRound_Label.place(x=370, y=20)


# -----------------Events for button pressed-----------------
def userSelectRock():
    global globalUserPlayOption
    globalUserPlayOption = "Rock"
    main.quit()
    # quit() will close the window but not mainloop()
    # destroy() will close the windows and mainloop()
    # No withdraw() here because it's the main window
    # If use then the app is basically closed.


def userSelectPaper():
    global globalUserPlayOption
    globalUserPlayOption = "Paper"
    main.quit()


def userSelectScissors():
    global globalUserPlayOption
    globalUserPlayOption = "Scissors"
    main.quit()
    print("You selected Scissors")


def userSelectOneRound():
    global globalGameRound
    globalGameRound = 1
    updateGameRound()
    popup.withdraw()
    print(globalGameRound)


def userSelectThreeRound():
    global globalGameRound
    globalGameRound = 3
    updateGameRound()
    popup.withdraw()
    print(globalGameRound)


def userSelectTenRound():
    global globalGameRound
    globalGameRound = 10
    updateGameRound()
    popup.withdraw()
    print(globalGameRound)


def userSelectExit():
    sys.exit()


#  Create an popup message box for user to select game round
#  Ref: https://www.youtube.com/watch?v=4McKSuuUQ-0
def popupMsgSelectGameRound(msg):
    popup.wm_title("Game Menu")
    # ICON src: http://www.iconarchive.com/show/umicons-icons-by-mattahan/Games-icon.html
    #popup.iconbitmap(r'gameConsole.ico')    # Works within the IDE but not working for .exe
    # Need to change for different directory
    popup.iconbitmap(r'.\images\gameConsole.ico')
    label = Label(popup, text=msg)
    label.pack(side=TOP, fill="x", pady=10)
    B1 = Button(popup, text="1", width=5, height=3, command=userSelectOneRound)
    B1.pack(side=LEFT)
    B2 = Button(popup, text="3", width=5, height=3, command=userSelectThreeRound)
    B2.pack(side=LEFT)
    B3 = Button(popup, text="10", width=5, height=3, command=userSelectTenRound)
    B3.pack(side=LEFT)
    B4 = Button(popup, text="Exit", width=5, height=3, bg="red", command=userSelectExit)
    B4.pack(side=RIGHT)


# GUI menu to play the game
def popupMain():
    main.resizable(False, False)
    main.title('Rock, Paper and Scissors Game, by Jason')
    # ICON src: http://www.iconarchive.com/show/umicons-icons-by-mattahan/Games-icon.html
    # Need to change for diferrent directory
    #main.iconbitmap(r'gameConsole.ico) # Works within the IDE but not working for .exe
    main.iconbitmap(r'.\images\\gameConsole.ico')
    main.geometry('500x348')    # Offset horizontal pixels to fit the window with buttons
    # Create image for the option buttons
    # Image dont display previosly because the garbage collector clear the image
    # Ref: https://stackoverflow.com/questions/22200003/tkinter-button-not-showing-image
    # Need to change for different directory
    rockPhoto = PhotoImage(file=r'.\images\rock_resized.png')
    paperPhoto = PhotoImage(file=r'.\images\paper_resized.png')
    scissorsPhoto = PhotoImage(file=r'.\images\scissors_resized.png')
    #rockPhoto = PhotoImage(file=r'rock_resized.png')   # Works within the IDE but not working for .exe
    #paperPhoto = PhotoImage(file=r'paper_resized.png') # Works within the IDE but not working for .exe
    #scissorsPhoto = PhotoImage(file=r'scissors_resized.png')   # Works within the IDE but not working for .exe

    #  Create the play option buttons
    #  Ref: https://stackoverflow.com/questions/46284901/how-do-i-resize-buttons-in-pixels-tkinter/
    #  Reference to resize the button
    ButtonRock = Button(main, text="Rock", command=userSelectRock)
    ButtonRock.place(x=0, y=0, width=100, height=116)
    ButtonRock.image = rockPhoto
    ButtonRock.config(image=rockPhoto, width="120", height="120")

    ButtonPaper = Button(main, text="Paper", command=userSelectPaper)
    ButtonPaper.place(x=0, y=116, width=100, height=116)
    ButtonPaper.image = paperPhoto
    ButtonPaper.config(image=paperPhoto, width="120", height="120")

    ButtonScissors = Button(main, text="Scissors", command=userSelectScissors)
    ButtonScissors.place(x=0, y=232, width=100, height=116)
    ButtonScissors.image = scissorsPhoto
    ButtonScissors.config(image=scissorsPhoto, width="120", height="120")


# Initialise the windows of hide it using withdraw()
def initWindows():
    popupMain()
    main.withdraw()  # Hide the window and use deiconify() to show later
    popupMsgSelectGameRound("Please select the rounds to be played or exit.")
    popup.withdraw()


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


# Find the final result of the game
def getGameResult(userWin, Tie, computerWin):
    if userWin > computerWin:
        return "The winner is User, YOU WIN!"
    elif userWin < computerWin:
        return "The winner is Computer, YOU LOSE!"
    else:
        return "Game tied! Play one more round..."


#  Desc: Main function to call functions to perform
#        the game - GUI version
#  Param: None
#  Retval: None
def gameManagerGUI():
    global globalGameRound
    global computerPlayOption
    global globalUserPlayOption
    global gameRound

    initWindows()
    main.deiconify()  # Display the main menu window
    popup.deiconify()  # Display the sub menu window
    while globalGameRound != 0:
        updateGameRound()
        updateScoreBoard()
        userPlayOption = globalUserPlayOption
        computerPlayOption = playOptions[randint(0, 2)]
        if isTheGameTied(userPlayOption, computerPlayOption) and globalGameRound != STOP_GAME_FLAG:
            global tieCount
            tieCount += 1
            updateScoreBoard()
            #  Could not find a way to update the text
            #  This is a work around
            showMsg("Tie!                                ")
            globalGameRound -= 1
            updateGameRound()
        else:
            if globalGameRound != STOP_GAME_FLAG:
                showMsg(gameNotTiedHandlerGUI(userPlayOption, computerPlayOption))
                updateScoreBoard()
                globalGameRound -= 1  # Put inside bcoz when globalGameRound = STOP_GAME_FLAG
                updateGameRound()  # it will this else
        if globalGameRound == 0:
            msg = getGameResult(userWinCount, tieCount, computerWinCount)
            popupMsg(msg)
            if not isGameTied(msg):
                gameRound = 1  # Reset the value
                updateGameRound()
                resetScoreBoard()
                showMsg("Game Over!                                ")  # Reset the msg box
                popup.deiconify()
            else:
                globalGameRound += 1
                updateGameRound()
        main.mainloop()  # This infinite loop should be the last line of the function code


 gameManagerGUI()  # Remove the comment to allow GUI to run because this is commented for unit testing.
