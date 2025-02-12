import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Operación inválida")
            screen_var.set("")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

app = tk.Tk()
app.title("Calculadora Básica")

screen_var = tk.StringVar()
screen = tk.Entry(app, textvar=screen_var, font="lucida 20 bold")
screen.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

first_num = None
second_num = None
operation = None

def click(event):
    global first_num, second_num, operation
    text = event.widget.cget("text")
    
    if text.isdigit():
        if operation is None:
            if first_num is None:
                first_num = text
            else:
                first_num += text
            screen_var.set(first_num)
        else:
            if second_num is None:
                second_num = text
            else:
                second_num += text
            screen_var.set(second_num)
    elif text in "+-*/":
        if first_num is not None:
            if second_num is not None:
                try:
                    first_num = str(eval(first_num + operation + second_num))
                    screen_var.set(first_num)
                    second_num = None
                except Exception as e:
                    messagebox.showerror("Error", "Operación inválida")
                    first_num = None
                    second_num = None
                    operation = None
                    screen_var.set("")
            operation = text
    elif text == "=":
        if first_num is not None and operation is not None and second_num is not None:
            try:
                result = eval(first_num + operation + second_num)
                screen_var.set(result)
                first_num = str(result)
                second_num = None
                operation = None
            except Exception as e:
                messagebox.showerror("Error", "Operación inválida")
                first_num = None
                second_num = None
                operation = None
                screen_var.set("")
    elif text == "C":
        first_num = None
        second_num = None
        operation = None
        screen_var.set("")
        
for button in buttons:
    btn = tk.Button(app, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

app.mainloop()