'''
Paul Talaga
CSCI 420 - Networking - Fall 2021
Simple TK program to count number of clicks.
Sept 7, 2021

'''

from tkinter import *
import time
import random

def buttonClicked(event):
	global output
	global counter
	print("Button was clicked!")
	#print(dir(output))
	counter += 1
	output.config(text = counter)
	time.sleep(2)

def boxDone(event = None):
	print("Got enter")
	print(dir(event.widget))
	print(event.widget.get())

def doStuff():
	global counter2
	global master
	global colors
	print(counter2)
	print(time.time())
	counter2 += 1
	master.after(100, doStuff)
	master.configure(background = colors[random.randint(0,len(colors)-1)])


master = Tk()

colors = ['green','red','blue','purple']

counter = 0
counter2 = 0

button = Button(master, text="Click Me")
button.grid(column = 0, row = 0)
button.bind('<Button>', buttonClicked)

output = Label(master, text= counter)
output.grid(column = 1, row = 0)

box = Entry(master)
box.grid(column = 2, row = 0)
box.bind('<Return>', boxDone)

master.after(100, doStuff)





mainloop()

