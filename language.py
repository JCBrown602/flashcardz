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
	global hinter, hint_count

	# Clear labels and entry
	answer_label.config(text="")
	my_entry.delete(0, END)
	hint_label.config(text="")

	# Reset hint info
	hinter = ""
	hint_count = 0

	# Random selection
	global random_word
	random_word = randint(0, count-1)
	# Update label
	spanish_word.config(text=words[random_word][0])

def answer():
	if my_entry.get().capitalize() == words.[random_word][1]:
		answer_label.config(text=f"Correct. {words[random_word][0]} means {words[random_word][1]}.")
	else:
		answer_label.config(text=f"Incorrect. {words[random_word][0]} means {my_entry.get().capitalize()}.")

# Keep track of hints
hinter = ""
hint_count = 0

def hint():
	global hint_count
	global hinter

	if hint_count < len(words[random_word][1]):
		hinter = hinter + words[random_word][1][hint_count]
		hint_label.config(text=hinter)
		hint_count +=1

spanish_word = Label(root, text="", font=("Helvetica", 30))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

next()

root.mainloop()
