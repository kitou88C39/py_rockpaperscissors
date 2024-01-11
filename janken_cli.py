import ramdom

hands = ["グー", "チョキ", "パー"]
win, draw, lose = "勝","相子","負"
rules = {
    (0,0):draw,(0,1):win, (0,2):lose,
    (1,0):lose,(1,1):draw, (1,2):win,
    (2,0):win,(2,1):lose, (2,2):draw
}

my_hand = int(input('''0~2の数字を入力して下さい 0:グー, 1:チョキ, 2:パー >>>'''))
enemy_hand = ramdom.randint(0, 2)

my_hand_str = hands[my_hand]
enemy_hand_str = hands[enemy_hand]
print()