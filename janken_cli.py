import random

gu, choki, pa = "グー", "チョキ", "パー"
hands = [gu, choki, pa]
WIN, DRAW, LOSE = "勝","相子","負"
rules = {
    (0,0):DRAW,(0,1):WIN, (0,2):LOSE,
    (1,0):LOSE,(1,1):DRAW, (1,2):WIN,
    (2,0):WIN,(2,1):LOSE, (2,2):DRAW
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