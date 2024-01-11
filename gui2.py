import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self)
        self.quit = tk.Button(self,text="Button", command=self.master.destroy):
        self.quit.place(x=80, y=80)
