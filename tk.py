from tkinter import *

root = Tk()
root.geometry('400x400')

def chosen_encryption():
    e = Entry(root)
    enter_encryption = Label(root, text="Choose your type of encryption: ", command=encrypt)  

def enter():
    enter_sentence = Label(root, text="Please enter a word/sentence: ", command=encrypt)
    e = Entry(root)
    choose_caeser = Label(root, command=caeser)
    e.pack()
    choose_caeser.pack()

def choose_caeser():
    

enter()

root.mainloop()
