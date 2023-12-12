import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class HumanPlayer(Player):
    def get_move(self, board):
        row, col = map(int, input(f"Enter row and column numbers to place '{self.symbol}': ").split())
        return row - 1, col - 1

class ComputerPlayer(Player):
    def get_move(self, board):
        # Implement the computer AI strategy here (e.g., random move or minimax)
        # For a simple AI, you can randomly choose an empty spot.
        empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
        return random.choice(empty_spots)
    
class TicTacToe:

    def __init__(self):
        self.board = []
# creating a board using a 2-dimensional array and initialising each element as empty
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
        for i in range(3):
            for j in range(3):
                self.board[i][j] = '-'

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)
# checking whether a player has won or not
#  checking for all the rows, columns, and two diagonals

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        # Ask the user if they want to play against the computer or another person.
        player_choice = input("Enter '1' to play against the computer or '2' to play against another person: ")
        
        if player_choice == '1':
            player1 = HumanPlayer('X')
            player2 = ComputerPlayer('O')
        else:
            player1 = HumanPlayer('X')
            player2 = HumanPlayer('O')

        current_player = player1

        while True:
            print(f"Player {current_player.symbol}'s turn")
            self.show_board()

            if current_player == player1:
                move = player1.get_move(self.board)
            else:
                move = player2.get_move(self.board)

            row, col = move

            if self.board[row][col] == '-':
                self.fix_spot(row, col, current_player.symbol)
            else:
                print("Invalid move. Try again.")
                continue

            if self.is_player_win(current_player.symbol):
                self.show_board()
                print(f"Player {current_player.symbol} wins the game!")
                break

            if self.is_board_filled():
                self.show_board()
                print("Match Draw!")
                break

            current_player = player2 if current_player == player1 else player1

        print()

# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
