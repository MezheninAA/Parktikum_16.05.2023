#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.current_turn = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)
    def draw_board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, fill="white")
        for i in range(1, 3):
            self.canvas.create_line(i * 100, 0, i * 100, 300)
            self.canvas.create_line(0, i * 100, 300, i * 100)
    def handle_click(self, event):
        x, y = event.x, event.y
        row, col = y // 100, x // 100
        if self.board[row][col] == "":
            self.board[row][col] = self.current_turn
            self.draw_symbol(row, col, self.current_turn)
            if self.check_win():
                self.show_win_message()
            elif self.check_tie():
                self.show_tie_message()
            else:
                self.current_turn = "O" if self.current_turn == "X" else "X"
    def draw_symbol(self, row, col, symbol):
        x, y = col * 100 + 50, row * 100 + 50
        if symbol == "X":
            self.canvas.create_line(x - 40, y - 40, x + 40, y + 40, width=2)
            self.canvas.create_line(x + 40, y - 40, x - 40, y + 40, width=2)
        else:
            self.canvas.create_oval(x - 40, y - 40, x + 40, y + 40, width=2)
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
    def show_win_message(self):
        winner = "Крестики" if self.current_turn == "1" else "Нолики"
        message = f"{winner} выиграли!"
        self.show_message(message)
    def show_tie_message(self):
        message = "Ничья!"
        self.show_message(message)
    def show_message(self, message):
        self.canvas.create_rectangle(0, 150, 300, 200, fill="white")
        self.canvas.create_text(150, 175, text=message, font=("Arial", 16))
root = tk.Tk()
game = Game(root)
root.mainloop()


# In[ ]:





# In[ ]:




