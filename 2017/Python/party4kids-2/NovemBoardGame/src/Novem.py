from tkinter import *
from random import *

# initialize global game state

CurrentNumber = 0
Round = 0
Layer1 = []
Layer2 = []
CurrentPlayer = 1
Player1Score = 0
Player2Score = 0

while len(Layer1) < 9:
    CurrentNumber = randint (1, 9)
    if CurrentNumber not in Layer1:
        Layer1.append(CurrentNumber)

for n in Layer1:
    Layer2.append (10 - n)

# helpers

def insert_line(s):
    TextField.configure (state = "normal")
    TextField.insert (END, s + "\n")
    TextField.see(END)
    TextField.configure (state = "disabled")

def attacker_turn(row):
    if not game_is_running():
        return
    global CurrentHRow
    CurrentHRow = row
    insert_line ("Нападающий выбрал ряд. Теперь выбирает защитник...")
    A.configure (state ="disabled")
    B.configure (state ="disabled")
    C.configure (state ="disabled")
    One.configure (state ="normal")
    Two.configure (state ="normal")
    Three.configure (state ="normal")

def HrowA (Click):
    attacker_turn('A')

def HrowB (Click):
    attacker_turn('B')

def HrowC (Click):
    attacker_turn('C')

def process_square(i, button):
    global Player1Score
    global Player2Score

    if Layer1 [i] == 0:
        if Layer2 [i] == 0:
            insert_line("Нападающему досталась пустая клетка. Не повезло!")
        else:
            CurrentValue = Layer2 [i]
            Layer2 [i] = 0
            if CurrentPlayer == 1:
                Player1Score += CurrentValue
            else:
                Player2Score += CurrentValue
            button.configure (text = "", bg = "black")
            insert_line("Нападающему достаётся плитка со значением " + str(CurrentValue) + "!")
    else:
        CurrentValue = Layer1 [i]
        Layer1 [i] = 0
        if CurrentPlayer == 1:
            Player1Score += CurrentValue
        else:
            Player2Score += CurrentValue
        button.configure (text = Layer2 [i], bg = "grey")
        insert_line("Нападающему достаётся плитка со значением " + str(CurrentValue) + "!")


def defender_turn(column):
    if not game_is_running():
        return
    global Player1Score
    global Player2Score
    CurrentVRow = column
    CurrentSquare = CurrentHRow + CurrentVRow
    if CurrentSquare == "A1":
        process_square(0, A1)
    elif CurrentSquare == "B1":
        process_square(3, B1)
    elif CurrentSquare == "C1":
        process_square(6, C1)
    if CurrentSquare == "A2":
        process_square(1, A2)
    elif CurrentSquare == "B2":
        process_square(4, B2)
    elif CurrentSquare == "C2":
        process_square(7, C2)
    if CurrentSquare == "A3":
        process_square(2, A3)
    elif CurrentSquare == "B3":
        process_square(5, B3)
    elif CurrentSquare == "C3":
        process_square(8, C3)

    One.configure (state = "disabled")
    Two.configure (state = "disabled")
    Three.configure (state = "disabled")
    A.configure (state = "normal")
    B.configure (state = "normal")
    C.configure (state = "normal")
    next_round()

def Vrow1 (Click):
    defender_turn('1')

def Vrow2 (Click):
    defender_turn('2')

def Vrow3 (Click):
    defender_turn('3')


root = Tk()

Border = Button (root, text = "", width = 4, height = 22, bg = "white")
Border.grid (row = 0, column = 4, rowspan = 4)
Border.configure (state = "disabled")
Empty = Button (root, text = "", width = 12, height = 5, bg = "blue", fg = "white")
Empty.grid (row = 0, column = 0)
Empty.configure (state = "disabled")
One = Button (root, text = "1", width = 12, height = 5, bg = "blue", fg = "white")
One.grid (row = 0, column = 1)
One.configure (state = "disabled")
Two = Button (root, text = "2", width = 12, height = 5, bg = "blue", fg = "white")
Two.grid (row = 0, column = 2)
Two.configure (state = "disabled")
Three = Button (root, text = "3", width = 12, height = 5, bg = "blue", fg = "white")
Three.grid (row = 0, column = 3)
Three.configure (state = "disabled")
A = Button (root, text = "A", width = 12, height = 5, bg = "blue", fg = "white")
A.grid (row = 1, column = 0)
# A.configure (state = "disabled")
B = Button (root, text = "B", width = 12, height = 5, bg = "blue", fg = "white")
B.grid (row = 2, column = 0)
# B.configure (state = "disabled")
C = Button (root, text = "C", width = 12, height = 5, bg = "blue", fg = "white")
C.grid (row = 3, column = 0)
# C.configure (state = "disabled")
A1 = Button (root, text = Layer1 [0], width = 12, height = 5, bg = "brown", fg = "white")
A1.grid (row = 1, column = 1)
A1.configure (state = "disabled")
A2 = Button (root, text = Layer1 [1], width = 12, height = 5, bg = "brown", fg = "white")
A2.grid (row = 1, column = 2)
A2.configure (state = "disabled")
A3 = Button (root, text = Layer1 [2], width = 12, height = 5, bg = "brown", fg = "white")
A3.grid (row = 1, column = 3)
A3.configure (state = "disabled")
B1 = Button (root, text = Layer1 [3], width = 12, height = 5, bg = "brown", fg = "white")
B1.grid (row = 2, column = 1)
B1.configure (state = "disabled")
B2 = Button (root, text = Layer1 [4], width = 12, height = 5, bg = "brown", fg = "white")
B2.grid (row = 2, column = 2)
B2.configure (state = "disabled")
B3 = Button (root, text = Layer1 [5], width = 12, height = 5, bg = "brown", fg = "white")
B3.grid (row = 2, column = 3)
B3.configure (state = "disabled")
C1 = Button (root, text = Layer1 [6], width = 12, height = 5, bg = "brown", fg = "white")
C1.grid (row = 3, column = 1)
C1.configure (state = "disabled")
C2 = Button (root, text = Layer1 [7], width = 12, height = 5, bg = "brown", fg = "white")
C2.grid (row = 3, column = 2)
C2.configure (state = "disabled")
C3 = Button (root, text = Layer1 [8], width = 12, height = 5, bg = "brown", fg = "white")
C3.grid (row = 3, column = 3)
C3.configure (state = "disabled")

A.bind ("<Button-1>", HrowA)
B.bind ("<Button-1>", HrowB)
C.bind ("<Button-1>", HrowC)
One.bind ("<Button-1>", Vrow1)
Two.bind ("<Button-1>", Vrow2)
Three.bind ("<Button-1>", Vrow3)

TextField = Text (root, width = 30, height = 18, font = "Verdana 12", wrap = WORD)
TextField.grid (row = 0, column = 5, rowspan = 5)
TextField.insert (END, "Привет, это игра Novem. Первый игрок - нападающий, а второй - защитник. Нападающий тайно выбирает горизонтальный ряд (A, B или C), а защитник, тоже тайно, после него выбирает вертикальный ряд (1, 2 или 3). Нападающий забирает пластинку на пересечении выбранных рядов, а число на ней прибавляется к счёту игрока. Потом они меняются местами, и это происходит до тех пор, пока не опустеет вертикальный или горизонтальный ряд. Побеждает тот, кто наберёт больше очков.\n")

def game_is_running():
    return (Layer2 [0] != 0 or Layer2 [3] != 0 or Layer2 [6] != 0) and (Layer2 [1] != 0 or Layer2 [4] != 0 or Layer2 [7] != 0) and (Layer2 [2] != 0 or Layer2 [5] != 0 or Layer2 [8] != 0) and (Layer2 [0] != 0 or Layer2 [1] != 0 or Layer2 [2] != 0) and (Layer2 [3] != 0 or Layer2 [4] != 0 or Layer2 [5] != 0) and (Layer2 [6] != 0 or Layer2 [7] != 0 or Layer2 [8] != 0)

def next_round():
    global Round, CurrentPlayer
    Round += 1
    if not game_is_running():
        A.configure (state ="disabled")
        B.configure (state ="disabled")
        C.configure (state ="disabled")
        One.configure (state ="disabled")
        Two.configure (state ="disabled")
        Three.configure (state ="disabled")
        insert_line("Игра окончена! Первый игрок набрал {} очков, а второй – {}".format(Player1Score, Player2Score))
        return
    if Round % 2 == 1:
        CurrentPlayer = 1
    else:
        CurrentPlayer = 2
    insert_line("Нападающий выбирает ряд...")
    root.update ()

next_round()

root.mainloop ()
