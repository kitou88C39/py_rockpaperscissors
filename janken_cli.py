import random


hands = ["グー", "チョキ", "パー"]
win, draw, lose = "勝","相子","負"
rules = {
    (0,0):draw,(0,1):win, (0,2):lose,
    (1,0):lose,(1,1):draw, (1,2):win,
    (2,0):win,(2,1):lose, (2,2):draw
}

while True://無限ループ
    //inputを受け取って、intに変換する
    my_hand = int(input(
    '''0~2の数字を入力して下さい //''' '''　3連クォート　
    0:グー, 1:チョキ, 2:パー
    >>>'''))
    enemy_hand = ramdom.randint(0, 2)

    //自分の手と相手の手を表示する
    my_hand_str = hands[my_hand]
    enemy_hand_str = hands[enemy_hand]
    print("自分:" + "my_hand_str" + "相手:" + enemy_hand_str)

    //相子だったら、もう一度やり直す
    result = rules[(my_hand, enemy_hand)]
    print(result)
    //相子でなければ、終了
    if enemy_hand != my_hand:
        break