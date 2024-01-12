import tkinter as tk
from PIL import Image, ImageTk //PIL パッケージから Image クラスと ImageTk クラスをインポート

//tkinterを使って画面を構築
root = tk.Tk()
root.geometry("420x400")

//じゃんけんの画像を置く
gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
gu_image = ImageTk.PhotoImage(gu_image, master=root)

choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
choki_image = ImageTk.PhotoImage(choki_image, master=root)

pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
pa_image = ImageTk.PhotoImage(pa_image, master=root)

tk.Label(root, image=gu_image).place(x=100, y=100)
tk.Label(root, image=choki_image).place(x=100, y=100)
tk.Label(root, image=pa_image).place(x=100, y=100)

root.mainloop()