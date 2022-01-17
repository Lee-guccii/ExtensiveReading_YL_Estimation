import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import spearmanr
import scipy



###############
tosyo=0
new_list_tadoku = []
new_list_ippann = []

#textをnew_listに読み込む

#多読図書
with open("CohMetrixOutput.txt", "r", encoding="utf-8") as f:
    list_tadoku = f.readlines()


for i in list_tadoku:
    word_tadoku = i.split()
    new_list_tadoku.append(word_tadoku)


#一般図書
with open("CohMetrixOutput(ippann2).txt", "r", encoding="utf-8") as f:
    list_ippan = f.readlines()

for i in list_ippan:
    word_ippan = i.split()
    new_list_ippann.append(word_ippan)
    



#####################################
#多読図書のYL
x_tadoku = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 
            1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 3.3, 3.9, 5.7, 
            0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 
            0.7, 0.7]

#一般図書のYL
x_ippan = [5.0, 6.0, 6.5, 6.5, 8.0, 8.5, 7.0, 8.0, 5.0, 6.5, 
           8.0, 5.0, 8.0, 7.5, 5.5, 7.5, 8.0, 8.0, 7.0, 8.0, 
           8.0, 5.0, 8.0, 5.0, 5.0, 8.0, 8.5, 5.5, 8.0, 5.5,
           8.0, 5.0]


#多読図書と一般図書のYL
x_zenbu = x_tadoku + x_ippan


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
        if (new_list_tadoku[count_level][1].lower()).startswith(key.lower()):
            #[3:39]まで数字
            #x軸の数値を取り出す
            suuti_list_tadoku = new_list_tadoku[count_level][4:36]
            suuti_list_ippan = new_list_ippann[count_level][3:35] 
            
            #文字列を数値に変換
            tadoku = [float(s) for s in suuti_list_tadoku]
            ippan = [float(s) for s in suuti_list_ippan]

            #相関係数計算用
            y_zenbu = tadoku + ippan
            

            tadoku_np = np.array(tadoku)
            ippan_np = np.array(ippan)


            x_zenbu_np = np.array(x_zenbu)
            y_zenbu_np = np.array(y_zenbu)





            #シャピロウィルク検定で正規性の確認
            #w値とp_value
            shap_w_tadoku, shap_p_value_tadoku = stats.shapiro(tadoku_np)
            shap_w_ippan, shap_p_value_ippan = stats.shapiro(ippan_np)
            

            #F検定で等分散性の確認
            fkentei_w, fkentei_p_value = scipy.stats.bartlett(tadoku_np,ippan_np)


            
            #p_valueが0.05以上なら，帰無仮説が採択→正規性がある
            if (shap_p_value_tadoku >= 0.05) and (shap_p_value_ippan >= 0.05) :
                #print(count_level,"は正規性があるといえる")

                #print("正規性があるといえる")
                #print(shap_p_value)


                #ピアソンの相関係数をとる
                # 相関行列を計算
                coef = np.corrcoef(x_zenbu_np, y_zenbu_np)
                soukan = coef[0][1]



            #p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
            else:
                #print("正規性があるといえない")
                #print(shap_p_value)
                        
                #スピアマンの順位相関係数
                correlation, pvalue = spearmanr(x_zenbu_np, y_zenbu_np)
                soukan = correlation
            
            #パラメータと相関係数でディクショナリを作成
            soukankekka[count_level] = soukan #パラメータ,相関の結果




        count_level+=1


    #ディクショナリをソート
    #相関係数を絶対値(abs())で大きい順に並び替え
    soukankekka = sorted(soukankekka.items(), key = lambda x : abs(x[1]), reverse=True)
    print(leveldic[key],"レベル")
    print("<相関係数>")
    #パラメータ番号と相関係数の結果を，相関係数の大きい順で表示
    for s in soukankekka:
        print(s)
            
    print("------------")

