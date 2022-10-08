import random


while True:

    userInput = input("Enter Rock, Paper or Scissors: ")
    userInput = userInput.lower()

    # check user wants to quit
    if userInput == "quit":
        break

    # check valid input
    if userInput != "rock" and userInput != "paper" and userInput != "scissors":
        print("Invalid Input, Please try again")
        continue

    # if valid answer => continue the process
    computerAnswer = random.choice(["rock", "paper", "scissors"])

    # wining chances
    if userInput == "rock" and computerAnswer == "scissors":
        print(
            f" You won ! your answer is {userInput} and computer anser is {computerAnswer}")
        break
    elif userInput == "paper" and computerAnswer == "rock":
        print(
            f" You won ! your answer is {userInput} and computer anser is {computerAnswer}")
        break
    elif userInput == "scissors" and computerAnswer == "paper":
        print(
            f" You won ! your answer is {userInput} and computer anser is {computerAnswer}")
        break
    elif userInput == computerAnswer:
        print(
            f"You have tied. your answer is {userInput} and computer anser is {computerAnswer} Try again")
        continue
    else:
        print(
            f"You have lose! your answer is {userInput} and computer answer is {computerAnswer}")
        continue
