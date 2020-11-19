from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1000x800')




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
    
    choose_caeser = ttk.Button(root, command=caeser_select, text='caeser')
    choose_vernam = ttk.Button(root, command=vernam, text='virnam')
    choose_caeser.pack()
    choose_vernam.pack()

def caeser_select():

    def get_shift_number():
        global shifty
        shifty = shift_number.get()

    def we_shift_left():
        for i in range(length):
            final = int(convert[i])-int(shifty)
            final_numbers.append(final)
        print(final_numbers)

    def we_shift_right():
        for i in range(length):
             final = convert[i]+int(shifty)
             final_numbers.append(final)
        print(final_numbers)

    convert = []
    final_numbers = []
    length = len(L)
    print(length)
    
    for i in range(length):
        number = ord(L[i]) - 96
        convert.append(number)
    print(convert)

    shift_number = Entry(root)
    how_many = Label(root, text='how many positions would you like to shift by?')
    how_many.pack()
    shift_number.pack()

    select_number = Button(root, text='select number', command=get_shift_number)
    select_number.pack()

    label = Label(root, text="What direction would you like to shift? Please enter 'L' for left or 'R' for right: ")
    label.pack()

    shift_left = Button(root, text='shift left', command=we_shift_left)
    shift_left.pack()

    shift_right = Button(root, text='shift right', command=we_shift_right)
    shift_right.pack()



        


def vernam():
    print('')

enter()

root.mainloop()
