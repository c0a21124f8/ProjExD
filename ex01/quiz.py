import random
import datetime


toi = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオからみてどんな関係？"]
ans01 = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]

i = random.randint(0,4)
def shutudai():
    st = datetime.datetime.now()
    ans = input(toi[i])
    return ans

def kaito(a):
    if a in ans01[i]:
        print("正解！！！")
    else:
        print("出直してこい")
    ed = datetime.datetime.now()
    x = str((ed-st).seconds)
    print("回答時間" + x + "秒")

st = datetime.datetime.now()
kaito(shutudai())

