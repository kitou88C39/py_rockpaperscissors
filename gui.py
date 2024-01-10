import tkinter as tk

root = tk.TK()
root.geometry("200 * 200")

frame = tk.Frame(master=root)
frame.pack(expand=True, fill="both")

button = tk.Button(frame, text="Button", command=root.destroy)
button.place(x=80, y=80)

root.mainloop()