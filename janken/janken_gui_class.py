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

# View classを作成する
class View:
    def __init__(self):
        //じゃんけんの画像を置く インスタンス変数にする self.を先頭に入れる
        self.gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
        self.gu_image = ImageTk.PhotoImage(self.gu_image, master=root)

        self.choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
        self.choki_image = ImageTk.PhotoImage(self.choki_image, master=root)

        self.pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
        self.pa_image = ImageTk.PhotoImage(self.pa_image)

        self.images = [self.gu_image, self.choki_image, self.pa_image]

        self.gu_label = tk.Label(root, image=self.gu_image)
        self.gu_label.place(x=20, y=100)

        self.choki_label =.tk.Label(root, image=self.choki_image)
        self.choki_label.place(x=160, y=100)

        self.pa_label = tk.Label(root, image=self.pa_image)
        self.pa_label.place(x=300, y=100)

        self.gu_btn = tk.Button(frame, text="gu")
        self.gu_btn.place(x=50, y=320)

        self.choki_btn = tk.Button(frame, text="choki")
        self.choki_btn.place(x=190, y=320)

        self.pa_btn = tk.Button(frame, text="pa")
        self.pa_btn.place(x=335, y=320)

        //相手の手を表示させる
        self.enemy_label = tk.Label(root, image=self.gu_image)
        self.enemy_label.place(x=160, y=20)
       
       //画面を表示させる text_labelの作成
       self.text_label = tk.Label(root, text="最初はgu! じゃんけん!")
       self.text_label.place(x=140, y=140)

       self.retry_btn = tk.Button(root, text="リトライ")

# ジャッジとリセット
    def reset(self):

        self.retry_button.place_forget()
        self.gu_btton["state"] = tk.ACTIVE
        self.choki_btton["state"] = tk.ACTIVE
        self.pa_btton["state"] = tk.ACTIVE

        self.enemy_label.configure(image=self.images[0])
        self.text_label.configure("最初はgu! じゃんけん!")



# 結果を表示する
    def display(self, enemy, result):
        self.enemy_label.configure(image=self.images[enemy])
        if result == DRAW:
            self.text_label.configure(text="相子")
        elif result == WIN:
            self.text_label.configure(text="勝ち")
        elif result == LOSE:
            self.text_label.configure(text="負け")
    
    def show_retry(self):
        self.retry_button.place(x=185, y=360)
        self.gu_btton["state"] = tk.DISABLED
        self.choki_btton["state"] = tk.DISABLED
        self.pa_btton["state"] = tk.DISABLED


    

    

# Applicationのクラスを作り、tk.Frameを継承する
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("420x400")
        master.title("ジャンケンゲーム")

        self.view = View()

        self.view.gu_btton["command"]= lambda: self.judge(0)
        self.view.choki_btton["command"]= lambda: self.judge(1)
        self.view.pa_btton["command"]= lambda: self.judge(2)

# リトライボタンの実装
        self.view.retry_button["command"]= self.retry

# じゃんけんの実際の処理
    def judge(self, my_hand):
        enemy = random.randient(0,2)
        result = rules[(my_hand, enemy)]
        self.view.display(enemy, result)
        if.result != DRAW:
            self.view.show_retry()

    def retry(self):
        self.view.reset()

root = tk.Tk()
app = Application(master=root)
app.mainloop()