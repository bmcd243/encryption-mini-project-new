from tkinter import *
from tkinter import ttk
import os
import sys
import time
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen_res = str(width) + 'x' + str(height)

print(screen_res)

if height < 1080:
    print("Eek, your monitor isn't even 1080p")


root.geometry(screen_res)
root.title("Encryption project")
root.iconbitmap('./images/key.jpg')





def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def hide_all_frames():
    caeser_frame.pack_forget()
    vernam_frame.pack_forget()
    explainer_frame.pack_forget()



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

        display_entered = Label("Phrase to convert is" + word)
        display_entered.pack()
    

        
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
    enter()

    
    # define lists
    convert = []
    final_numbers = []

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
        global shifty

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
        print("here")
        global final_letters
        print (final_numbers)
        number_to_letter = []

        print ("we go now")
        ranger = len(final_numbers)
        final_letters = []

        if any(y > 0 for y in final_numbers):
            for i in range(ranger):
                number_to_letter=chr(final_numbers[i]+96)
                print(number_to_letter)
                final_letters.append(number_to_letter)
                print("once")
                number_to_letter = []
            display_final_result()
        else:
            not_possible = Label(caeser_frame, text = "I am afraid that it isn't possible to encrypt that text, please restart the program to try again")
            not_possible.pack()

        

    def display_final_result():
        print ("number to letter is " + str((final_letters)))
        display_converted = Label(caeser_frame, text=str(final_letters))
        display_converted.pack()

  
        
    #     ask_decrypt_caeser_func()


    # def caeser_decrypt():
    #     print("Hello")


    # def ask_decrypt_caeser_func():
    #     print('sup')
    #     ask_caeser_decrypt = Label(caeser_frame, text="Would you like to decrypt")
    #     select_caeser_decrypt = ttk.Button(caeser_frame, text="Decrypt", command=caeser_decrypt)
    #     ask_caeser_decrypt.pack()
    #     select_caeser_decrypt.pack()



    



        


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

        fetcher = ttk.Button(text = 'Encrypt', command = lambda: fetch(e))
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
        global K
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

        # ask_decrypt_vernam_func()

    ### START VERNAM
    
    enter_plaintext()

    # def ask_decrypt_vernam_func():
    #     ask_decrypt = Label(vernam_frame, text="Would you like to decrypt")
    #     select_decrypt = ttk.Button(vernam_frame, text="Decrypt", command=vernam_decrypt)
    #     ask_decrypt.pack()
    #     select_decrypt.pack()

    # def vernam_decrypt():
    #     print("")

def explainer():
    hide_all_frames()
    explainer_frame.pack()


    tab_parent = ttk.Notebook(explainer_frame, width=800, height=400)
    symmetric_tab = ttk.Frame(tab_parent)
    asymmetric_tab = ttk.Frame(tab_parent)
    tab_parent.add(symmetric_tab, text="Symmetric")
    tab_parent.add(asymmetric_tab, text="Asymmetric")
    tab_parent.pack(expand=150, fill='both')

    
    ### display versus image
    def display_image():
            image_1 = ImageTk.PhotoImage(Image.open("./images/versus.png"))
            photo = Label(explainer_frame, image = image_1)
            photo.image = image_1
            photo.pack()

    ### symmetric encryption function
    def symmetric():

        symmetric_title = Label(symmetric_tab, text="Symmetric encryption")
        symmetric_title.pack()
        symmetric_title.config(font=("Courier", 44))

        symmetric_text = Text(symmetric_tab, height=10, width=50)
        symmetric_text.insert(END, '\nWhat is symmetric encryption?\n', 'big')
        quote = """
        Symmetric encryption aka secret key encryption uses one single key to encrypt and decrypt data. You have to share this key with the recipient. Let’s say you want to say I love you Mom, you would write your email, then set a secret key to encrypt it. When mom receives the message she would enter the secret key to decrypt the email.


        """
        symmetric_text.insert(END, quote, 'color')
        symmetric_text.pack(fill=X)



        symmetric_tree=ttk.Treeview(symmetric_tab)

        symmetric_tree["columns"]=("one")
        symmetric_tree.column("#0", width=270, minwidth=270)
        symmetric_tree.column("one", width=150, minwidth=150)

        symmetric_tree.heading("#0",text="Pros",anchor=W)
        symmetric_tree.heading("one", text="Cons",anchor=E)

        symmetric_tree.insert(parent="", index="end", iid="#0", text="Easy to set up", values=("The secret key needs to be shared with the recipient",))
        symmetric_tree.insert(parent="", index="end", iid="one", text="All ages and backgrounds can use it", values=("If the same key is used multiple times then the hacker needs to only figure it out once and then have access to multiple items of data",))

        
        symmetric_tree.pack(side="top",fill="x")
    
    
    ### asymmetric encryption function
    def asymmetric():
        asymmetric_title = Label(asymmetric_tab, text="Asymmetric encryption")
        asymmetric_title.pack()
        asymmetric_title.config(font=("Courier", 44))

        asymmetric_text = Text(asymmetric_tab, height=10, width=50)
        asymmetric_text.insert(END, '\nWhat is asymmetric encryption?\n', 'big')
        quote = """
        The public key and the private key are not the same thing but they are related. Moreover, you create your message then encrypt it with the recipient’s public key. After that, if the recipient wants to decrypt your message he/she would have to do it with his/her private key. Keep the (private) key private at all times, the best practice would be to store it locally. One requires greater knowledge than the average person to make this happen.

The emailing software of the recipient will see if the private key corresponds with the public key and then it will prompt the user to type the passphrase to decrypt the message. Some best practices for asymmetric encryption: Use 2048 bits and above keys. Finally creating strong keys is the foundation of Asymmetric encryption. A good encryption practice would be to use multiple encryption methods instead of just one. Not everyone knows how to use Asymmetric encryption so there may be occasions you have to use either Hash functions or Symmetric encryption.


        """
        asymmetric_text.insert(END, quote, 'color')
        asymmetric_text.pack(fill=X)

        asymmetric_tree=ttk.Treeview(asymmetric_tab)

        asymmetric_tree["columns"]=("one")
        asymmetric_tree.column("#0", width=270, minwidth=270)
        asymmetric_tree.column("one", width=150, minwidth=150)

        asymmetric_tree.heading("#0",text="Pros",anchor=W)
        asymmetric_tree.heading("one", text="Cons",anchor=E)

        asymmetric_tree.insert(parent="", index="end", iid="#0", text="It does not force the user to share (secret) keys as symmetric encryption does, therefore removing the necessity of key distribution", values=("It is time-intensive",))
        asymmetric_tree.insert(parent="", index="end", iid="one", text="Asymmetric encryption supports digital signing which authenticates the recipient identity and make sure that message is not tampered in transit", values=("Requires considerably more effort",))

        asymmetric_tree.pack(side="top",fill="x")


    symmetric()
    asymmetric()
    display_image()



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
