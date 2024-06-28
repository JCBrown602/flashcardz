from tkinter import *
from random import randint
from cards import words

root = Tk()
root.title('Spanish Language Cards')
photo = PhotoImage(file = 'mex-flag_2.png')
root.iconphoto(False, photo)
root.geometry("550x410")


# Get a count of the words
count = len(words)

def next():
	# Random selection
	random_word = randint(0, count-1)
	# Update label
	spanish_word.config(text=words[random_word][0])

def answer():
	pass



spanish_word = Label(root, text="", font=("Helvetica", 30))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer")
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint")
hint_button.grid(row=0, column=2, padx=20)

# Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

next()

root.mainloop()
