class TicTacToeSimple(object):
    def __init__(self):
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.turn = 'x'

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print self.board[i][j],
            print

    def play_game(self):
        count = 0
        while True:
            if count == 9:
                print "It's a draw!"
                self.print_board()
                break

            count += 1
            self.print_board()
            print "Player turn: " + self.turn
            position = input("Enter position number >>")
            self.board[position/3][position%3] = self.turn
            if self.turn == 'x':
                self.turn = 'o'
            else:
                self.turn = 'x'
            
            if self.check_row() == 'x' or self.check_col() == 'x' or self.check_diagonal() == 'x':
                print "Player x wons!"
                self.print_board()
                break
            elif self.check_row() == 'o' or self.check_col() == 'o' or self.check_diagonal() == 'o':
                print "Player o wons!"
                self.print_board()
                break

    
    def check_row(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        return None

    def check_col(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        return None

    def check_diagonal(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        else:
            return None

game = TicTacToeSimple()
game.play_game()