//pattern①
//ramdomというmoduleをimportする
import random
//listを作成する
hands = ["グー", "チョキ", "パー"]

i = ramdom.randint(0, 2)
hand = hands[i]
print(hand)

//pattern②
hands = ["グー", "チョキ", "パー"]

//inputで関数に文字列を引数として渡すと、その文字列はターミナルに出力される
my_input = input(input("0~2の数字を入力して下さい>>>"))
print(my_input)
i = int(my_input)
hand = hands[i]
print(hand)