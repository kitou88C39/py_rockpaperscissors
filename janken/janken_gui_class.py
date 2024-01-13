import random
import tkinter as tk
from PIL import Image, ImageTk //PIL パッケージから Image クラスと ImageTk クラスをインポート

gu, choki, pa = "グー", "チョキ", "パー"
hands = [gu, choki, pa]
WIN, DRAW, LOSE = "勝","相子","負"
rules = {
    (0,0):DRAW,(0,1):WIN, (0,2):LOSE,
    (1,0):LOSE,(1,1):DRAW, (1,2):WIN,
    (2,0):WIN,(2,1):LOSE, (2,2):DRAW
}

//View classを作成する
class View:
    def __init__(self):
        //じゃんけんの画像を置く インスタンス変数にする self.を先頭に入れる
        self.gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
        self.gu_image = ImageTk.PhotoImage(gu_image, master=root)

        self.choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
        self.choki_image = ImageTk.PhotoImage(choki_image, master=root)

        self.pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
        self.pa_image = ImageTk.PhotoImage(pa_image)

        self.tk.Label(root, image=gu_image).place(x=20, y=100)
        self.tk.Label(root, image=choki_image).place(x=160, y=100)
        self.tk.Label(root, image=pa_image).place(x=300, y=100)
        
    

//Applicationのクラスを作り、tk.Frameを継承する
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("420x400")
        master.title("ジャンケンゲーム")

        self.view = View()