# Function to run the quiz
def play_quiz():
    score = 0

    answer = input("What was Mario's first appearance? ")
    if answer.lower() == "donkey kong":
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input("What organization was Cloud Strife formerly a part of? ")
    if answer.lower() == "soldier":
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input("What was Sonic The Hedgehog's original name? ")
    if answer.lower() in ["mr. needlemouse", "mr needlemouse", "mr. needle mouse", "mr needle mouse"]:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input("What game won Game of the Year in 2023? ")
    if answer.lower() in ["baldur's gate 3", "baldur's gate iii"]:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    print("You got " + str(score) + " questions correct!")
    print("You got " + str(score / 4 * 100) + "%. ")
    print("Thank you for playing my quiz!")

# Main game loop
while True:
    print("Welcome to my gaming quiz!")

    playing = input("Do you want to play? (yes/no): ")
    if playing.lower() != "yes":
        print("Goodbye!")
        quit()

    print("Okay! Let's play :)")

    # Start the quiz
    play_quiz()

    # Ask if the player wants to try again
    playing = input("Want to try again? (yes/no): ")
    if playing.lower() != "yes":
        print("Thanks for playing!")
        quit()
    else:
        print("Let's play again!")  # Optional, but it confirms the replay
