import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
def clear():
    entry.delete(0, tk.END)


def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
window = tk.Tk()
window.title("Calculator")
window.geometry("520x500")
window.resizable(False, False)
window.configure(bg="#F7DC6F")

entry = tk.Entry(window, width=20, font=("Verdana", 28), borderwidth=5, bg="#FFD700", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']

row_num = 1
col_num = 0

button_style = {"font": ("Verdana", 16),"width": 6,"height": 2,"bg": "#3498DB","fg": "white","activebackground": "#2980B9","activeforeground": "white"}

for button in buttons:
    tk.Button(window, text=button, command=lambda b=button: button_click(b) if b != '=' else calculate(), **button_style).grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

clear_button = tk.Button(window, text='C', command=clear, font=("Verdana", 16), width=6, height=2, bg="#E74C3C", fg="white", activebackground="#C0392B", activeforeground="white")
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
