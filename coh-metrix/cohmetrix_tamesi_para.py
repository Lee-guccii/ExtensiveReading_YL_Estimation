import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random


###############
#ERFPTlevelとYLの相関
YL = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 
3.3, 3.9, 5.7, 0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 0.7, 0.7]

ERlevel = [6, 7, 8, 8, 10, 10, 11, 3, 4, 5, 4, 5, 7, 11, 13, 13, 8, 8, 10,
        14, 2, 2, 2, 9, 12, 12, 9, 3, 3, 3, 2, 2]

#相関計算
x_np = np.array(YL)
y_np = np.array(ERlevel)
    

# 相関行列を計算
coef = np.corrcoef(x_np, y_np)

print("ERFPTとYLの相関:",coef[0][1])
print("------------------------")

###############
#textをnew_listに読み込む
with open("CohMetrixOutput.txt", "r", encoding="utf-8") as f:
    list = f.readlines()

new_list = []

for i in list:
    word = i.split()
    new_list.append(word)



#####################################
#使いたいパラメータの数字を取り出す→相関の確認




count_list = [3, 31, 47, 92, 104, 106, 96, 99, 67, 102, 44, 77, 73,
              60, 100] #パラメータの番号
bookdic = {3: "総単語数", 31: "名詞の重なり", 47: "語彙の多様性", 92: "語彙の頻度", 
        104: "FRE", 106: "RDL２", 96: "単語の親しみやすさ", 99: "単語の意味性",
        67: "主動詞の前の単語数", 102: "動詞の上位概念語", 44: "LSA given/new",
        77: "前置詞の密度",73: "文章構造の類似性", 60: "因果関係のある動詞と助詞の割合",
        100: "単語の多義性"} #パラメータナンバーと指標名の対応
count_zyunbanX = 0 #X軸のcount_listの順番を決める変数
count_zyunbanY = 0 #Y軸のcount_listの順番を決める変数
soukankekka = {} #パラメータ：相関係数の結果　のディクショナリ


a=0


while count_zyunbanX < len(count_list):
    #X軸
    countX = count_list[count_zyunbanX] #count_listの中身を順番に出す
    
    #[3:39]まで数字
    #x軸の数値を取り出す
    suuti_listX = new_list[countX][3:39]
    suuti_listX = new_list[countX][4:36] #試し追加分
    
    #文字列を数値に変換
    x = [float(s) for s in suuti_listX]
    #print(new_suuti_list)

    #Y軸
    count_zyunbanY = 0
    while count_zyunbanY < len(count_list)-1:
        countY = count_list[count_zyunbanY] #count_listの中身を順番に出す

        if countY == countX:
            count_zyunbanY+=1
            countY = count_list[count_zyunbanY]
            

        #[3:39]まで数字
        #x軸の数値を取り出す
        suuti_listY = new_list[countY][3:39]
        suuti_listY = new_list[countY][4:36] #試し追加分
        
        #文字列を数値に変換
        y = [float(s) for s in suuti_listY]

        ##############################
        #相関をとる

        #相関計算
        x_np = np.array(x)
        y_np = np.array(y)

        # 相関行列を計算
        coef = np.corrcoef(x_np, y_np)

        print(bookdic[countX],"-",bookdic[countY])
        print("相関係数",coef[0][1])
        print("------")
    
        count_zyunbanY+=1
        a+=1

    count_zyunbanX+=1


print(a)
