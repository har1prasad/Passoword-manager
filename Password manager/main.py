from tkinter import *
from tkinter import messagebox
import json
import pyperclip
import os
import random

FONT = ("Helvetica", 11, "bold")

# ---------------------------- SEARCH ------------------------------- #
def search():

    website = entry_website.get()

    if not website:
        messagebox.showerror(title="OOPS", message="Please fill website field.")
    else:
        try:
            file_path = ".\\passwords.json"
            with open(file_path, "r") as data:
                existing_data = json.load(data)
        except FileNotFoundError:
            messagebox.showinfo(title="No File Found", message=f"please make sure to save some passwords before searching")
        else:
            if website not in existing_data:
                messagebox.showerror(title="OOPS", message=f"""No corresponding data related to {website}.
                                    \n Please ensure the spelling is accurate.""")
            else:
                messagebox.showinfo(title=website, message=f"""\nUsername :{existing_data[website]["name"]} 
                                \nPassword :{existing_data[website]["password"]}""")
        finally:
            entry_website.delete(0, END)



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

    new_dict = {
        website:{
            "name":name,
            "password":password
            }}

    if not website or not name or not password:
        messagebox.showerror(title="OOPS", message="Please fill out all required fields.")
    else:
        file_path = ".\\passwords.json"
        
        try:
            with open(file_path, "r") as data:
                existing_data = json.load(data)
                existing_data.update(new_dict)
        except FileNotFoundError:
            with open(file_path, "w") as data:
                json.dump(new_dict, data, indent=4)
        else:
            with open(file_path, "w") as data:
                json.dump(existing_data, data, indent=4)
        finally:
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
entry_website = Entry(window, width=43, borderwidth=1, highlightthickness=1)
entry_website.grid(row=1, column=1)
entry_website.focus()

label_name = Label(window, text="Username : ", font=FONT)
label_name.grid(row=2, sticky="w", column=0, pady=(0, 5))
entry_name = Entry(window, width=62, borderwidth=1, highlightthickness=1)
entry_name.grid(row=2, column=1, columnspan=2)

label_password = Label(window, text="Password : ", font=FONT)
label_password.grid(row=3,sticky="w", column=0, pady=(0, 5))
enrty_pass = Entry(window, width=43, borderwidth=1, highlightthickness=1)
enrty_pass.grid(row=3, column=1)

button_search = Button(window, width=14, text="Search", command=search)
button_search.grid(row =1, column=2, pady=(0, 5))

button_pass = Button(window, text="Generate password", command=generate_password)
button_pass.grid(row=3, column=2, pady=(0, 5))

button_add = Button(window, width=53, text="Add",command=save_data)
button_add.grid(row=4, column=1,columnspan=2)


window.mainloop()
