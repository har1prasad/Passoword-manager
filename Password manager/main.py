from tkinter import *
from tkinter import messagebox
import pyperclip
import os
import random

FONT = ("Helvetica", 11, "bold")

# ---------------------------- GENERATING PASSWORD ------------------------------- #
def generate_password():
    enrty_pass.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password = password_letters + password_numbers + password_symbols

    random.shuffle(password)
    shuffled_password = ''.join(password)

    enrty_pass.insert(0, shuffled_password)
    pyperclip.copy(shuffled_password)


# ---------------------------- SAVING DATA ------------------------------- #
def save_data():
    website = entry_website.get()
    name = entry_name.get()
    password = enrty_pass.get()

    if not website or not name or not password:
        messagebox.showerror(title="OOPS", message="Please fill out all required fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"""These are the details you've provided 
                            \nUsername : {name} \nPassword : {password} \nis it ok to save ?""")
        
        if is_ok:
            file_path = ".\\passwords.csv"
            
            is_empty = os.stat(file_path).st_size == 0 if os.path.isfile(file_path) else True
            # this line of code determines if the file is either empty or does not exist. 
            # If the file does not exist, it is treated as empty. 
            # If the file exists, it checks if it is empty based on its size.

            with open(file_path, "a") as data:
                if is_empty:
                    data.write("Website, Username, Password\n")
                data.write(f"{website}, {name}, {password}\n")

            entry_website.delete(0, END)
            entry_name.delete(0, END)
            enrty_pass.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My password manager")
window.config(padx=60, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=256, height=260)
canvas.create_image(136, 125, image=logo_img, )
canvas.grid(row=0, column=1, pady=(0, 12))

label_website = Label(window, text="Website : ", font=FONT)
label_website.grid(row=1, sticky="w", column=0, pady=(0, 5))
entry_website = Entry(window, width=62, borderwidth=1, highlightthickness=1)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

label_name = Label(window, text="Username : ", font=FONT)
label_name.grid(row=2, sticky="w", column=0, pady=(0, 5))
entry_name = Entry(window, width=62, borderwidth=1, highlightthickness=1)
entry_name.grid(row=2, column=1, columnspan=2)

label_password = Label(window, text="Password : ", font=FONT)
label_password.grid(row=3,sticky="w", column=0, pady=(0, 5))
enrty_pass = Entry(window, width=43, borderwidth=1, highlightthickness=1)
enrty_pass.grid(row=3, column=1)

button_pass = Button(window, text="Generate password", command=generate_password)
button_pass.grid(row=3, column=2, pady=(0, 5))

button_add = Button(window, width=53, text="Add",command=save_data)
button_add.grid(row=4, column=1,columnspan=2)


window.mainloop()