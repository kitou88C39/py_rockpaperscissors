gu, choki, pa = "グー","チョキ","パー"
win, draw, lose = "勝","相子","負"

my_hand = gu
enemy_hand = pa

if my_hand == enemy_hand:
    print(draw)
elif (my_hand == gu and enemy_hand == choki) or\
    (my_hand == pa and enemy_hand == gu) or\
    (my_hand == choki and enemy_hand == pa):
    print(win)
else
    print(lose)