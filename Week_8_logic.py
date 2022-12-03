# Create the database:
import pandas as pd
games = pd.DataFrame(columns=[
    "Game ID",
    "Player X",
    "Player O",
    "Winner",
])

# Inserting data:
def add_game(player_X_name, player_O_name, winner):
    games.loc[len(games)] = {
        "Game ID": len(games) + 1,
        "Player X": player_X_name,
        "Player O": player_O_name,
        "Winner": winner
    }

# Initial board:
theboard = {
    '1': ' ', '2': ' ', '3': ' ', 
    '4': ' ', '5': ' ', '6': ' ', 
    '7': ' ', '8': ' ', '9': ' ', 
}

board_keys = []

for key in theboard:
    board_keys.append(key)

# Print the board:
def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Tictactoe function:
def tictactoe():
    
    turn = 'X'
    count = 0

    # Enter player name:
    player_X_name = input("Enter player X name:")
    player_O_name = input("Enter player O name:")

    for i in range(10):

        print_board(theboard)

        if turn == 'X':
            print("It's you turn,", player_X_name, ". Move to which place?")
        else:
            print("It's you turn,", player_O_name, ". Move to which place?")
        
        def player_name(turn):
            if turn == 'X':
                return (player_X_name)
            else:
                return (player_O_name)

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
            
        # Check the winner:
        if count >= 5:
            if theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break
            elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                print_board(theboard)
                print("\nGame Over.\n")
                add_game(player_X_name, player_O_name, player_name(turn))
                print(player_name(turn), "wins")
                break

        # Define the draw:
        if count == 9:
            print("\nGame Over.\n")
            print("It's a draw!")

        # Change the turn after each move:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    print(games)

    # Restart the game:
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theboard[key] = " "

        tictactoe()

# Save csv:
filename = "games.csv"

def read_games():
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Game ID",
            "Player 1",
            "Player 2",
            "Winner"
        ])

games = read_games()

if __name__ == "__main__":
    tictactoe()
    filename = "games.csv"
    games.to_csv(filename)

