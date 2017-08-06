import tkinter 
from tkinter import messagebox
from tkinter import *



def show_result(): 
    messagebox.showinfo("calcylator",str("game over"))

def Button1_click():
    my_entry.insert(END,'1')

def Button2_click():
    my_entry.insert(END,'2')

def Button3_click():
    my_entry.insert(END,'3')

def Button4_click():
    my_entry.insert(END,'4')

def Button5_click():
    my_entry.insert(END,'5')

def Button6_click():
    my_entry.insert(END,'6')

def Button7_click():
    my_entry.insert(END,'7')

def Button8_click():
    my_entry.insert(END,'8')

def Button9_click():
    my_entry.insert(END,'9')

def Button10_click():
    my_entry.insert(END,'=')

def Button11_click():
    my_entry.insert(END,'+')

def Button12_click():
    my_entry.insert(END,'-')

def Button13_click():
    my_entry.insert(END,'0')

def Button14_click():
    my_entry.insert(END,'/')

def Button15_click():
    my_entry.insert(END,'.')

def Button16_click():
    my_entry.insert(END,'*')

def get_result():
    result = my_entry.get()

    conteins_minus = result.find('-')
    if conteins_minus > 0:
        minus(result)

    conteins_delit = result.find('/')
    if conteins_delit > 0:
        delit(result)

    conteins_multiply = result.find('*')
    if conteins_multiply > 0:
        multiply(result)
    
    conteins_plus = result.find('+')
    if conteins_plus > 0:
        sum(result)

    

def sum(text):
    operation= text.find('+')
    first_number = text[0:operation]
    print(first_number)
    second_number = text[operation+1:]
    print(second_number)
    text =float(first_number) + float(second_number)
    my_entry.delete(0, END)
    my_entry.insert(0, text)

def  minus(text):
    operation= text.find('-')
    first_number = text[0:operation]
    print(first_number)
    second_number = text[operation+1:]
    print(second_number)
    text =float(first_number) - float(second_number)
    my_entry.delete(0, END)
    my_entry.insert(0, text)


def delit(text):
    operation= text.find('/')
    first_number = text[0:operation]
    print(first_number)
    second_number = text[operation+1:]
    print(second_number)
    text =float(first_number) / float(second_number)
    my_entry.delete(0, END)
    my_entry.insert(0, text)

def multiply(text):
    operation= text.find('*')
    first_number = text[0:operation]
    print(first_number)
    second_number = text[operation+1:]
    print(second_number)
    text =float(first_number) * float(second_number)
    my_entry.delete(0, END)
    my_entry.insert(0, text)
    
 
def destroy():
    window.destroy() 

window = tkinter.Tk() 

frame1 = Frame(window)
frame1.grid()

my_entry = tkinter.Entry(frame1, bd = 5, font="Helvetica 20 bold",  width = 20) 
my_entry.grid(row=0,column=0) 

frame2 = Frame(window)
frame2.grid()


b1 = tkinter.Button(frame2,text = "1",command = Button1_click, width = 10, height = 5) 
b1.grid(row=1, column=1) 
b2 = tkinter.Button(frame2,text = "2",command = Button2_click, width = 10, height = 5) 
b2.grid(row=1,column=2) 
b3 = tkinter.Button(frame2,text = "3",command = Button3_click, width = 10, height = 5) 
b3.grid(row=1,column=3) 
b4 = tkinter.Button(frame2,text = "4",command = Button4_click, width = 10, height = 5) 
b4.grid(row=2,column=1) 
b5 = tkinter.Button(frame2,text = "5",command = Button5_click, width = 10, height = 5) 
b5.grid(row=2,column=2) 
b6 = tkinter.Button(frame2,text = "6",command = Button6_click, width = 10, height = 5) 
b6.grid(row=2,column=3) 
b7 = tkinter.Button(frame2,text = "7",command = Button7_click, width = 10, height = 5) 
b7.grid(row=3,column=1) 
b8 = tkinter.Button(frame2,text = "8",command = Button8_click, width = 10, height = 5) 
b8.grid(row=3,column=2) 
b9 = tkinter.Button(frame2,text = "9",command = Button9_click, width = 10, height = 5) 
b9.grid(row=3,column=3) 
b10 =tkinter.Button(frame2,text = ".",command = Button15_click, width = 10, height = 5) 
b10.grid(row=4,column=1) 
b11 = tkinter.Button(frame2,text = "0",command = Button13_click, width = 10, height = 5) 
b11.grid(row=4,column=2) 
b12 = tkinter.Button(frame2,text = "=",command = get_result, width = 10, height = 5, fg="red") 
b12.grid(row=4,column=3) 
b13 = tkinter.Button(frame2,text = "+",command = Button11_click, width = 10, height = 5) 
b13.grid(row=4,column=4) 
b14 = tkinter.Button(frame2,text = "-",command =Button12_click, width = 10, height = 5) 
b14.grid(row=3,column=4) 
b15 = tkinter.Button(frame2,text = "/",command =  Button14_click, width = 10, height = 5) 
b15.grid(row=2,column=4) 
b16 = tkinter.Button(frame2,text = "*",command = Button16_click, width = 10, height = 5) 
b16.grid(row=1,column=4) 





window.mainloop()