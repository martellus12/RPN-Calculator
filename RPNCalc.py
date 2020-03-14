import tkinter as tk
from tkinter import font

HEIGHT = 300
WIDTH = 500
END = 1000

calc = tk.Tk()
calc.title('RPN Calculator')


#Numberical Key Operation
def btn_click(num):
    current = e0.get()
    e0.delete(0, END)
    e0.insert(0, current+num)

#Define mathematical operation function:
def operation(op):
    if op == '+':
        result = float(e1.get())+float(e0.get())
    elif op == '-':
        result = float(e1.get())-float(e0.get())
    elif op == 'X':
        result = float(e1.get())*float(e0.get())
    elif op == '/':
        if float(e0.get()) == False:                #DIVIDE BY ZERO CASE
            e0.insert(0, 'ERR: divide by zero')
        else:
            result = float(e1.get())/float(e0.get())
            
    e0.delete(0,END)
    e1.delete(0,END)
    e0.insert(0,result)
    

#Register Stack Movement Buttons
def stack_up():
    e2.insert(0, e1.get())
    e1.delete(0, END)
    e1.insert(0, e0.get())
    e0.delete(0,END)
    
def stack_down():
    if e2.get() and e0.get() and not e1.get():
        e1.insert(0,e2.get())
        e2.delete(0,END)

    else:
        e0.delete(0,END)
        e0.insert(0,e1.get())
        e1.delete(0, END)
        e1.insert(0, e2.get())
        e2.delete(0,END)
    
    
#Create widgets:
canvas = tk.Canvas(calc, height = HEIGHT, width = WIDTH)
canvas.pack()

calc_label = tk.Label(canvas, text = 'REGISTERS                INPUT', font = ('ARIAL BOLD', 16), anchor = 'sw')
calc_label.place(relheight = 0.2, relwidth = 0.6, relx = 0, rely = 0)

#frame1 will contain the entry boxes
frame1 = tk.Frame(canvas, highlightbackground = 'black', highlightthickness = 1)
frame1.place(relwidth = 0.4, relheight = .8, relx = 0, rely = 0.2)

#frame2 will contain the buttons
frame2 = tk.Frame(canvas, highlightbackground = 'black', highlightthickness = 1)
frame2.place(relwidth = 0.6, relheight = .8, relx = 0.4, rely = 0.2)

#e0 is the result register
e0 = tk.Entry(frame1, bd = 5, font = ('Courier',12), justify = 'right')
e0.place(relx = 0 , rely = 0.6, relheight = 0.2, relwidth = 0.4)
e0label = tk.Label(frame1, text = 'R0')
e0label.place(relx = 0.4 , rely = 0.6, relheight = 0.2, relwidth = 0.2)

#e1 is the register above the results register in the stack
e1 = tk.Entry(frame1, bd = 5, font = ('Courier',12), justify = 'right')
e1.place(relx = 0 , rely = 0.25, relheight = 0.2, relwidth = 0.4)
e1label = tk.Label(frame1, text = 'R1')
e1label.place(relx = 0.4 , rely = 0.25, relheight = 0.2, relwidth = 0.2)

#e2 is the top register on the stack
e2 = tk.Entry(frame1, bd = 5, font = ('Courier',12), justify = 'right')
e2.place(relx = 0 , rely = 0, relheight = 0.2, relwidth = 0.4)
e2label = tk.Label(frame1, text = 'R2')
e2label.place(relx = 0.4, rely = 0, relheight = 0.2, relwidth = 0.2)

#These are the buttons that move numbers up and down the stack
button_up = tk.Button(frame1, text = '↑', bd = 5, command = stack_up)
button_down = tk.Button(frame1, text = '↓', bd = 5, command = stack_down)

button_up.place(relx = 0.7 , rely = 0.1, relheight = 0.3, relwidth = 0.2)
button_down.place(relx = 0.7 , rely = 0.5, relheight = 0.3, relwidth = 0.2)


#Number Buttons
button1 = tk.Button(frame2, text = '1', bd = 3,command = lambda: btn_click('1'))
button2 = tk.Button(frame2, text = '2', bd = 3,command = lambda: btn_click('2'))
button3 = tk.Button(frame2, text = '3', bd = 3,command = lambda: btn_click('3'))
button4 = tk.Button(frame2, text = '4', bd = 3,command = lambda: btn_click('4'))
button5 = tk.Button(frame2, text = '5', bd = 3,command = lambda: btn_click('5'))
button6 = tk.Button(frame2, text = '6', bd = 3,command = lambda: btn_click('6'))
button7 = tk.Button(frame2, text = '7', bd = 3,command = lambda: btn_click('7'))
button8 = tk.Button(frame2, text = '8', bd = 3,command = lambda: btn_click('8'))
button9 = tk.Button(frame2, text = '9', bd = 3,command = lambda: btn_click('9'))
button0 = tk.Button(frame2, text = '0', bd = 3,command = lambda: btn_click('0'))
buttonDot = tk.Button(frame2, text = '.', bd = 3, command = lambda: btn_click('.'), bg = '#68BCFF')

#Button Placement
button1.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 0.2)
button2.place(relx = .3, rely = 0, relwidth = 0.3, relheight = 0.2)
button3.place(relx = .6, rely = 0, relwidth = 0.3, relheight = 0.2)
button4.place(relx = 0, rely = .2, relwidth = 0.3, relheight = 0.2)
button5.place(relx = .3, rely = .2, relwidth = 0.3, relheight = 0.2)
button6.place(relx = .6, rely = .2, relwidth = 0.3, relheight = 0.2)
button7.place(relx = 0, rely = .4, relwidth = 0.3, relheight = 0.2)
button8.place(relx = 0.3, rely = .4, relwidth = 0.3, relheight = 0.2)
button9.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.2)
button0.place(relx = 0.3, rely = .6, relwidth = 0.3, relheight = 0.2)
buttonDot.place(relx = .9, rely = 0.4, relwidth = 0.1, relheight = 0.2)

#Operation Buttons
button_add = tk.Button(frame2, text = '+', bd = 3, command = lambda: operation('+'))
button_sub = tk.Button(frame2, text = '-', bd = 3, command = lambda: operation('-'))
button_clr = tk.Button(frame2, text = 'CLR', bd = 3, command = lambda: e0.delete(0,1000))
button_mult = tk.Button(frame2, text = 'X', bd = 3, command = lambda: operation('X'))
button_div = tk.Button(frame2, text = '/',  bd = 3, command = lambda: operation('/'))

#Op Button Placement
button_add.place(relx = 0, rely = .6, relwidth = 0.3, relheight = 0.2)
button_sub.place(relx = 0.6, rely = .6, relwidth = 0.3, relheight = 0.2)
button_mult.place(relx = 0, rely = .8, relwidth = 0.3, relheight = 0.2)
button_clr.place(relx = 0.3, rely = .8, relwidth = 0.3, relheight = 0.2)
button_div.place(relx = 0.6, rely = .8, relwidth = 0.3, relheight = 0.2)


calc.mainloop()
