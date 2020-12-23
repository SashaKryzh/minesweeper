import tkinter as tk

from constants import *

window = None
frame = None

width = None
height = None
mines = None

board = []


def start_game(difficulty):
    global frame
    width, height, mines = difficulty.value

    frame.destroy()
    frame = tk.Frame()
    frame.pack()

    tk.Button(frame, text='TEST').pack()

    board_frm = tk.Frame(frame)
    board_frm.pack()

    board = [[0 for j in range(width)] for i in range(height)]

    for y in range(height):
        for x in range(width):
            tile = {
                'x': x,
                'y': y,
                'btn': tk.Button(board_frm)
            }

            tile['btn'].grid(row=y, column=x)

            board[y][x] = tile


def home_screen():
    global frame
    frame = tk.Frame(window)
    frame.pack()

    button1 = tk.Button(frame, text='Easy', width=25, height=5,
                        bg='green', fg='black', command=lambda: start_game(Difficulty.EASY))
    button1.pack()

    button2 = tk.Button(frame, text='Medium', width=25, height=5,
                        bg='green', fg='black', command=lambda: start_game(Difficulty.MEDIUM))
    button2.pack()

    button3 = tk.Button(frame, text='Profi', width=25, height=5,
                        bg='green', fg='black', command=lambda: start_game(Difficulty.HARD))
    button3.pack()


if __name__ == '__main__':
    global widnow
    window = tk.Tk()
    window.title("Pythonicway Minesweep")
    home_screen()
    window.mainloop()
