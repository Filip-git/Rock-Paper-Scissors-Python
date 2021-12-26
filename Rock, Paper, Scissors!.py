import random

def main():
    computer = random.choice(["rock", "paper", "scissors"])
    player = input("Enter your choice (rock, paper, scissors): ")
    print(f"\nYou chose {player}, computer chose {computer}.\n")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    Replay()

def Replay():
    print ('Would you like to play one more? [Y/N] ')
    reply = input()
    if reply == 'Y' or reply =='y':
        main()
    elif reply == 'N' or reply =='n':
        end()
    else:
        print('Please repeat and choose Y or N.')
        Replay()

def end():
    print('Thanks for playing =)')
		
main()