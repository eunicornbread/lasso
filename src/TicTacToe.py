from Tkinter import *

class TicTacToe(object):
    def __init__(self):
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.turn = 'X'
        self.has_won = False

        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("308x310")
        

        self.button0 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark0)
        self.button0.grid(row = 0, column = 0)
        self.button1 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark1)
        self.button1.grid(row = 0, column = 1)
        self.button2 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark2)
        self.button2.grid(row = 0, column = 2)
        self.button3 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark3)
        self.button3.grid(row = 1, column = 0)
        self.button4 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark4)
        self.button4.grid(row = 1, column = 1)
        self.button5 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark5)
        self.button5.grid(row = 1, column = 2)
        self.button6 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark6)
        self.button6.grid(row = 2, column = 0)
        self.button7 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark7)
        self.button7.grid(row = 2, column = 1)
        self.button8 = Button(self.window, text = " ", width = 3, height = 1, font = ('Helvetica', '40'), command = self.mark8)
        self.button8.grid(row = 2, column = 2)

        self.window.mainloop()
        # self.print_board()

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print self.board[i][j],
            print

    def check_winner(self):
        row_result = self.check_row()
        if row_result == 0 and self.has_won == False:
            self.button0["bg"] = "red"
            self.button1["bg"] = "red"
            self.button2["bg"] = "red"
            self.has_won = True
        elif row_result == 1 and self.has_won == False:
            self.button3["bg"] = "red"
            self.button4["bg"] = "red"
            self.button5["bg"] = "red"
            self.has_won = True
        elif row_result == 2 and self.has_won == False:
            self.button6["bg"] = "red"
            self.button7["bg"] = "red"
            self.button8["bg"] = "red"
            self.has_won = True

        col_result = self.check_col()
        if col_result == 0 and self.has_won == False:
            self.button0["bg"] = "red"
            self.button3["bg"] = "red"
            self.button6["bg"] = "red"
            self.has_won = True
        elif col_result == 1 and self.has_won == False:
            self.button1["bg"] = "red"
            self.button4["bg"] = "red"
            self.button7["bg"] = "red"
            self.has_won = True
        elif col_result == 2 and self.has_won == False:
            self.button2["bg"] = "red"
            self.button5["bg"] = "red"
            self.button8["bg"] = "red"
            self.has_won = True

        diagonal_result = self.check_diagonal()
        if diagonal_result == 0 and self.has_won == False:
            self.button0["bg"] = "red"
            self.button4["bg"] = "red"
            self.button8["bg"] = "red"
            self.has_won = True
        elif diagonal_result == 2 and self.has_won == False:
            self.button2["bg"] = "red"
            self.button4["bg"] = "red"
            self.button6["bg"] = "red"
            self.has_won = True

    def check_row(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return i
        return -1

    def check_col(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return i
        return -1

    def check_diagonal(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return 0
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return 2
        else:
            return -1

    def mark0(self):
        if self.board[0][0] == 0 and self.has_won == False:
            self.board[0][0] = self.turn
            self.button0["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark1(self):
        if self.board[0][1] == 1 and self.has_won == False:
            self.board[0][1] = self.turn
            self.button1["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark2(self):
        if self.board[0][2] == 2 and self.has_won == False:
            self.board[0][2] = self.turn
            self.button2["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark3(self):
        if self.board[1][0] == 3 and self.has_won == False:
            self.board[1][0] = self.turn
            self.button3["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark4(self):
        if self.board[1][1] == 4 and self.has_won == False:
            self.board[1][1] = self.turn
            self.button4["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark5(self):
        if self.board[1][2] == 5 and self.has_won == False:
            self.board[1][2] = self.turn
            self.button5["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()
    
    def mark6(self):
        if self.board[2][0] == 6 and self.has_won == False:
            self.board[2][0] = self.turn
            self.button6["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()
        
    def mark7(self):
        if self.board[2][1] == 7 and self.has_won == False:
            self.board[2][1] = self.turn
            self.button7["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()

    def mark8(self):
        if self.board[2][2] == 8 and self.has_won == False:
            self.board[2][2] = self.turn
            self.button8["text"] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.check_winner()


instance = TicTacToe()

