import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import spearmanr



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



x = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 
3.3, 3.9, 5.7, 0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 0.7, 0.7]

count_level = 1 #パラメータの番号
leveldic = {"des": "記述的", "pc": "テキストの使いやすさ主成分", "crf": "参照の結束",
    "lsa": "LSA", "ld": "語彙の多様性", "cnc": "連結語", "sm": "状況モデル", 
    "syn": "構文の複雑さ", "dr": "構文パターン密度", "wrd": "単語情報", 
    "rd": "読みやすさ"} #ラベルとレベル名の対応
allparaldic = {1: "記述的", 2: "テキストの使いやすさ主成分", 3: "参照の結束", 4: "LSA", 5: "語彙の多様性", 6: "連結語", 7: "状況モデル", 8: "構文の複雑さ", 9: "構文パターン密度", 10: "単語情報", 
    11: "記述的", 12: "テキストの使いやすさ主成分", 13: "参照の結束", 14: "LSA", 15: "語彙の多様性", 16: "連結語", 17: "状況モデル", 18: "構文の複雑さ", 19: "構文パターン密度", 20: "単語情報", 
    21: "記述的", 22: "テキストの使いやすさ主成分", 23: "参照の結束", 24: "LSA", 25: "語彙の多様性", 26: "連結語", 27: "状況モデル", 28: "構文の複雑さ", 29: "構文パターン密度", 30: "単語情報",
    31: "記述的", 32: "テキストの使いやすさ主成分", 33: "参照の結束", 34: "LSA", 35: "語彙の多様性", 36: "連結語", 37: "状況モデル", 38: "構文の複雑さ", 39: "構文パターン密度", 40: "単語情報",
    41: "記述的", 42: "テキストの使いやすさ主成分", 43: "参照の結束", 44: "LSA", 45: "語彙の多様性", 46: "連結語", 47: "状況モデル", 48: "構文の複雑さ", 49: "構文パターン密度", 50: "単語情報", 
    51: "記述的", 52: "テキストの使いやすさ主成分", 53: "参照の結束", 54: "LSA", 55: "語彙の多様性", 56: "連結語", 57: "状況モデル", 58: "構文の複雑さ", 59: "構文パターン密度", 60: "単語情報", 
    61: "記述的", 62: "テキストの使いやすさ主成分", 63: "参照の結束", 64: "LSA", 65: "語彙の多様性", 66: "連結語", 67: "状況モデル",  68: "構文の複雑さ", 69: "構文パターン密度", 70: "単語情報",
    71: "記述的", 72: "テキストの使いやすさ主成分", 73: "参照の結束", 74: "LSA", 75: "語彙の多様性", 76: "連結語", 77: "状況モデル", 78: "構文の複雑さ", 79: "構文パターン密度", 80: "単語情報",
    81: "記述的", 82: "テキストの使いやすさ主成分", 83: "参照の結束", 84: "LSA", 85: "語彙の多様性", 86: "連結語", 87: "状況モデル", 88: "構文の複雑さ", 89: "構文パターン密度", 90: "単語情報",
    91: "記述的", 92: "テキストの使いやすさ主成分", 93: "参照の結束", 94: "LSA", 95: "語彙の多様性", 96: "連結語", 97: "状況モデル", 98: "構文の複雑さ", 99: "構文パターン密度", 100: "単語情報",
    101: "記述的", 102: "テキストの使いやすさ主成分", 103: "参照の結束", 104: "LSA", 105: "語彙の多様性", 106: "連結語"} #ラベルとレベル名の対応
count = 0 #軸のcount_listの順番を決める変数




soukan2=[]
    
for key, value in leveldic.items():
    soukankekka = {} #パラメーター番号：レベル内での相関係数の結果リスト
    count_level = 0
    while count_level < 107:
        if (new_list[count_level][1].lower()).startswith(key.lower()):
            #[3:39]まで数字
            #x軸の数値を取り出す
            suuti_list = new_list[count_level][3:39]
            suuti_list = new_list[count_level][4:36] #試し追加分
            
            #文字列を数値に変換
            y = [float(s) for s in suuti_list]
            #print(new_suuti_list)


            #相関計算
            x_np = np.array(x)
            y_np = np.array(y)


            #シャピロウィルク検定で正規性の確認
            #w値とp_value
            shap_w, shap_p_value = stats.shapiro(y)
            #p_valueが0.05以上なら，帰無仮説が採択→正規性がある
            if shap_p_value >= 0.05 :
                print(count_level,"は正規性があるといえる")
                #print(shap_p_value)


                #ピアソンの相関係数をとる
                # 相関行列を計算
                coef = np.corrcoef(x_np, y_np)
                soukan = coef[0][1]


            #p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
            else:
                print(count_level,"は正規性があるといえない")
                #print(shap_p_value)
            
                #スピアマンの順位相関係数
                correlation, pvalue = spearmanr(x, y)
                soukan = correlation
            
            ##############################
            

            #パラメータと相関係数でディクショナリを作成
            #soukankekka[count_level] = coef[0][1] # パラメータ，相関の結果
            soukankekka[count_level] = soukan # パラメータ，相関の結果
 
            

           
        count_level+=1

    #ディクショナリをソート
    #相関係数を絶対値(abs())で大きい順に並び替え
    soukankekka = sorted(soukankekka.items(), key = lambda x : abs(x[1]), reverse=True)
    print(leveldic[key],"レベル")
    print("<相関係数>")
    #パラメータ番号と相関係数の結果を，相関係数の大きい順で表示
    for s in soukankekka:
        print(s)
            
    print("------")
        
lst=[]
for s in range(1,108):
    lst.append(s)

left = np.array(lst)
height = np.array()
plt.bar(left, height, align="center")
plt.savefig("tadokutosyo1.png")


