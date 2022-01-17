import numpy as np
from scipy import stats
from scipy.stats import spearmanr
import re



###############
#textをnew_listに読み込む
with open("tango_sitasimiyasusa_list.txt", "r", encoding="utf-8") as f:
    list = f.readlines()

new_list = []

for i in list:
    word = i.split()
    new_list.append(word)



#####################################
#使いたいパラメータの数字を取り出す→相関の確認




#単語名，親やすさ（100：親しみがない，700：親しみがある）
sitasimi_tango={}

count_level = 1
while count_level < 1945:

    #[3:39]まで数字
    #x軸の数値を取り出す
    tango_list = new_list[count_level][0] #試し追加分
    suuti_list = new_list[count_level][5] #試し追加分

    
    #文字列を数値に変換
    y = round(float(suuti_list)*100)
    sitasimi_tango[tango_list] = y
    

 
    count_level+=1


print(sitasimi_tango)




