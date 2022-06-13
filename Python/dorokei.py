import random
import math

def calc_distance(x1, y1, x2, y2):
    # ２点間の距離を求める
    diff_x = x1 - x2
    diff_y = y1 - y2
    
    return math.sqrt(diff_x**2 + diff_y**2)

kei_x = random.randrange(0, 5)  # 泥棒のx座標
kei_y = random.randrange(0, 5)  # 泥棒のy座標

doro_x = random.randrange(0, 5) # 警察のx座標
doro_y = random.randrange(0, 5) # 警察のy座標

# 泥棒と警察の位置が異なる間、処理を繰り返す
while (doro_x != kei_x) or (doro_y != kei_y):

    # 泥棒と警察の距離を表示する
    distance = calc_distance(kei_x, kei_y, doro_x, doro_y)
    print("泥棒との距離:", distance, "\n")
    
    # キー入力に応じて、警察を移動する
    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動　")
    if c == "n":
        kei_y = kei_y - 1
    elif c == "s":
        kei_y = kei_y + 1
    elif c == "w":
        kei_x = kei_x - 1
    elif c == "e":
        kei_x = kei_x + 1

print("泥棒を捕まえた！")
