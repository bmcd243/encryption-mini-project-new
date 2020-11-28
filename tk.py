from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1000x800')


### create menu bar

menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_1 = Menu(menu_bar)
menu_bar.add_cascade(label="Pick cipher", menu=menu_1)
menu_1.add_command(label="caeser")
menu_1.add_command(label="vernam")


# enter phrase to be encrypted

def enter():
    global e
    
    enter_sentence = Label(root, text="Please enter a word/sentence: ")
    enter_sentence.pack()
    e = Entry(root)
    e.pack()


    fetcher = ttk.Button(root, command=fetch, text='fetcher')
    fetcher.pack()
    
# choose cipher

def fetch():
    global L
    

    word=e.get()
    L = list(word)
    

    print(L)
    
    choose_caeser = ttk.Button(root, command=caeser_select, text='caeser')
    choose_vernam = ttk.Button(root, command=vernam, text='virnam')
    choose_caeser.pack()
    choose_vernam.pack()

# caeser cipher

def caeser_select():

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

    
    
    # start of program
    
    
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

    shift_number = Entry(root)
    how_many = Label(root, text='how many positions would you like to shift by?')
    how_many.pack()
    shift_number.pack()

    select_number = ttk.Button(root, text='select number', command=get_shift_number)
    select_number.pack()

    # choose shift direction

    label = Label(root, text="What direction would you like to shift? Please enter 'L' for left or 'R' for right: ")
    label.pack()

    shift_left = ttk.Button(root, text='shift left', command=we_shift_left)
    shift_left.pack()

    shift_right = ttk.Button(root, text='shift right', command=we_shift_right)
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

enter()

root.mainloop()
