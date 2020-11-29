from tkinter import *
from tkinter import ttk
import os
import sys

root = Tk()
root.geometry('1000x800')



def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def hide_all_frames():
    caeser_frame.pack_forget()
    vernam_frame.pack_forget()


# caeser cipher

def caeser():
    hide_all_frames()

    #pack caeser frame
    caeser_frame.pack()


    def fetch():
        global L
        word=e.get()
        print(word)
        L = list(word)
    
        print(L)
        
        choose_caeser = ttk.Button(caeser_frame, command=caeser, text='caeser')
        choose_caeser.pack()

    fetcher = ttk.Button(caeser_frame, command=fetch, text='Encrypt')
    fetcher.pack()

    # fetch shift by how many
    def get_shift_number():
        global shifty
        shifty = shift_number.get()

    # shift left chosen
    def we_shift_left():
        for i in range(length):
            final = int(convert[i])-int(shifty)
            final_numbers.append(final)
        
        for i in range(length):
            if convert[i] < 1:
                print ("Out of range - can't convert")
            else:
                print(final_numbers)
                number_to_letter()
    
    # shift right chosen
    def we_shift_right():
        for i in range(length):
             final = convert[i]+int(shifty)
             final_numbers.append(final)
        
        for i in range(length):
             if convert[i] > 26:
                 print("Out of range")
             else:
                print(final_numbers)
                number_to_letter()


    # enter phrase to be encrypted
    enter_sentence = Label(caeser_frame, text="Please enter a word/sentence to be encrypted below: ")
    enter_sentence.pack()
    e = Entry(caeser_frame)
    e.pack()

    
    # define lists
    convert = []
    final_numbers = []
    length = len(L)
    print(length)
    converted_letters = []

    # convert letters to corresponding numbers
    for i in range(length):
        number = ord(L[i]) - 96
        convert.append(number)
    print(convert)

    # choose how many positions to shift by
    def shift_num_fun():
        shift_number = Entry(caeser_frame)
        how_many = Label(caeser_frame, text='how many positions would you like to shift by?')
        how_many.pack()
        shift_number.pack()

        select_number = ttk.Button(caeser_frame, text='select number', command=get_shift_number)
        select_number.pack()

    # choose shift direction
    def shift_direct_num():
        label = Label(caeser_frame, text="What direction would you like to shift? Please enter 'L' for left or 'R' for right: ")
        label.pack()

        shift_left = ttk.Button(caeser_frame, text='shift left', command=we_shift_left)
        shift_left.pack()

        shift_right = ttk.Button(caeser_frame, text='shift right', command=we_shift_right)
        shift_right.pack()

    #################

    def number_to_letter():
        print (final_numbers)

        print ("we go now")

        number_to_letter = [chr(n) for n in final_numbers]
        print ("number to letter is" + str(number_to_letter))

        # for i in range(length):
        #     number_to_letter = final_numbers
        #     converted_letters.append(number_to_letter)
        # print(number_to_letter)



        


def vernam():
    print('')



### START OF PROGRAM

welcome = Label(root, text="Hello, please use the menu above to navigate the interface")
welcome.pack()

### create menu bar

menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_1 = Menu(menu_bar)
menu_bar.add_cascade(label="Main Menu", menu=menu_1)
menu_1.add_command(label="Caeser Cipher", command=caeser)
menu_1.add_command(label="Vernam Cipher", command=vernam)
menu_1.add_command(label="Restart program", command=restart)

caeser_frame = Frame(root, width=800, height=1000)
vernam_frame = Frame(root, width=800, height=1000)


root.mainloop()
