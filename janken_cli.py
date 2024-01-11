hands = ["グー", "チョキ", "パー"]

win, draw, lose = "勝","相子","負"
rules = {
    (0,0):draw,(0,1):win, (0,2):lose,
    (1,0):lose,(1,1):draw, (1,2):win,
    (2,0):win,(2,1):lose, (2,2):draw
}

my_hand = input("0~2の数字を入力して下さい>>>")
enemy_hand = 1
result = rules[(my_hand, enemy_hand)]
print(result)