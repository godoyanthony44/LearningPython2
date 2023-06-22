from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Courier", 14, "bold")
email = 'ENTER EMAIL HERE'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_text.delete(0, END)
    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_text.get().lower()
    emails = email_text.get().lower()
    password = password_text.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if len(website) == 0 or len(emails) == 0 or len(password) == 0:
        messagebox.showwarning(title='Empty Fields', message='Please Do Not Leave Any Empty Fields')
    else:
        try:
            with open('accounts.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('accounts.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except ValueError:
            with open('accounts.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            with open('accounts.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


def search_accounts():
    search_term = website_text.get().lower()
    try:
        with open('accounts.json', 'r') as data_file:
            data = json.load(data_file)
            website = search_term.title()
            emails = data[search_term]["email"]
            password = data[search_term]["password"]
            messagebox.showinfo(title=f'{website}', message=f'Email: {emails}\nPassword: {password}')

    except ValueError:
        messagebox.showwarning(title='Value Error', message='Account was not found in the list of Accounts')
    finally:
        website_text.delete(0, END)
        password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=50, padx=50, width=500, height=500)
window.title("Password Manager")
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
website_label = Label(text='Website:', font=FONT)
email_label = Label(text='Email/Username:', font=FONT)
password_label = Label(text='Password:', font=FONT)
website_text = Entry(width=22)
email_text = Entry(width=35)
password_text = Entry(width=22)
search_button = Button(text='Search', font=FONT, command=search_accounts, width=10)
generate_button = Button(text='Generate', font=FONT, command=generate_password, width=10)
add_button = Button(text='Add', font=FONT, width=36, command=save_data)

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_text.grid(column=1, row=1, sticky='w')
email_text.grid(column=1, row=2, columnspan=2)
password_text.grid(column=1, row=3, sticky='w')
search_button.grid(column=2, row=1, sticky='e')
generate_button.grid(column=2, row=3, sticky='e')
add_button.grid(column=1, row=4, columnspan=2)

website_text.focus()
email_text.insert(0, email)

window.mainloop()
