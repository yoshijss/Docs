# coding: utf-8
try:
    import Tkinter
    import tkFont
except ImportError:
    import tkinter as Tkinter
    import tkinter.font as tkFont

from tkinter import ttk

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



def main():
    root = Tkinter.Tk()
    root.wm_title("Simple window")
    root.wm_iconname("simple")

    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()
