import random

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        self.board.append(["-", "-", "-"])
        self.board.append(["-", "-", "-"])
        self.board.append(["-", "-", "-"])

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to tic tac toe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to three in a row wins.")
        return

    def print_board(self):
        # TODO: Print the board
        print("   0  1  2")
        for i in range(0,3):
            s = ""
            for y in range (0,3):
                s = s + "  " + self.board[i][y]
            print(str(i) + s)
        return



    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid

        while row > 2 or col > 2 or self.board[row][col] != "-":
            return False
        return

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        input_row = input("Enter a row:")
        input_col = input("Enter a col:")
        while self.is_valid_move(int(input_row), int(input_col)) == False:
            print("Please enter a valid move.")
            input_row = input("Enter a row:")
            input_col = input("Enter a col:")
            self.is_valid_move(int(input_row), int(input_col))
        self.place_player(player, int(input_row), int(input_col))
        self.print_board()

        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s turn.")
        if player == "X":
            self.take_manual_turn(player)
        if player == "O":
            self.take_random_turn(player)
        return

    def take_random_turn(self, player):
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)
        while self.is_valid_move(row, col) == False:
            row = random.randrange(0, 3)
            col = random.randrange(0, 3)
        self.place_player(player, row, col)
        self.print_board()

        return


    def check_col_win(self, player):
        # TODO: Check col win


        if self.board[0][0] == player == self.board[1][0] == self.board[2][0]:
            return True

        if self.board[0][1] == player == self.board[1][1] == self.board[2][1]:
            return True

        if self.board[0][2] == player == self.board[1][2] == self.board[2][2]:
            return True

        return False

    def check_row_win(self, player):
        # TODO: Check row win


       if self.board[0][0] == player == self.board[0][1] == self.board[0][2]:
            return True

       if self.board[1][0] == player == self.board[1][1] == self.board[1][2]:
            return True


       if self.board[2][0] == player == self.board[2][1] == self.board[2][2]:
            return True

       return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win

        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True




        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True:
            print(player + " wins!")
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        count = 0
        for r in range(0, 3):
            for c in range(0, 3):
                if self.board[r][c] != '-':
                    count = count + 1
        if count == 9:
            return True

        return False

    def play_game(self):
        # TODO: Play game
        player1 = "X"
        player2 = "O"
        self.print_instructions()
        self.print_board
        while not self.check_win(player1) and not self.check_tie() and not self.check_win(player2):
                self.take_turn(player1)
                self.check_win(player1)
                self.take_turn(player2)
                self.check_win(player2)

        print("Game Over.")
        return

