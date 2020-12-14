from tkinter import *
from tkinter import ttk
import os
import sys
import time
import tkinter.font as tkFont




root = Tk()
root.geometry('1000x800')
root.title("Encryption project")
root.iconbitmap('./images/key.jpg')


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

    # label_one = Label(root, text = 'Hello')
    # label_one.config("Courier", 50)
    # label_one.pack()

    

    def fetch():
        word=e.get()
        print(word)
        as_list = list(word)
        letter_to_number(as_list)
    
        
    fetcher = ttk.Button(caeser_frame, command=fetch, text='Encrypt')
    fetcher.pack()

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
    

    def enter():
        # enter phrase to be encrypted
        global e
        enter_sentence = Label(caeser_frame, text="Please enter a word/sentence to be encrypted below: ")
        enter_sentence.pack()
        e = Entry(caeser_frame)
        e.pack()

    
    # define lists
    convert = []
    final_numbers = []
    final_letters = []

    # convert letters to corresponding numbers
    
    def letter_to_number(L):
        global length
        length = len(L)
        for i in range(length):
            number = ord(L[i]) - 96
            convert.append(number)
        print(convert)
        shift_num_fun()

    # choose how many positions to shift by
    def shift_num_fun():

    # fetch shift by how many
        def get_shift_number():
            global shifty
            shifty = shift_number.get()

        shift_number = Entry(caeser_frame)
        how_many = Label(caeser_frame, text='how many positions would you like to shift by?')
        how_many.pack()
        shift_number.pack()

        select_number = ttk.Button(caeser_frame, text='select number', command=get_shift_number)
        select_number.pack()

        shift_direct_num()

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
        number_to_letter = []

        print ("we go now")
        print (len(final_numbers))

        for i in range(len(final_numbers)):
            print(i)
            number_to_letter=chr(final_numbers[i]+96)
            final_letters.append(number_to_letter)
            number_to_letter = []
            print(final_letters)
            

        print ("number to letter is " + str((final_letters)))

    choose_decrypt = ttk.Button(caeser_frame, text="Decrypt message", command=caeser_decrypt)
    choose_decrypt.pack()

    def caeser_decrypt():
        print("Hello")

    enter()



        


def vernam():
    ### vernam cipher

    hide_all_frames()

    #pack vernam frame
    vernam_frame.pack()
    

    ### get message to encrypt

    def enter_plaintext():
        enter_sentence = Label(vernam_frame, text="Please enter a word/sentence to be encrypted below: ")
        enter_sentence.pack()
        e = Entry(vernam_frame)
        e.pack()

        fetcher = ttk.Button(text = 'Encrypt', command = lambda:fetch(e))
        fetcher.pack()

    ### fetch input

    def fetch(input):
        global word
        word=input.get()
        print(word)
        length = len(word)
        create_key(length)
    ### create key

    def create_key(L):
        waiting = Label(vernam_frame, text="Creating key...")
        waiting.pack()
        import random
        K = []
        for i in range(L):
            current = chr(random.randrange(97, 97 + 26))
            K.append(current)
        print(K)
        string = ""
        print_K = string.join(K)

        display_key = Label(vernam_frame, text="The key is: " + str(print_K))
        display_key.pack()

        encrypt(word, K)

    ### VERNAM ENCRYPT
    def encrypt(message_to_encrypt, key):
        message_binary = ''.join(format(ord(i), 'b') for i in message_to_encrypt)
        key_binary = ''.join(format(ord(i), 'b') for i in key)

        encrypted_binary = message_binary + key_binary

        print (encrypted_binary)

        n = 8

        split_strings = []

        for i in range(0, len(encrypted_binary), n):
            split_strings.append(encrypted_binary[i : i + n])


        print (split_strings)

        encrypted_message = []

        for i in range(len(split_strings)):
            int(split_strings[i], 2)
            current = chr(int(split_strings[i], 2))
            encrypted_message.append(current)

        print ("You're encrypted message is: " + str(encrypted_message))

        empty = ""
        to_string = empty.join(encrypted_message)

        display_vernam = Label(vernam_frame, text="You're encrypted message is: " + str(to_string))
        display_vernam.pack()

    ### START VERNAM
    
    enter_plaintext()

def explainer():
    hide_all_frames()
    explainer_frame.pack()


    tab_parent = ttk.Notebook(explainer_frame, width=800, height=800)
    symmetric_tab = ttk.Frame(tab_parent)
    asymmetric_tab = ttk.Frame(tab_parent)
    tab_parent.add(symmetric_tab, text="Symmetric")
    tab_parent.add(asymmetric_tab, text="Asymmetric")
    tab_parent.pack(expand=100, fill='both')

    def symmetric():
        symmetric_title = Label(symmetric_tab, text="Symmetric encryption")
        symmetric_title.pack()
        symmetric_title.config(font=("Courier", 44))

        symmetric_tree=ttk.Treeview(symmetric_tab)

        symmetric_tree["columns"]=("one")
        symmetric_tree.column("#0", width=270, minwidth=270)
        symmetric_tree.column("one", width=150, minwidth=150)

        symmetric_tree.heading("#0",text="Pros",anchor=W)
        symmetric_tree.heading("one", text="Cons",anchor=E)

        symmetric_tree.insert(parent="", index="end", iid="#0", text="Easy to set up", values=("The secret key needs to be shared with the recipient",))
        symmetric_tree.insert(parent="", index="end", iid="one", text="All ages and backgrounds can use it", values=("If the same key is used multiple times then the hacker needs to only figure it out once and then have access to multiple items of data",))

        
        symmetric_tree.pack(side="top",fill="x")

    def asymmetric():
        asymmetric_title = Label(asymmetric_tab, text="Asymmetric encryption")
        asymmetric_title.pack()
        asymmetric_title.config(font=("Courier", 44))

        asymmetric_tree=ttk.Treeview(symmetric_tab)

        asymmetric_tree["columns"]=("one")
        asymmetric_tree.column("#0", width=270, minwidth=270)
        asymmetric_tree.column("one", width=150, minwidth=150)

        asymmetric_tree.heading("#0",text="Pros",anchor=W)
        asymmetric_tree.heading("one", text="Cons",anchor=E)

        asymmetric_tree.insert(parent="", index="end", iid="#0", text="It does not force the user to share (secret) keys as symmetric encryption does, therefore removing the necessity of key distribution", values=("It is time-intensive",))
        asymmetric_tree.insert(parent="", index="end", iid="one", text="Asymmetric encryption supports digital signing which authenticates the recipient identity and make sure that message is not tampered in transit", values=("Requires considerably more effort",))
    
    symmetric()
    asymmetric()




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
menu_1.add_command(label="Symmetric and Asymmetric encryption", command=explainer)
menu_1.add_command(label="Restart Program", command=restart)


caeser_frame = Frame(root, width=800, height=1000)
vernam_frame = Frame(root, width=800, height=1000)
explainer_frame = Frame(root, width=800, height=1000)


root.mainloop()
