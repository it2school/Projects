from random import*
from tkinter import*
from time import*
from tkinter.messagebox import*

#kletki = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
rect_color = 'yellow'
num_color = 'red'
screen_color = '#003300'

root = Tk()
root.title('2048 - game')
        
def calculate_score():
    score = 0
    for kletka in kletki:
        if kletka != ' ':
            score += int(kletka)
    return score

def draw(kl):
    try:
        screen.delete('all')
        for q in range(4):
            for z in range(4):
                screen.create_rectangle(z*150,q*150,(z+1)*150,(q+1)*150,outline=rect_color)
                screen.create_text((z*150)+60,(q*150)+75,text=kl[(q*4)+z],font="Verdana 40",anchor='center' ,justify=CENTER,fill=num_color)
    except:
        pass
    
def check():
    if '2048' in kletki:
        resp = askretrycancel('Поздравляю!', 'Вы победили, можно начать заново.')
        if resp:
            screen.destroy()
            score.destroy()
            back.destroy()
            play_game()
        else:
            screen.destroy()
            score.destroy()
            back.destroy()
            menu()
    elif ' ' not in kletki:
        resp = askretrycancel('Увы!', 'Вы проиграли, можно начать заново.')
        if resp:
            screen.destroy()
            score.destroy()
            back.destroy()
            play_game()
        else:
            screen.destroy()
            score.destroy()
            back.destroy()
            menu()


#реакция на события:

def move_up(ev):
    for x in range(4):
        for i in range(len(kletki)):
            if i >= 4 and kletki[i] != ' ':
                if kletki[i-4] == ' ':
                    kletki[i-4] = kletki[i]
                    kletki[i] = ' '
                if kletki[i] == kletki[i-4]:
                    kletki[i-4] = str(int(kletki[i]) * 2)
                    kletki[i] = ' '
                    break
        root.update_idletasks()
        sleep(0.03)
        draw(kletki)
    root.update_idletasks()
    sleep(0.3)
    for ind in kletki:
        val = randint(0, 15)
        if kletki[val] == ' ':
            if randint(0, 100) <= 70:
                kletki[val] = '2'
            else:
                kletki[val] = '4'
            break
    score['text'] = 'Score: %s' % (calculate_score())
    draw(kletki)
    check()


def move_left(ev):
    for x in range(4):
        for i in range(len(kletki)):
            if i % 4 != 0 and kletki[i] != ' ':
                if kletki[i-1] == ' ':
                    kletki[i-1] = kletki[i]
                    kletki[i] = ' '
                if kletki[i] == kletki[i-1]:
                    kletki[i-1] = str(int(kletki[i]) * 2)
                    kletki[i] = ' '
                    break
        root.update_idletasks()
        sleep(0.03)
        draw(kletki)
    root.update_idletasks()
    sleep(0.3)
    for ind in kletki:
        val = randint(0, 15)
        if kletki[val] == ' ':
            if randint(0, 100) <= 70:
                kletki[val] = '2'
            else:
                kletki[val] = '4'
            break
    score['text'] = 'Score: %s' % (calculate_score())
    draw(kletki)
    check()


def move_down(ev):
    for x in range(4):
        for i in range(len(kletki)):
            if len(kletki)-(i+1) <= 11 and kletki[len(kletki)-(i+1)] != ' ':
                if kletki[len(kletki)-(i-3)] == ' ':
                    kletki[len(kletki)-(i-3)] = kletki[len(kletki)-(i+1)]
                    kletki[len(kletki)-(i+1)] = ' '
                if kletki[len(kletki)-(i-3)] == kletki[len(kletki)-(i+1)]:
                    kletki[len(kletki)-(i-3)] = str(int(kletki[len(kletki)-(i+1)]) * 2)
                    kletki[len(kletki)-(i+1)] = ' '
                    break
        root.update_idletasks()
        sleep(0.03)
        draw(kletki)
    root.update_idletasks()
    sleep(0.3)
    for ind in kletki:
        val = randint(0, 15)
        if kletki[val] == ' ':
            if randint(0, 100) <= 70:
                kletki[val] = '2'
            else:
                kletki[val] = '4'
            break
    score['text'] = 'Score: %s' % (calculate_score())
    draw(kletki)
    check()


def move_right(ev):
    for x in range(4):
        for i in range(len(kletki)):
            if ((len(kletki)-(i+1))-3) % 4 != 0 and kletki[len(kletki)-(i+1)] != ' ':
                if kletki[len(kletki)-(i)] == ' ':
                    kletki[len(kletki)-(i)] = kletki[len(kletki)-(i+1)]
                    kletki[len(kletki)-(i+1)] = ' '
                if kletki[len(kletki)-(i)] == kletki[len(kletki)-(i+1)]:
                    kletki[len(kletki)-(i)] = str(int(kletki[len(kletki)-(i+1)]) * 2)
                    kletki[len(kletki)-(i+1)] = ' '
                    break
        root.update_idletasks()
        sleep(0.03)
        draw(kletki)
    root.update_idletasks()
    sleep(0.3)
    for ind in kletki:
        val = randint(0, 15)
        if kletki[val] == ' ':
            if randint(0, 100) <= 70:
                kletki[val] = '2'
            else:
                kletki[val] = '4'
            break
    score['text'] = 'Score: %s' % (calculate_score())
    draw(kletki)
    check()


#запуск игры и обработка событий
def play_game():
    global back
    global screen
    global kletki
    global score
    play.destroy()
    info.destroy()
    exit.destroy()
    help.destroy()
    settings.destroy()
    screen = Canvas(root, width = 600, height = 600, bg = screen_color)
    back = Button(root, text = 'Назад', command = go_back_b, font = 7, width = 10, height = 1)
    score = Label(root, text = 'Score: 4', font = 7, width = 10, height = 1)
    kletki = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    screen.grid()
    screen.focus_set()
    back.grid(sticky = 'w')
    score.grid(sticky = 'e')
    draw(kletki)
    kletki[randint(0, 15)] = '2'
    for ind in kletki:
        val = randint(0, 15)
        if kletki[val] == ' ':
            kletki[val] = '2'
            break
    draw(kletki)
    screen.bind("w", move_up)
    screen.bind("a", move_left)
    screen.bind("s", move_down)
    screen.bind("d", move_right)
    
def go_back_a():
    back.destroy()
    txt.destroy()
    menu()

def go_back_b():
    resp = askyesno('Вы увеенны?', 'Вы точно хотите выйти из игры?')
    if resp:
        screen.destroy()
        score.destroy()
        back.destroy()
        menu()
    
def go_back_c():
    if (screen_col.get() != num_col.get() or screen_col.get() == '') and (screen_col.get() != rect_col.get() or rect_col.get() == '') and (rect_col.get() != num_col.get() or num_col.get() == ''):
        global screen_color
        global num_color
        global rect_color
        if screen_col.get() != '':
            screen_color = screen_col.get()
        if num_col.get() != '':
            num_color = num_col.get()
        if rect_col.get() != '':
            rect_color = rect_col.get()
        back.destroy()
        num_col.destroy()
        num_txt.destroy()
        screen_col.destroy()
        screen_txt.destroy()
        txt.destroy()
        col_set.destroy()
        enter.destroy()
        control_set.destroy()
        control_txt.destroy()
        #check1.destroy()
        #check2.destroy()
        menu()
    else:
        pass

def show_settings():
    global back
    global check1
    global check2
    global num_col
    global screen_col
    global col_set
    global rect_col
    global txt
    global screen_txt
    global num_txt
    global rect_txt
    global enter
    global control_set
    global control_txt
    #global control_wasd
    #global control_arrows
    play.destroy()
    settings.destroy()
    info.destroy()
    help.destroy()
    exit.destroy()
    col_set = Frame(root, bd = 5)
    txt = Label(col_set, text = 'Настройки цвета', font = 8)
    screen_txt = Label(col_set, text = 'Цвет поля(%s): ' % (screen_color), font = 4)
    screen_col = Entry(col_set)
    num_txt = Label(col_set, text = 'Цвет чисел(%s): ' % (num_color), font = 4)
    num_col = Entry(col_set)
    rect_txt = Label(col_set, text = 'Цвет линий(%s): ' % (rect_color), font = 4)
    rect_col = Entry(col_set)
    #control_wasd = IntVar()
    #control_arrows = IntVar()
    enter = Label(root, text = '')
    control_set = Frame(root, bd = 5)
    control_txt = Label(control_set, text = 'Настройки управления', font = 4)
    #check1 = Checkbutton(control_set, text = 'Стрелками', variable=control_arrows, onvalue=1, offvalue=0)
    #check2 = Checkbutton(control_set, text = 'W, A, S, D', variable=control_wasd, onvalue=1, offvalue=0)
    back = Button(root, text = 'Назад', command = go_back_c, font = 7, width = 10, height = 1)
    col_set.grid()
    txt.grid(row = 0, padx = (110, 0))
    screen_txt.grid(row = 1)
    screen_col.grid(row = 1, column = 1)
    num_txt.grid(row = 2)
    num_col.grid(row = 2, column = 1)
    rect_txt.grid(row = 3)
    rect_col.grid(row = 3, column = 1)
    enter.grid()
    #control_set.grid()
    #control_txt.grid()
    #check1.grid()
    #check2.grid()
    back.grid(padx = (0, 270))

def show_info():
    global back
    global txt
    play.destroy()
    info.destroy()
    help.destroy()
    exit.destroy()
    settings.destroy()
    txt = Label(root, text = 'Версия 1.0\nCopyright © 2017 Levsoft. All rights reserved.\nРазработчик - Тартаковский Лев\n', font = 5)
    back = Button(root, text = 'Назад', command = go_back_a, font = 7, width = 10, height = 1)
    txt.pack()
    back.pack(side = LEFT)

def show_help():
    global txt
    global back
    play.destroy()
    settings.destroy()
    info.destroy()
    help.destroy()
    exit.destroy()
    txt = Label(root, text = 'Ваша цель - цифра 2048. В начале игры на поле два числа 2.\nВы можете перемещать числа вверх,вниз, направо и налево\nиспользуя клавишы w, a, s, d.\nДва одинаковых числа сталкнувшись образуют их сумму\n', font = 5)
    back = Button(root, text = 'Назад', command = go_back_a, font = 7, width = 10, height = 1)
    txt.pack()
    back.pack(side = LEFT)

#меню программы
def menu():
    global play
    global settings
    global help
    global info
    global exit
    play = Button(root, text = 'Играть', command = play_game, font = 10, width = 20, height = 3)
    settings = Button(root, text = 'Настройки', command = show_settings, font = 10, width = 20, height = 3)
    help = Button(root, text = 'Помощь', command = show_help, font = 10, width = 20, height = 3)
    info = Button(root, text = 'Информация', command = show_info, font = 10, width = 20, height = 3)
    exit = Button(root, text = 'Выход', command = root.destroy, font = 10, width = 20, height = 3)
    play.pack()
    settings.pack()
    help.pack()
    info.pack()
    exit.pack()

menu()
root.mainloop()