#!/usr/bin/python3

import tkinter as tk

def callback(event):
	print("clicked at", event.x, event.y) 

#=================================================
# main function
#=================================================
if __name__  == '__main__':
	root = tk.Tk()
	frame = tk.Frame(root, width=100, height=100)
	frame.bind("<Button-1>", callback)
	frame.pack()
	root.mainloop()
