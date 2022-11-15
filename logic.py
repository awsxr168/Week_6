class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    
    # Draw the board:
    def __str__(self):
        s = '-------\n'
        for row in self.board:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + '|\n-------\n'
        return s

    # Define the winner:
    def get_winner(self):
        winner = ""
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            winner = self.board[0][0]
            return winner
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            winner = self.board[0][1]
            return winner
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            winner = self.board[0][2]
            return winner
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            winner = self.board[0][0]
            return winner
        if self.board[1][1] == self.board[1][1] == self.board[1][2]:
            winner = self.board[1][1]
            return winner
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            winner = self.board[2][0]
            return winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            winner = self.board[0][0]
            return winner
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            winner = self.board[0][2]
            return winner
        else:
            return "It was a draw"

    # Define the move:
    def move_board(self, row, col):
        if Game.current_player == Human():
            row = int(input("Input the row:"))
            col = int(input("Input the col:"))
            return self.board[row][col]
        else:
            import random
            row = random.randint(0,3)
            col = random.randint(0,3)
            return self.board[row][col]


# Define class Game:
class Game:
    def __init__(self, playerX, playerO):
        self.board = Board()
        self.playerX = playerX
        self.playerO = playerO
        self.current_player = playerO
    
    # Define game modes (human v human / human v bot / bot v bot):
    def mode(self):
        if input("Input '1' to start human vs human; Input '2' to start human vs bot; Input '3' to start bot vs bot;") == 1:
            playerX = Human()
            playerO = Human()
        if input("Input '1' to start human vs human; Input '2' to start human vs bot; Input '3' to start bot vs bot;") == 2:
            playerX = Human()
            playerO = Bot()
        if input("Input '1' to start human vs human; Input '2' to start human vs bot; Input '3' to start bot vs bot;") == 3:
            playerX = Bot()
            playerO = Bot()

    # Run the game:
    def run(self):
        board = Board()
        winner = None
        while winner == None:
            Board.move_board
            Game.change_player
            if winner != None:
                break
        print(Board.get_winner)
            
    # Change the player:
    def change_player(self, playerX, playerO):
        if current_player == playerO:
            current_player = playerX
        elif current_player == playerX:
            current_player = playerO


class Human:
    def get_move(self, board):
        Board.move_board


class Bot:
    def get_move(self, board):
        Board.move_board
