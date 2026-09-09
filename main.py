import random

wins = 0
looses = 0
ties = 0

def playerInput():
    inputa = input("Your turn - ")
    if inputa == "Rock" or "Paper" or "Scissors":
        return inputa

def computerInput():
    return random.choice(["Rock", "Paper", "Scissors"])

def win():
    global wins
    wins += 1
    print(f"Win ({wins})")

def loose():
    global looses
    looses += 1
    print(f"Loose ({looses})")

def tie():
    global ties
    ties += 1
    print(f"Tie ({ties})")

def playRound():
    inputa = playerInput()
    inputb = computerInput()
    if inputa == "Rock" and inputb == "Paper":
        loose()
    
    if inputa == "Paper" and inputb == "Scissors":
        loose()   

    if inputa == "Scissors" and inputb == "Rock":
        loose()  

    if inputb == "Rock" and inputa == "Paper":
        win()
    
    if inputb == "Paper" and inputa == "Scissors":
        win()   

    if inputb == "Scissors" and inputa == "Rock":
        win()

    if inputb == inputa:
        tie()

    print()

while wins < 3 and looses < 3:
    playRound()

if wins == 3:
    print(f"You won{chr(33)} - ")
elif looses == 3:
    print("You lost :(")

print(f"Wins: {wins}, Looses: {looses}, Ties: {ties}")
