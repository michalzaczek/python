from tkinter import *
from tkinter import messagebox
from random import randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = ''.join([chr(randint(33,127)) for x in range(10)])
    password_txtbox.delete(0, END)
    password_txtbox.insert(0, generated_password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            website = data.get(website_txtbox.get())
    except:
        with open('data.json', 'w') as file:
            json.dump({}, fp=file, indent=4)
        messagebox.showerror(title='Error. No .json file', message='Couldn\'t find .json file.\n'                                                           'New data file has been created.')
    else:
        if website:
            msq = 'Username: ' + website['user'] + '\n' \
                  'Password: ' + website['password'] + '\n\n' \
                  'Password has been copied to clipboard'
            pyperclip.copy(website['password'])
        else:
            msq = f'Couldn\'t find {website_txtbox.get()} website'
        messagebox.showinfo(title='Data details', message=msq)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_txtbox.get()
    user = user_txtbox.get()
    password = password_txtbox.get()

    new_data = {
        website: {
            "user" : user,
            "password" : password
        }
    }

    #checks if all filled
    if not all((website, user, password)):
        messagebox.showerror(title='Error', message='Not all fields filled!')
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                if data != '':
                    data.update(new_data)
                else:
                    data = {}
        except FileNotFoundError:
            data = new_data

        with open('data.json', 'w') as file:
            json.dump(data, fp=file, indent=4)
        messagebox.showinfo(title='Success!', message='Your data has been successfully saved.\n'
                                                      'Your password has been copied to the clipboard.')
        pyperclip.copy(password_txtbox.get())

        website_txtbox.delete(0, END)
        user_txtbox.delete(0, END)
        password_txtbox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_lbl = Label(text='Website:')
website_lbl.grid(row=1, column=0)

website_txtbox = Entry(width=35)
website_txtbox.grid(row=1, column=1)
website_txtbox.focus()

search_btn = Button(text='Search', width=14, command=search)
search_btn.grid(row=1, column=2)

user_lbl = Label(text='Email/Username:')
user_lbl.grid(row=2, column=0)

user_txtbox = Entry(width=53)
user_txtbox.grid(row=2, column=1, columnspan=2)
user_txtbox.insert(0, 'exemple@domain.com')

password_lbl = Label(text='Password:')
password_lbl.grid(row=3, column=0)

password_txtbox = Entry(width=35)
password_txtbox.grid(row=3, column=1)

generate_btn = Button(text='Generate Password', command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=45, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()

