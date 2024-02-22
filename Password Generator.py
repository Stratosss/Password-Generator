from tkinter import * 
from tkinter import messagebox
import pyperclip
import random


# 
def is_int():   #Oversees that the length and numbers given meet the requirements
    try:
        length_int = int(length_var.get())   #Ensures that an integer is given
        if 0 < length_int < 100:     #Password length limited to the range of 1 to 99 for practical and performance purposes
            return password_generator(length_int)
        else:
            messagebox.showwarning(title='Warning', message='Please provide a length from 1-99')
    except ValueError as e:
        print(e)
        return messagebox.showwarning(title='Warning', message='Please provide a length from 1-99')
    
def password_generator(length):
    capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','^','&','*','(',')','€']
    password = ''
    password_final = ''
    all_lists = capital + lowercase + numbers + symbols
    for i in range(length):
        temp = random.choice(all_lists)
        temp_to_string = password.join(str(x) for x in temp)
        password_final= password_final + temp_to_string
        
    pyperclip.copy(password_final)
    messagebox.showinfo("Information", f'password: {password_final} was copied to clipboard')
    
    
root = Tk()
frame = Frame(root, bg="#FFA07A")
root.resizable(width=False, height=False)

root.geometry("350x200")
root.configure(bg="#FFA07A")
root.title("Password Generator")

description_label = Label(master= frame, text="Enter the length of the password (1-99 characters)", bg="#FFA07A", font=("Garamond", 12, "bold"))
description_label.pack(pady=5)

length_var = StringVar()
my_entry = Entry(master= frame, textvariable = length_var, width = 20)
my_entry.pack(pady=10)

button1 = Button(master= frame, text = "Generate", command = is_int, font=("Garamond", 12, "bold"))
button1.pack(side= LEFT, padx= 15, pady=20)

button2 =Button(master= frame, text = "Exit", command = root.destroy, font=("Garamond", 12, "bold"), fg="red")
button2.pack(side= RIGHT, padx= 15, pady=20)

frame_b = Frame(root)
signature = Label(text="Created by Stratos Gialouris", bg="#FFA07A", font=("Garamond", 12, "bold", "italic"))

frame.pack()
frame_b.pack(side=BOTTOM, fill=X)
signature.pack(side=RIGHT)

root.mainloop()