import random
mport tkinter as tk
from PIL import Image, ImageTk //PIL パッケージから Image クラスと ImageTk クラスをインポート

gu, choki, pa = "グー", "チョキ", "パー"
hands = [gu, choki, pa]
WIN, DRAW, LOSE = "勝","相子","負"
rules = {
    (0,0):DRAW,(0,1):WIN, (0,2):LOSE,
    (1,0):LOSE,(1,1):DRAW, (1,2):WIN,
    (2,0):WIN,(2,1):LOSE, (2,2):DRAW
}

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

tk.Label(root, image=gu_image).place(x=20, y=100)
tk.Label(root, image=choki_image).place(x=160, y=100)
tk.Label(root, image=pa_image).place(x=300, y=100)

//ボタンをクリックしたら、起動する
def press_gu():
    judge(0)
def press_choki():
    judge(1)
def press_pa():
    judge(2)

tk.Button(frame, text="gu" command=press_gu).place(x=50, y=320)
tk.Button(frame, text="choki" command=press_choki).place(x=190, y=320)
tk.Button(frame, text="pa" command=press_pa).place(x=335, y=320)

//相手の手を表示させる
enemy_label = tk.Label(root, image=gu_image)
enemy_label.place(x=160, y=20)
//画面を表示させる　text_labelの作成
text_label = tk.Label(root, text="最初はgo! じゃんけん!")
text_label.place(x=140, y=140)

//じゃんけんの判定を表示する
def judge(me):
    enemy = random.randint(0,2)
    result = rules[(me, enemy)]
//画面上に結果を表示させる
if result == DRAW:
    text_label.configure(text_result)


root.mainloop()