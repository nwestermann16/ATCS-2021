

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
            self.take_minimax_turn(player)
        return

    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player)
        self.place_player(player, row, col)
        self.print_board()
        return







    def minimax(self, player):
        opt_row = -1
        opt_col = -1
        if self.check_win("O") == True:
            score = 10
            return score, None, None

        if self.check_tie():
            score = 0
            return score, None, None

        if self.check_win("X") == True:
            score = -10
            return score, None, None

        if player == "O":
            best = -10
            for row in range(0, 3):
                for col in range(0, 3):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score = self.minimax("X")[0]
                        if best < score:
                            best = score
                            opt_row = row
                            opt_col = col
                        self.place_player("-", row, col)
            return best, opt_row, opt_col
        if player == "X":
            worst = 10
            for r in range(0, 3):
                for c in range(0, 3):
                    if self.board[r][c] == "-":
                        self.place_player(player, r, c)
                        score = self.minimax("O")[0]
                        if worst > score:
                            worst = score
                            opt_row = r
                            opt_col = c
                        self.place_player("-", r, c)

            return worst, opt_row, opt_col

        return

    def check_col_win(self, player):
        # TODO: Check col win


        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True

        if self.board[0][1] == player and player == self.board[1][1] and player == self.board[2][1]:
            return True

        if self.board[0][2] == player == self.board[1][2] == self.board[2][2]:
            return True

        return False

    def check_row_win(self, player):
        # TODO: Check row win
       if self.board[0][0] == player and player == self.board[0][1] and player == self.board[0][2]:
            return True

       if self.board[1][0] == player and player == self.board[1][1] and player == self.board[1][2]:
            return True

       if self.board[2][0] == player and player == self.board[2][1] and player == self.board[2][2]:
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
            if not self.check_win(player1) and not self.check_tie():
                self.take_turn(player2)
        print("Game Over.")
        if self.check_win(player1):
            print("X Wins!")
        if self.check_win(player2):
            print("O Wins!")
        elif self.check_tie():
            print("Tie!")

        return

