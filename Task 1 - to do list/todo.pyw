from tkinter import *

main = Tk()
main.geometry("600x800")
main.resizable(0, 0)
main.title("Todo")
taskn = 0
toggle = -1
tasklist = []


bg_color = "#f5f5f5"  
button_color = "#3498db"  
font_color = "#333333"  


font_style = ("Arial", 12)
main.configure(bg=bg_color)

entry_frame = Frame(main, bg=bg_color)
task_frame = Frame(main, bg=bg_color)

welcome_label = Label(main, text='"The best way\nto get something done\nis to begin"',  font = ("Copperplate Gothic Bold", 24), bg=bg_color, justify = 'center')
welcome_label.pack(pady=30)

def delete_task(n):
    global taskn
    try:
        valid_task_label.destroy()
    except:
        pass
    try:
        task_limit_label.destroy()
    except:
        pass
    tasklist[n - 1][0].destroy()
    tasklist[n - 1][3].destroy()
    tasklist[n - 1][5].destroy()
    i = 0
    while i < len(tasklist):
        if not tasklist[i][0].winfo_exists():
            tasklist.remove(tasklist[i])
            for j in range(i, len(tasklist)):
                tasklist[j][1] -= 1
        i += 1
    for i in range(len(tasklist)):
        tasklist[i][3].config(command=lambda a=tasklist[i][1]: edit_task(a))
        tasklist[i][5].config(command=lambda a=tasklist[i][1]: delete_task(a))
    for i in range(len(tasklist)):
        tasklist[i][0].grid(row=i + 1, column=1, padx=10, pady=10)
        tasklist[i][3].grid(row=i + 1, column=2, padx=10, pady=10)
        tasklist[i][5].grid(row=i + 1, column=3, padx=10, pady=10)
    taskn -= 1


def edit_task(n):
    global tasklist
    global toggle
    global task_button
    global valid_task_label
    try:
        valid_task_label.destroy()
    except:
        pass
    try:
        task_limit_label.destroy()
    except:
        pass
    
    if toggle < 0:
        try:
            valid_task_label.destroy()
        except:
            pass
        try:
            task_limit_label.destroy()
        except:
            pass
        tasklist[n - 1][0].config(state=NORMAL, bg="white", fg=font_color, font=font_style)
        tasklist[n - 1][2] = PhotoImage(file="pics/check.png")
        tasklist[n - 1][3].config(image=tasklist[n - 1][2],  bd=0, cursor="hand2")

        task_button.config(state=DISABLED, bg="lightgray", fg=font_color, font=font_style)

        for i in range(len(tasklist)):
            tasklist[i][5].config(state=DISABLED)
            if i != n - 1:
                tasklist[i][3].config(state=DISABLED)
        task_entry.config(state="readonly", bg="lightgray")

    else:
        try:
            valid_task_label.destroy()
        except:
            pass
        try:
            task_limit_label.destroy()
        except:
            pass
        if len(tasklist[n - 1][0].get()) == 0:
            valid_task_label = Label(entry_frame, text="Please input a valid task", fg="red", bg=bg_color, font=font_style)
            valid_task_label.pack()
            return None
        tasklist[n - 1][0].config(state="readonly", bg=bg_color, fg=font_color, font=font_style)
        tasklist[n - 1][2] = PhotoImage(file="pics/edit.png")
        tasklist[n - 1][3].config(image=tasklist[n - 1][2],  bd=0, cursor="hand2")

        task_button.config(state=NORMAL, bg=button_color, fg="white", font=font_style)

        for i in range(len(tasklist)):
            tasklist[i][5].config(state=NORMAL)
            if i != n - 1:
                tasklist[i][3].config(state=NORMAL)
        task_entry.config(state=NORMAL, bg="white")
    toggle *= -1


def save_task():
    global taskn
    global edit_image
    global delete_image
    global tasklist
    global valid_task_label
    global task_entry
    global task_limit_label
    task = task_entry.get()
    try:
        valid_task_label.destroy()
    except:
        pass
    try:
        task_limit_label.destroy()
    except:
        pass
    if len(task) == 0:
        valid_task_label = Label(entry_frame, text="Please input a valid task", fg="red", bg=bg_color, font=font_style)
        valid_task_label.pack()
        return None
    if taskn == 10:
        task_limit_label = Label(entry_frame, text="You reached the task limit (10)", fg="red", bg=bg_color,
                                 font=font_style)
        task_limit_label.pack()
        return None
    task_text = Entry(task_frame, width=40, bg="white", font=font_style, fg=font_color)
    task_text.insert("0", task)
    task_text.config(state="readonly")
    taskn += 1
    task_entry.delete(0, END)

    edit_image = PhotoImage(file="pics/edit.png")
    delete_image = PhotoImage(file="pics/delete.png")

    edit = Button(task_frame, image=edit_image, command=lambda taskn=taskn: edit_task(taskn), bd=0,
                  cursor="hand2")
    delete = Button(task_frame, image=delete_image, command=lambda taskn=taskn: delete_task(taskn), 
                    bd=0, cursor="hand2")

    tasklist.append([task_text, taskn, edit_image, edit, delete_image, delete])

    task_text.grid(row=taskn, column=1, padx=10, pady=10)
    edit.grid(row=taskn, column=2, padx=10, pady=10)
    delete.grid(row=taskn, column=3, padx=10, pady=10)


task_entry = Entry(entry_frame, width=40, bg="white", font=font_style, fg=font_color)
task_button = Button(entry_frame, text="Create Task", command=save_task, bg=button_color, fg="white",
                     font=font_style, bd=0, cursor="hand2")

task_entry.pack(pady=10)
task_button.pack(pady=10)

entry_frame.pack()
task_frame.pack()

main.mainloop()