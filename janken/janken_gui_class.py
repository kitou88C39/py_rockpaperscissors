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