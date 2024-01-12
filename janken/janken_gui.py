import tkinter as tk
from PIL import Image, ImageTk //PIL パッケージから Image クラスと ImageTk クラスをインポート

//tkinterを使って画面を構築
root = tk.Tk()
root.geometry("420x400")

//じゃんけんの画像を置く
gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
gu_image = ImageTk.PhotoImage(gu_image, master=root)

tk.Label(root, image=gu_image).place(x=100, y=100)

root.mainloop()