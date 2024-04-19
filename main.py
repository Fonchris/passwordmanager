from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
               'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U',
               'u',
               'V',
               'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = [';', ':', '/', '>', '<', '?', '#', '@', '!', '"', '.', '+', '_', '-', '(', ')', '*', '&', '^', '%', '$',
               ']']

    print("welcome to the python password generator")
    letter_no = randint(8, 10)
    number_no = randint(2, 4)
    symbol_num = randint(2, 4)
    # new_list = [new_item for item in list]
    password_letters = [choice(letters) for letter in range(letter_no)]
    password_numbers = [choice(numbers) for num in range(number_no)]
    password_symbols = [choice(symbols) for sym in range(symbol_num)]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    # print(f"your password is {password}")
    password_input.insert(END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    get_website = website_input.get()
    get_email = email_user_input.get()
    get_password = password_input.get()
    new_data = {get_website:
                    {"email": get_email,
                     "password": get_password
                     }
                }
    if len(get_website) == 0 or len(get_password) == 0 or len(get_email) == 0:
        messagebox.showinfo(title="oops", message="please make sure you haven't left any of these empty")

    else:
        try:
            with open("save_file.json", "r") as file:
                # reading the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("save_file.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("save_file.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# -----------------------------FIND PASSWORD--------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("save_file.json") as data_file:

            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title ="error", message="no data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"no details for {website}  exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
email_user_input = Entry(width=35)
email_user_input.insert(0, "eg:chris@gmail.com")
email_user_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
password_generator_button = Button(text="generate password", command=generate_password)
password_generator_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1)

search_button = Button(text="search", command=find_password, width=5)
search_button.grid(row=1, column=2)

window.mainloop()
