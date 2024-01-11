//pattern①

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

//pattern②

win, draw, lose = "勝","相子","負"
rules = {
    (0,0):draw,(0,1):win, (0,2):lose,
    (1,0):lose,(1,1):draw, (1,2):win,
    (2,0):win,(2,1):lose, (2,2):draw
}

my_hand = 0
enemy_hand = 1
result = rules[(my_hand, enemy_hand)]
print(result)