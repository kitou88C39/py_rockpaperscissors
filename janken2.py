//pattern①
import ramdom

hands = ["グー", "チョキ", "パー"]

i = ramdom.randint(0, 2)
hand = hands[i]
print(hand)

//pattern②
hands = ["グー", "チョキ", "パー"]

my_input = input(input("0~2の数字を入力して下さい>>>"))

i = int(my_input)
hand = hands[i]
print(hand)