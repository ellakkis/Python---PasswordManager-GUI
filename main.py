from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# -----------------------------CONSTANTS--------------------------------- #
FONT = ("Courier", 10, "normal")
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------DATA VALIDATION----------------------------#
def check_data():
  if txt_email_username.get() == "" or txt_pass.get() == "" or txt_website.get() == "":
    return False
  else:
    return True
# ----------------------------MESSAGE BOX--------------------------------#
def show_messagebox(title, message):
  messagebox.showinfo(title, message)

# -------------------------------------------Search---------------------------------#
def search():
  website = txt_website.get()

  try:
    with open("data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    print("no file found")
  else:
    if website in data:
      show_messagebox(website, f"\nUsername: {data[website]['email_username']}\nPassword: {data[website]['password']}")
    else:
      show_messagebox(website, "Data not found")

# ---------------------------- PASSWORD GENERATOR ---------------------------- #
def generate_password():  
  password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
  password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
  password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

  full_pass = password_letters + password_numbers + password_symbols
  shuffle(full_pass)
  final_password = "".join(full_pass)
  
  txt_pass.delete(0, 'end')
  txt_pass.insert(0, final_password)

  # pyperclip.copy(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
  if check_data():
    website = txt_website.get()
    email_username = txt_email_username.get()
    password = txt_pass.get()

    new_data = {
      website:{
        "email_username": email_username,
        "password": password
      }
    }
    try:
      with open("data.json", "r") as data_file:
        data = json.load(data_file)
    except FileNotFoundError:
      with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)

        with open("data.json", "w") as data_file:
          json.dump(data, data_file, indent=4)
    finally:
      txt_website.delete(0, 'end')
      txt_email_username.delete(0, 'end')
      txt_pass.delete(0, 'end')
  
    show_messagebox("Data Saved", "Your data have been saved successfully")  
  else:
    show_messagebox("Error", "Please make sure all data is provided") 
# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.configure(width=350, height=350, bg="white", padx=50, pady=50)
root.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")

# logo
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

# Labels 
lbl_website = Label(text="Website", font=FONT, bg="white")
lbl_website.grid(column=0, row=2)

lbl_email_username = Label(text="Email/Username", font=FONT, bg="white")
lbl_email_username.grid(column=0, row=3)

lbl_pass = Label(text="Password", font=FONT, bg="white")
lbl_pass.grid(column=0, row=4)

# Text fields
txt_website = Entry(root, width=25)
txt_website.grid(column=1, row=2, padx=3, pady=3)

txt_email_username = Entry(root, width=40)
txt_email_username.grid(columnspan=2, column=1, row=3, padx=3, pady=3)

txt_pass = Entry(root, width = 25)
txt_pass.grid(column=1, row=4, padx=0, pady=3)

# Buttons
btn_search = Button(text="Search", command=search, bg="white", font=("Courier", 7, "normal"), width=13, height=1, pady=1)
btn_search.grid(column=2, row=2, padx=1, pady=0)

btn_generate_pass = Button(text="Generate Password", command=generate_password, font=("Courier", 7, "normal"), bg="white", padx=1, pady=1)
btn_generate_pass.grid(column=2, row=4)

btn_add = Button(text="Add", command=add, width=37, bg="white")
btn_add.grid(columnspan=2, column=1, row=5, padx=0, pady=3)











root.mainloop()