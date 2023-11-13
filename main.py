import tkinter as tk
from tkinter import ttk
from math import sqrt, pi, sin, cos, tan

app_title = 'Calculosos v2.01'
info = 'Calculosos v2.01 - © 2021 by Paul Koops'
current_entry = ''
welcome_text = 'Welcome to Calculosos!'
div_by_zero = 'You can not divide by zero.'
error = 'Error!'


# ----- FUNCTIONS -----
def click_button(button):
    global current_entry
    calc_display.configure(foreground='black')
    current_entry += str(button)
    helper.set(current_entry)

    try:
        evaluation = eval(current_entry)
        if int(evaluation) == float(evaluation):
            evaluation = int(evaluation)

    except SyntaxError:
        evaluation = ''

    helper.set(current_entry)
    display.set(evaluation)


def click_equals():
    global current_entry
    current_entry += '='
    helper.set(current_entry)

    try:
        calc_display.configure(foreground='black')
        evaluation = eval(current_entry[:-1])

        if int(evaluation) == float(evaluation):
            evaluation = int(evaluation)

        current_entry = str(evaluation)
        display.set(evaluation)

    except SyntaxError:
        calc_display.configure(foreground='red')
        display.set(error)

    except ZeroDivisionError:
        calc_display.configure(foreground='red')
        helper.set(div_by_zero)
        display.set(error)


def click_reset():
    global current_entry
    current_entry = ''
    helper.set(welcome_text)
    display.set(0)


def click_delete():
    global current_entry
    current_entry = current_entry[:-1]
    helper.set(current_entry)

    try:
        evaluation = eval(current_entry)
        if int(evaluation) == float(evaluation):
            evaluation = int(evaluation)

    except SyntaxError:
        evaluation = ''

    helper.set(current_entry)
    display.set(evaluation)


def click_info():
    helper.set(info)


def key_handler(event):
    key = event.keysym
    #print(key)
    if key in '1234567890':
        click_button(key)
    elif key in ['asterisk', 'x', 'X']:
        click_button('*')
    elif key == 'slash':
        click_button('/')
    elif key == 'plus' or key == 'equal':
        click_button('+')
    elif key == 'Multi_key':
        click_button('**')
    elif key == 'minus':
        click_button('-')
    elif key == 'parenleft':
        click_button('(')
    elif key == 'parenright':
        click_button(')')
    elif key == 'period' or key == 'comma':
        click_button('.')
    elif key == 'Return':
        click_equals()
    elif key == 'BackSpace':
        click_delete()
    elif key in 'cC':
        click_reset()
    elif key in 'iI':
        click_info()


# ----- CALCULATOR WINDOW -----
root = tk.Tk()
root.configure(background='grey25')
root.resizable(False, False)  # Window can not be resized or maximised
root.title(app_title)
root.bind("<Key>", key_handler)
root.iconbitmap('Img/calculator_icon.ico')

# ----- FONTS -----
FONT_DISPLAY = ('Courier', 24, 'bold')
FONT_HELPER = ('Courier', 12, 'normal')

# ----- STYLES -----
s = ttk.Style()
#print(s.theme_names())
s.theme_use('default')
s.configure('TButton', font='Arial 14 bold', width=6, background='grey25', foreground='dark orange')
s.configure('Op.TButton', font='Arial 12 normal', background='steel blue', foreground='black')
s.configure('Equals.TButton', font='Arial 14 bold', background='dark orange', foreground='black')
s.configure('Info.TButton', font='Courier 10 italic')

# ----- CALCULATOR -----
# HELPER  DISPLAY
# row 0 - items
helper = tk.StringVar()  # Helper Display
calc_helper = ttk.Label(root, font=FONT_HELPER, textvariable=helper, background='light grey', padding=15, anchor='e')
calc_helper.grid(row=0, columnspan=5, sticky='E W', padx=5, pady=5)

# MAIN DISPLAY
# row 1 - items
display = tk.StringVar()  # Main Display
calc_display = ttk.Label(root, font=FONT_DISPLAY, textvariable=display, background='white', padding=20, anchor='e')
calc_display.grid(row=1, columnspan=5, sticky='E W', padx=5, pady=5)

# BUTTONS
# row 2 - items
button_sin = ttk.Button(root, style='Op.TButton', text='sin', padding=10, command=lambda: click_button('sin('))
button_cos = ttk.Button(root, style='Op.TButton', text='cos', padding=10, command=lambda: click_button('cos('))
button_tan = ttk.Button(root, style='Op.TButton', text='tan', padding=10, command=lambda: click_button('tan('))
button_rb_open = ttk.Button(root, style='Op.TButton', text='(', padding=10, command=lambda: click_button('('))
button_rb_close = ttk.Button(root, style='Op.TButton', text=')', padding=10, command=lambda: click_button(')'))

# row 2 - positioning
button_sin.grid(row=2, column=0, sticky="E W")
button_cos.grid(row=2, column=1, sticky="E W")
button_tan.grid(row=2, column=2, sticky="E W")
button_rb_open.grid(row=2, column=3, sticky="E W")
button_rb_close.grid(row=2, column=4, sticky="E W")

# row 3 - items
button_percentage = ttk.Button(root, style='Op.TButton', text='%', padding=10, command=lambda: click_button(''))
button_1_abs = ttk.Button(root, style='Op.TButton', text='|x|', padding=10, command=lambda: click_button('abs('))
button_x_square = ttk.Button(root, style='Op.TButton', text='x²', padding=10, command=lambda: click_button('**'))
button_square_root = ttk.Button(root, style='Op.TButton', text='√x', padding=10, command=lambda: click_button('sqrt('))
button_ce = ttk.Button(root, style='Op.TButton', text='π', padding=10, command=lambda: click_button('pi'))

# row 3 - positioning
button_percentage.grid(row=3, column=0, sticky="E W")
button_1_abs.grid(row=3, column=1, sticky="E W")
button_x_square.grid(row=3, column=2, sticky="E W")
button_square_root.grid(row=3, column=3, sticky="E W")
button_ce.grid(row=3, column=4, sticky="E W")

# row 4 - items
button_7 = ttk.Button(root, text='7', padding=10, command=lambda: click_button('7'))
button_8 = ttk.Button(root, text='8', padding=10, command=lambda: click_button('8'))
button_9 = ttk.Button(root, text='9', padding=10, command=lambda: click_button('9'))
button_divide = ttk.Button(root, style='Op.TButton', text='/', padding=10, command=lambda: click_button('/'))
button_delete = ttk.Button(root, style='Op.TButton', text='DEL', padding=10, command=click_delete)

# row 4- positioning
button_7.grid(row=4, column=0, sticky="E W")
button_8.grid(row=4, column=1, sticky="E W")
button_9.grid(row=4, column=2, sticky="E W")
button_divide.grid(row=4, column=3, sticky="N E S W")
button_delete.grid(row=4, column=4, sticky="N E S W")

# row 5 - items
button_4 = ttk.Button(root, text='4', padding=10, command=lambda: click_button('4'))
button_5 = ttk.Button(root, text='5', padding=10, command=lambda: click_button('5'))
button_6 = ttk.Button(root, text='6', padding=10, command=lambda: click_button('6'))
button_multiply = ttk.Button(root, style='Op.TButton', text='x', padding=10, command=lambda: click_button('*'))
button_c = ttk.Button(root, style='Op.TButton', text='C', padding=10, command=click_reset)

# row 5 - positioning
button_4.grid(row=5, column=0, sticky="E W")
button_5.grid(row=5, column=1, sticky="E W")
button_6.grid(row=5, column=2, sticky="E W")
button_multiply.grid(row=5, column=3, sticky="N E S W")
button_c.grid(row=5, column=4, sticky="N E S W")

# row 6 - items
button_1 = ttk.Button(root, text='1', padding=10, command=lambda: click_button('1'))
button_2 = ttk.Button(root, text='2', padding=10, command=lambda: click_button('2'))
button_3 = ttk.Button(root, text='3', padding=10, command=lambda: click_button('3'))
button_subtract = ttk.Button(root, style='Op.TButton', text='-', padding=10, command=lambda: click_button('-'))
button_equals = ttk.Button(root, style='Equals.TButton', text='=', padding=10, command=click_equals)

# row 6 - positioning
button_1.grid(row=6, column=0, sticky="E W")
button_2.grid(row=6, column=1, sticky="E W")
button_3.grid(row=6, column=2, sticky="E W")
button_subtract.grid(row=6, column=3, sticky="N E S W")
button_equals.grid(row=6, column=4, rowspan=2, sticky="N E S W")

# row 7 - items
button_info = ttk.Button(root, style='Info.TButton', text='info', padding=10, command=click_info)
button_0 = ttk.Button(root, text='0', padding=10, command=lambda: click_button('0'))
button_comma = ttk.Button(root, text=',', padding=10, command=lambda: click_button('.'))
button_add = ttk.Button(root, style='Op.TButton', text='+', padding=10, command=lambda: click_button('+'))

# row 7 - positioning
button_info.grid(row=7, column=0, sticky="N E S W")
button_0.grid(row=7, column=1, sticky="N E S W")
button_comma.grid(row=7, column=2, sticky="N E S W")
button_add.grid(row=7, column=3, sticky="N E S W")


display.set(0)
helper.set(welcome_text)

root.mainloop()
