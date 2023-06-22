from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
FONT = ("Courier", 14, "bold")
email = 'INSERT EMAIL HERE'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    website = website_text.get()
    emails = email_text.get()
    password = password_text.get()
    if len(website) == 0 or len(emails) == 0 or len(password) == 0:
        messagebox.showwarning(title='Empty Fields', message='Please Do Not Leave Any Empty Fields')
    else:
        decision = messagebox.askokcancel(title=f'{website}', message=f'Email: {emails} \n Password: '
                                                                  f'{password} \n Is it okay to save?')
        if decision:
            with open('accounts.txt', 'a') as data:
                data.write(f'{website} | {emails} | {password} \n')
            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=50, padx=50, width=500,height=500)
window.title("Password Manager")
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200,height=200, highlightthickness=0)
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)
website_label = Label(text='Website:', font=FONT)
email_label = Label(text='Email/Username:', font=FONT)
password_label = Label(text='Password:', font=FONT)
website_text = Entry(width=35)
email_text = Entry(width=35)
password_text = Entry(width=21)
generate_button = Button(text='Generate', font=FONT,command=generate_password)
add_button = Button(text='Add', font=FONT, width=36, command=save_data)

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_text.grid(column=1, row=1, columnspan=2)
email_text.grid(column=1, row=2, columnspan=2)
password_text.grid(column=1, row=3, sticky='w')
generate_button.grid(column=2, row=3, sticky='e')
add_button.grid(column=1, row=4, columnspan=2)

website_text.focus()
email_text.insert(0, email)


window.mainloop()
