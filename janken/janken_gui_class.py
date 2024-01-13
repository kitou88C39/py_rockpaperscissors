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
        
    

//Applicationのクラスを作り、tk.Frameを継承する
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("420x400")
        master.title("ジャンケンゲーム")

        self.view = View()