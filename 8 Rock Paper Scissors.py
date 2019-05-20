"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)"""


def game():
    while True:
        player1 = input('Player1: Rock, Paper or Scissors? ').lower()
        player2 = input('Player2: Rock, Paper or Scissors? ').lower()

        if player1 == player2:
            print('Draw!')
        elif player1 == 'rock':
            print('Player 1 wins!') if player2 == 'scissors' else print('Player 2 wins!')
        elif player1 == 'scissors':
            print('Player 1 wins!') if player2 == 'paper' else print('Player 2 wins!')
        elif player1 == 'paper':
            print('Player 1 wins!') if player2 == 'rock' else print('Player 2 wins!')

        decision = input('Do you want another game? Y or N: ').lower()
        if decision == 'n':
            break


game()
