from tkinter import *
from tkinter import ttk

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
n=15
o=16
p=17
q=18
r=18
s=19
t=20
u=21
v=22
w=23
x=24
y=25
z=26

root = Tk()
root.geometry('400x400')




def enter():
    global e
    
    enter_sentence = Label(root, text="Please enter a word/sentence: ")
    enter_sentence.pack()
    e = Entry(root)
    e.pack()


    fetcher = ttk.Button(root, command=fetch, text='fetcher')
    fetcher.pack()
    

def fetch():
    global L

    word=e.get()
    L = list(word)

    print(L)
    
    choose_caeser = ttk.Button(root, command=caeser, text='caeser')
    choose_vernam = ttk.Button(root, command=vernam, text='virnam')
    choose_caeser.pack()
    choose_vernam.pack()

def caeser():
    
    shift = Entry(root)
    label1 = Label(root, text="What direction would you like to shift? Please enter 'L' for left or 'R' for right: ")
    label1.pack()
    shift.pack()

    chosen_shift = shift.get()
    
    convert = []
    length = len(L)
    print(length)
    
    for i in range(length):
        number = ord(L[i]) - 96
        convert.append(number)
    print(convert)

def vernam():
    print('')

enter()

root.mainloop()
