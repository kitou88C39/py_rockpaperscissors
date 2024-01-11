gu, choki, pa = "グー","チョキ","パー"
win, draw, lose = "勝","相子","負"

my_hand = go
enemy_hand = pa

if my_hand == enemy_hand:
    print(draw)
elif my_hand == gu and enemy_hand == choki:
    print(win)
else
    print(lose)