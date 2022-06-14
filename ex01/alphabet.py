import random
import string
import datetime

t_mozi = 10
k_mozi = 2




def shutudai():
    count = 0
    mozi = "".join(random.choice(string.ascii_letters) for _ in range(t_mozi))
    mozi = str.upper(mozi)
    mozi_list =[]
    k_mozi_list = []
    for i in range(len(mozi)):
        mozi_list.append(mozi[i])
    mozi_list_moto = mozi_list.copy()

    while count < 1 :
        random.shuffle(mozi_list)
        print(" ".join(mozi_list))
        print(mozi_list_moto)
        print(k_mozi_list)
        toi = input("欠損文字はいくつあるでしょうか？")
        if int(toi) == (k_mozi):
            print("正解です。それでは具体的に欠損文字を１つずづ入力してください")
            count += 1
        else:
            print("不正解です。二度と間違えんな。")

    while count < k_mozi:
        x = [] * k_mozi
        for i in range(k_mozi):
            x[i] = input(str(i + 1) +"つ目の文字数を入力してください")
        if x in k_mozi_list:
            print("おめでとう君が神だ")
            count += 1
        else:
            print("不正解です。二度と間違えんな。")
    return None
shutudai()
    
