from tkinter import *

root = Tk()
root.geometry('400x400')




def enter():
    global L
    
    enter_sentence = Label(root, text="Please enter a word/sentence: ")
    enter_sentence.pack()
    e = Entry(root)
    e.pack()
    choose_caeser = Button(root, command=caeser, text='caeser')
    choose_vernam = Button(root, command=vernam, text='virnam')
    choose_caeser.pack()
    choose_vernam.pack()
    

    word=e.get()
    L = list(word)

def caeser():
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

    print (L)

def vernam():
    print('')

enter()

root.mainloop()
