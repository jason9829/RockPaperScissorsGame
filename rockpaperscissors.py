#  Inspiration: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs
#  Ref: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

from random import randint

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
# gameManager()