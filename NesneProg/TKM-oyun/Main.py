import random

class Player:
    def __init__(self, name):
        self.name = name
        self.move = ""

    def make_move(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_name(self):
        return self.name

    def get_move(self):
        return self.move

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self):
        choice = int(input("Choose your move:\n1. Rock\n2. Paper\n3. Scissors\n"))
        if choice == 1:
            self.move = "Rock"
        elif choice == 2:
            self.move = "Paper"
        elif choice == 3:
            self.move = "Scissors"
        else:
            self.move = "Rock"  # Default move
        return self.move

class RandomComputerPlayer(ComputerPlayer):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self):
        choice = random.randint(1, 3)
        if choice == 1:
            self.move = "Rock"
        elif choice == 2:
            self.move = "Paper"
        elif choice == 3:
            self.move = "Scissors"
        return self.move

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Draw"
    if (player_move == "Rock" and computer_move == "Scissors") or \
       (player_move == "Scissors" and computer_move == "Paper") or \
       (player_move == "Paper" and computer_move == "Rock"):
        return "Player"
    else:
        return "Computer"

def main():
    player_name = input("Enter your name: ")

    human = HumanPlayer(player_name)
    computer = RandomComputerPlayer("Computer")

    player_score = 0
    computer_score = 0
    move_history = []

    while True:
        print("\nNew Round!")

        player_move = human.make_move()
        computer_move = computer.make_move()

        winner = determine_winner(player_move, computer_move)

        print(f"{player_name} chose: {player_move}")
        print(f"Computer chose: {computer_move}")
        print(f"Winner: {winner}")

        if winner == "Player":
            player_score += 1
        elif winner == "Computer":
            computer_score += 1

        move_history.append(f"{player_move} vs {computer_move} -> {winner}")

        print(f"Scores - {player_name}: {player_score} Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() == 'n':
            break

    print("\nGame Over!")
    print(f"Final Scores - {player_name}: {player_score} Computer: {computer_score}")

    print("\nGame History: ")
    for entry in move_history:
        print(entry)

if __name__ == "__main__":
    main()
