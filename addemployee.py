import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
# from tkinter import ttk



def insert():
    # database
    con = sqlite3.connect("ContactInfo.db")
    cur = con.cursor()
    cur.execute("INSERT INTO addresses VALUES(:First_Name,:Last_Name, :Gender, :Age, :Address, :Contact)",{
        'First_Name': first_name.get(),
        'Last_Name': last_name.get(),
        'Gender': gender.get(),
        'Age': age.get(),
        'Address': address.get(),
        'Contact': contact.get()
    })
    messagebox.showinfo("Employee", "Employee Added Sucessfully !")

    con.commit()
    con.close()
    root.destroy()
    os.system(('contact.py'))

def clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    address.delete(0, END)
    contact.delete(0,END)


def add():
    global root
    root = Toplevel()
    root.geometry("1366x768")
    root.title("Add Employee")
    # myimage1 = ImageTk.PhotoImage(Image.open('./images/add.png'))
    # label1 = Label(root, image=myimage1)
    # label1.pack()

    global first_name
    global last_name
    global gender
    global age
    global address
    global contact

    # desgin
    root.geometry("1366x768+60+10")
    root.resizable(0, 0)
    # root.iconbitmap('./images/3.ico')

    first_name_lbl = Label(root, text="First Name", font=('Consolas', 15), bg="white")
    first_name_lbl.place(x=180, y=200)
    last_name_lbl = Label(root, text="Last Name", font=('Consolas', 15), bg="white")
    last_name_lbl.place(x=720, y=200)
    gender_lbl = Label(root, text="Gender", font=('Consolas', 15), bg="white")
    gender_lbl.place(x=180, y=290)
    age_lbl = Label(root, text="Age", font=('Consolas', 15), bg="white")
    age_lbl.place(x=720, y=290)
    address_lbl = Label(root, text="Address", font=('Consolas', 15), bg="white")
    address_lbl.place(x=180, y=380)
    contact_lbl = Label(root, text="Contact", font=('Consolas', 15), bg="white")
    contact_lbl.place(x=720, y=380)

    first_name = Entry(root, width=40, border=0, font=('Consolas', 15))
    first_name.place(x=180, y=230)
    last_name = Entry(root, width=40, border=0, font=('Consolas', 15))
    last_name.place(x=720, y=230)
    gender = Entry(root, width=40, border=0, font=('Consolas', 15))
    gender.place(x=180, y=320)
    age = Entry(root, width=40, border=0, font=('Consolas', 15))
    age.place(x=720, y=320)
    address = Entry(root, width=40, border=0, font=('Consolas', 15))
    address.place(x=180, y=410)
    contact = Entry(root, width=40, border=0, font=('Consolas', 15))
    contact.place(x=720, y=410)
    add_btn = Button(root, text="ADD", font=('Consolas', 15), cursor='hand2',
                     bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command=insert)
    add_btn.place(x=560, y=630)
    clear_btn = Button(root, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                       bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command=clear)
    clear_btn.place(x=715, y=630)


    root.mainloop()