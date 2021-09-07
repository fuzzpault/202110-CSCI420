'''
Paul Talaga
CSCI 420 - Networking - Fall 2021
Simple TK program to count number of clicks.
Sept 7, 2021

'''

from tkinter import *

def buttonClicked(event):
	global output
	global counter
	print("Button was clicked!")
	#print(dir(output))
	counter += 1
	output.config(text = counter)

master = Tk()

counter = 0

button = Button(master, text="Click Me")
button.grid(column = 0, row = 0)
button.bind('<Button>', buttonClicked)

output = Label(master, text= counter)
output.grid(column = 1, row = 0)





mainloop()

