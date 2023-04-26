from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
            elif check_winner() == "Tie":
                label.config(text = "Tie")
            elif check_winner() is True:
                label.config(text = players[0] + " wins")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
            elif check_winner() == "Tie":
                label.config(text = "Tie")
            elif check_winner() is True:
                label.config(text = players[1] + " wins")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="Green")
            buttons[row][1].config(bg="Green")
            buttons[row][2].config(bg="Green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="Green")
            buttons[1][column].config(bg="Green")
            buttons[2][column].config(bg="Green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[2][2].config(bg="Green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[2][0].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[0][2].config(bg="Green")
        return True
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text = player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = "white")

window = Tk()
window.title("Tic-tac-toe")

players = ["x", "o"]
player = random.choice(players)

label = Label(text = player + " turn", font = 20)
label.pack(side = "top")

reset_button = Button(text = "Restart", font = 40, command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = 40, width = 5, height = 2, bg = "white",
                                      command = lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].grid(row = row, column = column)

window.mainloop()
