from tkinter import *
import random

def generate_password():
    complexity = complexity_level.get()
    length_range_str = length_range.get()
    
    if not length_range_str:
        password_entry.config(state='normal')
        password_entry.delete(0, END)
        password_entry.insert(0, "Please select a length range.")
        password_entry.config(state='readonly')
        return
    
    min_length, max_length = map(int, length_range_str.split('-'))
    
    if complexity == 1:
        char_set = lowercase
    elif complexity == 2:
        char_set = lowercase + uppercase
    elif complexity == 3:
        char_set = lowercase + uppercase + numbers
    else:
        char_set = lowercase + uppercase + numbers + symbols
    
    password_length = random.randint(min_length, max_length)
    password = ''.join(random.choice(char_set) for _ in range(password_length))
    
    password_entry.config(state='normal')
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')


main = Tk()
main.title("Password Generator")
main.geometry("600x300")
main.resizable(False,False)

bg_color = "#3498db"
button_color = "#2ecc71"
text_color = "white"

lowercase = "a b c d e f g h i g k l m n o p q r s t u v w x y z".split()
uppercase = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
numbers = "0 1 2 3 4 5 6 7 8 9".split()
symbols = "~ ` ! @ # £ € $ § % ° ^ & * ( ) - _ + = { } [ ] | / : ; ' < > , . ".split()

title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

title_frame = Frame(main, bg=bg_color)
title_frame.pack(fill="both", expand=True)

generating_frame = Frame(main, bg=bg_color)
generating_frame.pack(fill="both", expand=True)

generated_frame = Frame(main, bg=bg_color)
generated_frame.pack(fill="both", expand=True)

title = Label(title_frame, text="Password Generator with Complexity", bg=bg_color, fg=text_color, font=title_font)
title.pack(pady=10)

complexity_label = Label(generating_frame, text="Choose complexity level: ", bg=bg_color, fg=text_color, font=label_font)
length_Label = Label(generating_frame, text="Choose password length: ", bg=bg_color, fg=text_color, font=label_font)

complexity_level = IntVar()
complexity_level.set(1)
length_range = StringVar()
length_range.set("4-7")

complexity_label.grid(row=1, column=1, pady=4)
length_Label.grid(row=2, column=1, pady=4)

complexity_button1 = Radiobutton(generating_frame, text="Level 1", variable=complexity_level, value=1, width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
complexity_button2 = Radiobutton(generating_frame, text="Level 2", variable=complexity_level, value=2, width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
complexity_button3 = Radiobutton(generating_frame, text="Level 3", variable=complexity_level, value=3, width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
complexity_button4 = Radiobutton(generating_frame, text="Level 4", variable=complexity_level, value=4, width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)

complexity_button1.grid(row=1, column=2, padx=4)
complexity_button2.grid(row=1, column=3, padx=4)
complexity_button3.grid(row=1, column=4, padx=4)
complexity_button4.grid(row=1, column=5, padx=4)

length_button1 = Radiobutton(generating_frame, text="4 - 7", variable=length_range, value="4-7", width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
length_button2 = Radiobutton(generating_frame, text="8 - 11", variable=length_range, value="8-11", width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
length_button3 = Radiobutton(generating_frame, text="12 - 15", variable=length_range, value="12-15", width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)
length_button4 = Radiobutton(generating_frame, text="16 - 19", variable=length_range, value="16-19", width=6, bg=bg_color, fg=text_color, font=button_font, selectcolor=bg_color)

length_button1.grid(row=2, column=2, padx=4)
length_button2.grid(row=2, column=3, padx=4)
length_button3.grid(row=2, column=4, padx=4)
length_button4.grid(row=2, column=5, padx=4)

generate_button = Button(generated_frame, text="Generate Password", command=generate_password, bg=button_color, fg=text_color, font=button_font)
generate_button.pack(pady=10)

password_entry = Entry(generated_frame, bg=bg_color, fg="blue", font=label_font, state='readonly')
password_entry.pack(pady=10)

main.mainloop()
