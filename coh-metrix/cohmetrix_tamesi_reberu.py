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
count = 0 #軸のcount_listの順番を決める変数





    

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
        




